import pandas as pd
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from datetime import datetime

# Load your CSV
df = pd.read_csv("job_openings.csv")

for index, row in df.iterrows():
    filename = f"{row['JobID']}_{row['JobTitle'].replace(' ', '_')}.pdf"
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"{row['JobTitle']}")

    # Subheading
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Department: {row['Department']} | Location: {row['Location']} | {row['JobType']}")
    c.drawString(50, height - 100, f"Salary Range: {row['SalaryRange']}")

    # About Role
    y = height - 140
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "About the Role:")
    c.setFont("Helvetica", 12)
    text_obj = c.beginText(50, y - 20)
    for line in row['AboutRole'].split('. '):
        text_obj.textLine(line.strip())
    c.drawText(text_obj)

    # Responsibilities
    y = y - 80
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Key Responsibilities:")
    c.setFont("Helvetica", 12)
    text_obj = c.beginText(50, y - 20)
    for item in row['Responsibilities'].split(';'):
        text_obj.textLine(f"- {item.strip()}")
    c.drawText(text_obj)

    # Skills
    y = y - 80
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Required Skills:")
    c.setFont("Helvetica", 12)
    text_obj = c.beginText(50, y - 20)
    for skill in row['Skills'].split(';'):
        text_obj.textLine(f"- {skill.strip()}")
    c.drawText(text_obj)

    # Education & Experience
    y = y - 80
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Education & Qualifications:")
    c.setFont("Helvetica", 12)
    text_obj = c.beginText(50, y - 20)
    for qual in row['EducationQualifications'].split(';'):
        text_obj.textLine(f"- {qual.strip()}")
    c.drawText(text_obj)

    y = y - 80
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Experience:")
    c.setFont("Helvetica", 12)
    c.drawString(50, y - 20, row['Experience'])

    # Application Instructions
    y = y - 60
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "How to Apply:")
    c.setFont("Helvetica", 12)
    c.drawString(50, y - 20, row['ApplicationInstructions'])

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(50, 30, f"Generated on {datetime.today().strftime('%Y-%m-%d')}")

    # Save PDF
    c.save()

print("✅ All job posting PDFs have been generated successfully.")
