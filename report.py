from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def generate_pdf(candidate, role, score, recommendation, feedbacks):

    filename = f"{candidate}_Interview_Report.pdf"

    pdf = SimpleDocTemplate(filename)

    elements = []

    elements.append(Paragraph("<b>HireAI Interview Report</b>", styles["Title"]))

    elements.append(Paragraph(f"<b>Candidate:</b> {candidate}", styles["BodyText"]))

    elements.append(Paragraph(f"<b>Role:</b> {role}", styles["BodyText"]))

    elements.append(Paragraph(f"<b>Overall Score:</b> {score}/10", styles["BodyText"]))

    elements.append(Paragraph(f"<b>Recommendation:</b> {recommendation}", styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Detailed Feedback</b>", styles["Heading2"]))

    for feedback in feedbacks:

        elements.append(Paragraph(feedback.replace("\n","<br/>"), styles["BodyText"]))

    pdf.build(elements)

    return filename