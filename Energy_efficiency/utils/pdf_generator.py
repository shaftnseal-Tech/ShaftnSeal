import os
from matplotlib.backends.backend_pdf import PdfPages
from Energy_efficiency.utils.energy_efficiency_curves import PumpSystemCurve

from django.conf import settings
import matplotlib.pyplot as plt
from datetime import datetime


def generate_efficiency_report_pdf(
    N1, N2, Qnp, Hnp, test_file,
    h1, h2, p1, p2, Qact, temp, psp, pdp,
    pump_philosophy
):
    """
    Generates a PDF report using combined system resistance and pump curve.
    """

    # Create PumpSystemCurve instance
    pump_curve_plotter = PumpSystemCurve(
        h1=h1, h2=h2, p1=p1, p2=p2,
        Qnp=Qnp, Hnp=Hnp,
        Qact=Qact, temp=temp,
        psp=psp, pdp=pdp,
        N1=N1, N2=N2,
        test_file=test_file,
        pump_philosophy=pump_philosophy
    )

    # Generate plot and get path
    pump_curve_img_path = pump_curve_plotter.plot_pumpsystem_graph()

    # Create unique PDF filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_filename = f"pump_efficiency_report_{timestamp}.pdf"
    pdf_output_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)

    # Generate the PDF
    with PdfPages(pdf_output_path) as pdf:

        # --- Page 1: Summary Information ---
        fig_summary, ax_summary = plt.subplots(figsize=(8.27, 11.69))  # A4 size in inches
        ax_summary.axis('off')

        # You can format this summary text as needed
        summary_text = f"""
        
        Pump Efficiency Report
        ----------------------
        Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        • Nameplate Flow (Qnp): {Qnp} m³/h
        • Nameplate Head (Hnp): {Hnp} m
        • Actual Flow (Qact): {Qact} m³/h
        • Suction Pressure (psp): {psp} kg/cm²
        • Delivery Pressure (pdp): {pdp} kg/cm²
        • Static Suction Head (h1): {h1} m
        • Static Delivery Head (h2): {h2} m
        • Suction Drum Height (p1): {p1} m
        • Delivery Drum Height (p2): {p2} m
        • Temperature: {temp} °C
        • Speed 1 (N1): {N1} rpm
        • Speed 2 (N2): {N2} rpm
        • Pump Philosophy: {pump_philosophy}
        """

        ax_summary.text(0.05, 0.95, summary_text, va='top', fontsize=10, family='monospace')
        pdf.savefig(fig_summary)
        plt.close(fig_summary)

        # --- Page 2: Plot Image ---
        fig_plot = plt.figure(figsize=(8.27, 11.69))
        img = plt.imread(pump_curve_img_path)
        plt.imshow(img)
        plt.axis('off')
        pdf.savefig(fig_plot)
        plt.close(fig_plot)

    return pdf_output_path
