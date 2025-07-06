import os
import re
import csv
from PyPDF2 import PdfReader

# Folder with your 51 PDFs
input_folder = "/content/drive/My Drive/Job_Descriptions"

# Output CSV for structured data
csv_output = "/content/drive/My Drive/job_descriptions_structured.csv"

# Folder for raw text
raw_output_folder = "/content/drive/My Drive/job_descriptions_raw"
os.makedirs(raw_output_folder, exist_ok=True)

# CSV headers
headers = [
    "FileName",
    "JobID",
    "JobTitle",
    "Department",
    "Location",
    "Status",
    "DatePosted",
    "ApplicationDeadline",
    "Education",
    "Experience",
    "Skills",
    "Summary"
]

with open(csv_output, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".pdf"):
            path = os.path.join(input_folder, filename)
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"

            # Save raw text
            raw_path = os.path.join(raw_output_folder, filename.replace(".pdf", ".txt"))
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(text)

            # Extract fields with regex
            job_id = re.search(r"Job ID:\s*(J\d+)", text)
            title = re.search(r"Job Description - (.+)", text)
            dept = re.search(r"Department:\s*(.+)", text)
            location = re.search(r"Location:\s*(.+)", text)
            status = re.search(r"Status:\s*(.+)", text)
            date_posted = re.search(r"Date Posted:\s*(.+)", text)
            deadline = re.search(r"Application Deadline:\s*(.+)", text)
            education = re.search(r"Required Education:\s*(.+)", text)
            experience = re.search(r"Required Experience:\s*(.+)", text)

            # Extract skills block
            skills_match = re.search(r"Core Skills and Competencies:(.*?)Job Summary:", text, re.DOTALL)
            summary_match = re.search(r"Job Summary:\s*(.+)", text, re.DOTALL)

            skills_text = skills_match.group(1).strip().replace("\n", "; ") if skills_match else ""
            summary_text = summary_match.group(1).strip() if summary_match else ""

            # Clean each field
            row = [
                filename,
                job_id.group(1).strip() if job_id else "",
                title.group(1).strip() if title else "",
                dept.group(1).strip() if dept else "",
                location.group(1).strip() if location else "",
                status.group(1).strip() if status else "",
                date_posted.group(1).strip() if date_posted else "",
                deadline.group(1).strip() if deadline else "",
                education.group(1).strip() if education else "",
                experience.group(1).strip() if experience else "",
                skills_text,
                summary_text
            ]

            writer.writerow(row)

print("✅ Parsing complete: structured CSV and raw text files created.")
