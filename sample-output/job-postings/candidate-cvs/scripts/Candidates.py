"""
generate_parse_hr_data.py

This script generates synthetic candidate CV PDFs and job description PDFs,
then parses them into structured CSV files. Designed as part of the HR data
analytics project for demonstration and portfolio purposes.
"""




import os
import random
from fpdf import FPDF

# Create output folder
output_folder = "Candidate_CVs"
os.makedirs(output_folder, exist_ok=True)

# Example lists of data
first_names = ["Ali", "Sara", "Omar", "Zara", "Bilal", "Nadia", "Hassan", "Mina", "Faisal", "Ayesha"]
last_names = ["Khan", "Ahmed", "Sheikh", "Hussain", "Chaudhry", "Raza", "Iqbal", "Jamil", "Mirza", "Farooq"]
skills_list = ["Power BI", "SQL", "Excel", "Python", "Data Analysis", "Project Management", "HR Policies", "Cloud Computing", "UX Design", "Digital Marketing"]
degrees = ["Bachelor's in Computer Science", "Bachelor's in Business Administration", "Master's in HR Management", "MBA", "Bachelor's in Finance"]
experience_range = ["1 year", "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "8 years"]

# Example job titles for linking
job_titles = [
    "Senior Data Analyst", "Human Resources Manager", "Finance Officer", "IT Support Specialist",
    "Marketing Coordinator", "Senior Software Engineer", "Project Manager", "Customer Support Lead",
    "Procurement Specialist", "QA Engineer", "Content Writer", "Operations Manager"
]

# Generate 300 CVs
for i in range(1, 301):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    
    # Candidate Name
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    
    # Mock contact info
    email = f"{first.lower()}.{last.lower()}@example.com"
    phone = f"+92-3{random.randint(0,9)}-{random.randint(1000000,9999999)}"
    
    # Linked Job
    job = random.choice(job_titles)
    
    # Text
    pdf.cell(0, 10, f"Candidate CV - {name}", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.cell(0, 10, f"Applied Position: {job}", ln=True)
    pdf.ln(5)
    
    pdf.multi_cell(0, 10, f"""
Professional Summary:
Highly motivated professional with {random.choice(experience_range)} of experience in {job}. Skilled in {', '.join(random.sample(skills_list, 3))}.
""")
    
    pdf.multi_cell(0, 10, f"""
Education:
{random.choice(degrees)}
""")
    
    pdf.multi_cell(0, 10, f"""
Skills:
- {random.choice(skills_list)}
- {random.choice(skills_list)}
- {random.choice(skills_list)}
""")
    
    # Save file
    filename = f"Candidate_{i:03d}_{first}_{last}.pdf"
    pdf.output(os.path.join(output_folder, filename))

print("✅ 300 Candidate CVs generated successfully.")
