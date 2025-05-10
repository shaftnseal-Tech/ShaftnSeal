import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # For headless environments
import matplotlib.pyplot as plt
import os
from django.conf import settings

class PumpEfficiency:
    def __init__(self):
        pass

    def text_curve(self, N1, N2, Qnp, Hnp, test_file):
      
        fig, ax = plt.subplots(figsize=(12, 6))  

        exl_data = pd.read_excel(test_file)

        Q = exl_data['Q']
        H = exl_data['H']

        
        N1 = float(N1)
        N2 = float(N2)
        Qnp = float(Qnp)
        Hnp = float(Hnp)

        k3 = N2 / N1
        k4 = (N2 ** 2) / (N1 ** 2)
        Qvm = Q * k3
        Hvm = H * k4
        print("Qvm:", Qvm.tolist())
        print("Hvm:", Hvm.tolist())
        ax.set_title('Pump Q-H Test curve & VM operation curve')
        ax.set_xlabel('Flow Rate (Q)')
        ax.set_ylabel('Head (H)')

        ax.plot(Q, H, label='Test Curve (Q,H)', marker='o')
        ax.plot(Qvm, Hvm, label='VM Curve (Qvm,Hvm)', marker='x')
        ax.scatter(Qnp, Hnp, color='red', label='Nameplate Point (Qnp,Hnp)', zorder=5)

      
        y_min = 550
        y_max = max(np.max(H), np.max(Hvm), Hnp) + 100
        ax.set_ylim(y_min, y_max)
        ax.set_yticks(np.arange(y_min, y_max + 1, 100))

      
        x_min = 0
        x_max = max(np.max(Q), np.max(Qvm), Qnp) + 10
        ax.set_xlim(x_min, x_max)
        ax.set_xticks(np.arange(x_min, x_max + 1, 10))

        ax.legend(loc='upper right')
        ax.grid(True)

        # Save the plot
        save_path = os.path.join(settings.MEDIA_ROOT, 'pump_test_curve.png')
        plt.savefig(save_path)
        plt.close()

        return save_path
