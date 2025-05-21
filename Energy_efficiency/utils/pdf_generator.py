import os
from matplotlib.backends.backend_pdf import PdfPages
from Energy_efficiency.utils.pump_test_curve import PumpTestCurvePlot  # Adjust import paths accordingly
from Energy_efficiency.utils.system_resistence_curve import SystemResistenceCurve  # Adjust import paths accordingly
from django.conf import settings
import matplotlib.pyplot as plt
from datetime import datetime


def generate_efficiency_report_pdf(
    N1, N2, Qnp, Hnp, test_file,
    h1, h2, p1, p2, Qact, temp, psp, pdp,
     pump_philosophy
):
    """
    Generates a PDF report using pump and system resistance curve plots.
    """

    pump_curve_plotter = PumpTestCurvePlot()
    pump_curve_img_path = pump_curve_plotter.text_curve(N1, N2, Qnp, Hnp, test_file)

    resistance_curve = SystemResistenceCurve(
        h1=h1, h2=h2, p1=p1, p2=p2, Qnp=Qnp, Hnp=Hnp,
        Qact=Qact, temp=temp, psp=psp, pdp=pdp,
        test_file=test_file,
        pump_philosophy=pump_philosophy
    )
    resistance_curve_img_path = resistance_curve.plot_combined_src()

    # Create unique PDF filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pdf_filename = f"pump_efficiency_report_{timestamp}.pdf"
    pdf_output_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)

    # Combine both plots into one PDF
    with PdfPages(pdf_output_path) as pdf:
        # Page 1: Pump Test Curve
        fig1 = plt.figure()
        img1 = plt.imread(pump_curve_img_path)
        plt.imshow(img1)
        plt.axis('off')
        pdf.savefig(fig1)
        plt.close(fig1)

        # Page 2: System Resistance Curve
        fig2 = plt.figure()
        img2 = plt.imread(resistance_curve_img_path)
        plt.imshow(img2)
        plt.axis('off')
        pdf.savefig(fig2)
        plt.close(fig2)

    return pdf_output_path
