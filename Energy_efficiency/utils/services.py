import pandas as pd

import numpy as np

from django.conf import settings
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for saving plots
import matplotlib.pyplot as plt
import os

class PumpEfficiency:
    def __init__(self):
        self.specific_gravity = None
        self.static_head = None
        self.dynamic_head1 = None
        self.dynamic_head2 = None
        self.k1 = None
        self.k2 = None
        self.src = None
        self.srcact = None
        self.Hnp = None
        self.Hact = None
        self.Qnp = None
        self.Qact = None
        self.temp = None
        self.pump_philosophy = None
        self.df = None  # Placeholder for the DataFrame

    def get_specific_gravity(self, temp):
        self.temp = temp
        try:
            file_path = os.path.join(settings.BASE_DIR, 'Energy_efficiency', 'utils', 'specific_gravity.csv')
            csv = pd.read_csv(file_path)
            csv = csv[csv['Temperature'] == self.temp]
            if csv.empty:
                print("Temperature not found in the dataset.")
                return None
            else:
                self.specific_gravity = csv['Specific_Gravity'].values[0]
                return self.specific_gravity
        except FileNotFoundError:
            print("CSV file not found. Please check the file path.")
            return None

    def set_dataframe(self, df):
        self.df = df  # Set the DataFrame outside of the methods

    def calculate_static_head(self, h1, h2, p1, p2):
        self.h1 = h1
        self.h2 = h2
        self.p1 = p1
        self.p2 = p2

        if self.get_specific_gravity(self.temp) is None:
            return "Temperature not found in the dataset."

        self.static_head = (h2 - h1) + (((p2 - p1) * 10) / self.specific_gravity)
        print(f"Calculated Static Head: {self.static_head:.2f}")
        return self.static_head

    def calculate_theoretical_src(self, pump_philosophy, Qnp, Hnp,excel_file):
        self.pump_philosophy = pump_philosophy
        self.df = pd.read_excel(excel_file)
        columns = self.df.columns
        self.Q1 = self.df[columns[0]]
        self.Q2 = self.df[columns[0]] * 2
        self.H = self.df[columns[1]]

        self.Qnp = float(Qnp)
        self.Hnp = float(Hnp)
        

        self.dynamic_head1 = self.Hnp - self.static_head
        self.k1 = self.dynamic_head1 / (self.Qnp ** 2)
        return self.k1 

    def calculate_actual_src(self, total_Qact, Pdp, Psp):
        static_line = np.full_like(self.Q1, self.static_head)

        self.total_Qact = float(total_Qact)
        self.Qact = self.total_Qact / 24

        self.Psp = float(Psp)
        self.Pdp = float(Pdp)
        self.Hact = ((self.Pdp - self.Psp) * 10) / self.specific_gravity
        self.dynamic_head2 = self.Hact - self.static_head
        self.k2 = self.dynamic_head2 / (self.Qact ** 2)
        self.srcact = self.static_head + self.k2 * (self.Q1 ** 2)

        plt.plot(self.Q1, self.srcact, label='Actual SRC')
        plt.plot(self.Q1, static_line, label='Static Head')
        plt.axhline(y=self.Hact, color='r', linestyle='-', label='Hact ')
        plt.axvline(x=self.Qact, color='b', linestyle='--', label='Qact (avg hourly flow)')

        plt.xlabel('Flow rate (Q)')
        plt.ylabel('Head (H)')
        plt.title('Actual System Resistance Curve')
        plt.legend()
        plt.grid(True)
        plt.show()




    def display_src(self):
        h_line = np.full_like(self.Q1, self.Hnp)
        static_line = np.full_like(self.Q2 if self.pump_philosophy == '2R + 1s' else self.Q1, self.static_head)

        if self.pump_philosophy == '2R + 1s':
            self.src = self.static_head + self.k1 * (self.Q2 ** 2)
            plt.plot(self.Q1, self.H, label='Hnp')
            plt.plot(self.Q2, self.H, label='2Hnp (Flat)')
            plt.plot(self.Q2, static_line, label='Static Head')
            plt.plot(self.Q2, self.src, label='Theoretical SRC')
        else:
            self.src = self.static_head + self.k1 * (self.Q2 ** 2)
            plt.plot(self.Q1, self.H, label='Hnp')
            plt.plot(self.Q1, static_line, label='Static Head')
            plt.plot(self.Q1, self.src, label='Theoretical SRC')

        plt.xlabel('Flow rate (Q)')
        plt.ylabel('Head (H)')
        plt.title('Theoretical SRC Curve')
        plt.legend()
        plt.grid(True)

        # Save the plot to a PDF file
        plot_filename = 'src_plot_2r1s.pdf' if self.pump_philosophy == '2R + 1s' else 'src_plot_standard.pdf'
        plot_path = os.path.join(settings.MEDIA_ROOT, plot_filename)
        print("Plot saved at:", plot_path)  # Confirm the saved path
        plt.savefig(plot_path, format='pdf')
        plt.close()  # Close the plot to free up memory

        # Return the file path to the template for rendering
        return plot_path