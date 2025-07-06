import os
import re
import csv
from PyPDF2 import PdfReader

# Define input folder where your CV PDFs are stored
input_folder = "Candidate_CVs"

# Define the output CSV file path
csv_file_path = os.path.join(input_folder, "parsed_candidates_data.csv")

# Write CSV header
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "FileName",
        "FullName",
        "Email",
        "Phone",
        "DateOfBirth",
        "AppliedPosition",
        "YearsOfExperience",
        "Education",
        "Skill1",
        "Skill2",
        "Skill3",
        "Skill4",
        "Skill5"
    ])

# Get all PDF files in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

# Process each PDF file
for pdf_file in pdf_files:
    pdf_path = os.path.join(input_folder, pdf_file)
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    # Extract fields using regular expressions
    name_match = re.search(r"Candidate CV - (.+)", text)
    email_match = re.search(r"Email:\s*(.+)", text)
    phone_match = re.search(r"Phone:\s*(.+)", text)
    dob_match = re.search(r"Date of Birth:\s*(.+)", text)
    position_match = re.search(r"Applied Position:\s*(.+)", text)
    experience_match = re.search(r"Years of Experience:\s*(.+)", text)
    education_match = re.search(r"Education:\s*(.+)", text)
    skills_block_match = re.search(r"Core Skills and Competencies:(.+?)Professional Experience:", text, re.S)

    # Clean extracted values
    name = name_match.group(1).strip() if name_match else ""
    email = email_match.group(1).strip() if email_match else ""
    phone = phone_match.group(1).strip() if phone_match else ""
    dob = dob_match.group(1).strip() if dob_match else ""
    position = position_match.group(1).strip() if position_match else ""
    experience = experience_match.group(1).strip() if experience_match else ""
    education = education_match.group(1).strip() if education_match else ""

    # Extract up to 5 skills
    skills = ["", "", "", "", ""]
    if skills_block_match:
        skills_lines = skills_block_match.group(1).strip().split("\n")
        skill_entries = [line.strip("-").strip() for line in skills_lines if line.strip()]
        for idx, skill in enumerate(skill_entries):
            if idx < 5:
                skills[idx] = skill

    # Append the extracted data to CSV
    with open(csv_file_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            pdf_file,
            name,
            email,
            phone,
            dob,
            position,
            experience,
            education,
            skills[0],
            skills[1],
            skills[2],
            skills[3],
            skills[4]
        ])

print("✅ parsed_candidates_data.csv generated successfully.")
