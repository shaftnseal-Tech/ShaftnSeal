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
class SystemResistenceCurve:
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

        return df['Q'].values, df['H'].values

    def plot_combined_src(self) -> str:
        SG = self.get_specific_gravity()
        static_head = self.get_static_head()

        # Theoretical SRC
        k1 = (self.Hnp - static_head) / (self.Qnp ** 2)
        Qi = np.linspace(0, max(self.Qnp, self.Qact) * 1.5, 100)
        static_line = np.full_like(Qi, static_head)
        src_theoretical = k1 * (Qi ** 2) + static_head

        # Actual SRC
        H_actual = (self.pdp - self.psp) * 10 / SG
        k2 = (H_actual - static_head) / (self.Qact ** 2)
        src_actual = k2 * (Qi ** 2) + static_head

        plt.figure(figsize=(8, 5))
        plt.plot(Qi, src_theoretical, label='Theoretical SRC', color='blue')
        plt.plot(Qi, src_actual, label='Actual SRC', color='red', linestyle='--')
        plt.plot(Qi, static_line, label='Static Head', color='green')

        if self.test_file:
            try:
                Q_exp, H_exp = self.read_test_data()
                if self.pump_philosophy == "1R + 1S":
                    plt.plot(Q_exp, H_exp, label='Experimental Data (1R + 1S)', color='purple')
                elif self.pump_philosophy == "2R + 1S":
                    Q_exp2 = Q_exp * 2
                    plt.plot(Q_exp, H_exp, label='Experimental Data (1R + 1S)', color='purple')
                    plt.plot(Q_exp2, H_exp, label='Experimental Data (2R + 1S)', color='grey')
            except Exception as e:
                print(f"Warning: Could not load experimental data: {e}")

        plt.xlim(left=0)
        plt.ylim(bottom=700)
        plt.axhline(0, color='black', linewidth=0.8)

        plt.xlabel('Flow Rate (Q)')
        plt.ylabel('Total Head (H)')
        plt.title('Theoretical vs Actual System Resistance Curve')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Save plot
        src_plot_path = os.path.join(settings.MEDIA_ROOT, 'system_resistance_curve.png')
        plt.savefig(src_plot_path)
        plt.close()

        return src_plot_path
