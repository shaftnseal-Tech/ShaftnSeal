from dataclasses import dataclass
from typing import Optional
import pandas as pd
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # For headless environments like Django
import matplotlib.pyplot as plt
from django.conf import settings

@dataclass 
class PumpSystemCurve:
    h1: float
    h2: float
    p1: float
    p2: float
    Qnp: float
    Hnp: float
    Qact: float
    temp: float
    psp: float
    pdp: float
    N1: float
    N2: float
    test_file: Optional[str] = None
    pump_philosophy: str = "1R + 1S"

    def get_specific_gravity(self) -> float:
        csv_path = os.path.join(os.path.dirname(__file__), "specific_gravity.csv")
        df = pd.read_csv(csv_path)
        if self.temp < 0 or self.temp > 300:
            raise ValueError("Please enter a temperature between 0 and 300.")
        df['Temperature'] = df['Temperature'].astype(float)
        sg_series = df.loc[df['Temperature'].round(2) == round(float(self.temp), 2), 'Specific_Gravity']
        if not sg_series.empty:
            return round(float(sg_series.values[0]), 4)
        else:
            raise ValueError(f"Specific gravity not found for temperature: {self.temp}")

    def get_static_head(self) -> float:
        SG = self.get_specific_gravity()
        return (self.h2 - self.h1) + (self.p2 - self.p1) * (10 / SG)

    def read_test_data(self):
        if not self.test_file:
            raise ValueError("No test file provided.")
        if not os.path.exists(self.test_file):
            raise FileNotFoundError(f"Test file not found: {self.test_file}")

        ext = os.path.splitext(self.test_file)[1].lower()
        if ext in ['.xlsx', '.xls']:
            df = pd.read_excel(self.test_file)
        elif ext == '.csv':
            df = pd.read_csv(self.test_file)
        else:
            raise ValueError("Unsupported test file format. Use CSV or Excel.")

        if 'Q' not in df.columns or 'H' not in df.columns:
            raise ValueError("Test file must contain 'Q' and 'H' columns.")

        return df

    def plot_pumpsystem_graph(self) -> str:
        SG = self.get_specific_gravity()
        static_head = self.get_static_head()

        fig, ax = plt.subplots(figsize=(12, 7))

        # Theoretical SRC
        k1 = (self.Hnp - static_head) / (self.Qnp ** 2)
        Qi = np.linspace(0, max(self.Qnp, self.Qact) * 1.5, 100)
        src_theoretical = k1 * (Qi ** 2) + static_head
        static_line = np.full_like(Qi, static_head)

        ax.plot(Qi, src_theoretical, label='Theoretical SRC', color='blue')
        ax.plot(Qi, static_line, label='Static Head', color='green')

        # Actual SRC
        H_actual = (self.pdp - self.psp) * 10 / SG
        k2 = (H_actual - static_head) / (self.Qact ** 2)
        src_actual = k2 * (Qi ** 2) + static_head
        ax.plot(Qi, src_actual, label='Actual SRC', color='red', linestyle='--')

        if self.test_file:
            try:
                df = self.read_test_data()
                Q = df['Q'].astype(float)
                H = df['H'].astype(float)

                # Pump test curve
                ax.plot(Q, H, label='Pump Test Curve (Q,H)', marker='o', linestyle='-', color='purple')

                # VM Curve
                k3 = self.N2 / self.N1
                k4 = (self.N2 ** 2) / (self.N1 ** 2)
                Qvm = Q * k3
                Hvm = H * k4
                ax.plot(Qvm, Hvm, label='VM Curve (Qvm,Hvm)', marker='x', linestyle='-', color='orange')

                # Experimental data based on pump philosophy
                if self.pump_philosophy == "2R + 1S":
                    Q_exp2 = Q * 2
                    ax.plot(Q_exp2, H, label='Experimental (2R + 1S)', linestyle='--', color='grey')

                # Nameplate point
                ax.scatter(self.Qnp, self.Hnp, color='red', label='Nameplate Point (Qnp, Hnp)', zorder=5)

            except Exception as e:
                print(f"Warning: Could not load test data: {e}")

        # Set limits
        y_min = 550
        y_max = max(static_head, H_actual, self.Hnp) + 300
        ax.set_ylim(y_min, y_max)
        ax.set_yticks(np.arange(y_min, y_max + 1, 100))

        x_max = max(self.Qnp, self.Qact) * 2 + 10
        ax.set_xlim(0, x_max)
        ax.set_xticks(np.arange(0, x_max + 1, 10))

        # Labels and legend
        ax.set_title('Combined System Resistance & Pump Test Curve')
        ax.set_xlabel('Flow Rate (Q)')
        ax.set_ylabel('Total Head (H)')
        ax.grid(True)
        ax.legend(loc='best')

        plt.tight_layout()

        # Save plot
        combined_path = os.path.join(settings.MEDIA_ROOT, 'combined_pump_system_curve.png')
        plt.savefig(combined_path)
        plt.close()

        return combined_path
