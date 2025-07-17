**📂 InsightForge | HR Recruitment Automation Demo**

**Automated, scalable, and professional recruitment analytics from job posting to candidate selection.**

📑 Table of Contents
🎯 Project Overview

📊 Process Flow Diagram

📁 Repository Contents

🛠️ Technologies Used

📝 How to Use This Repository

🏃‍♂️ Running the Colab Notebook

📊 Example Outputs

📫 Contact

🎯 Project Overview
This project demonstrates how to automate and visualize the full recruitment pipeline using Power BI, Python, and Google Sheets.

Key Features:

✅ Generate polished job posting PDFs

✅ Auto-generate candidate CVs with structured mock data

✅ Parse job and candidate data using Google Colab + Python

✅ Store all data with GitHub version control

✅ Sync interview scores via Google Sheets

✅ Build live dashboards in Power BI (fully interactive)

📊 Process Flow Diagram

📁 Repository Contents
Folder/File	Description
/job-postings	50+ job posting PDFs
/CandidatesCVs	300+ candidate CVs mapped by Job ID
/parsed-candidate-texts	Raw extracted text from CVs
/sample-output	Parsed structured CSV files
colab-parsing-notebook.ipynb	Colab script to parse PDFs to CSV
Interview_Panel_Input.xlsx	Interview panel score entry sheet
README.md	This documentation

🛠️ Technologies Used
Python (PyPDF2, pandas) – PDF parsing

Google Colab – Free cloud environment

GitHub – File storage & version control

Power BI – Data visualization and automation

Google Sheets – Manual interview input + sync

Dropbox/Google Drive – Structured file storage

📝 How to Use This Repository
📂 1️⃣ Download Job Postings
Go to /job-postings, download individual PDFs or ZIP archive.

📂 2️⃣ Download Candidate CVs
Go to /CandidatesCVs, download CVs for parsing or audit.

📄 3️⃣ Edit Interview Scores
Open Interview_Panel_Input.xlsx in Excel or Sheets, enter panel feedback.

⚙️ 4️⃣ Run Parsing Notebook
Open colab-parsing-notebook.ipynb in Google Colab to:

Parse PDFs

Export structured CSV

Connect to Power BI

🏃‍♂️ Running the Colab Notebook – Detailed Steps
✅ Step 1: Install Dependencies

python
Copy
Edit
!pip install PyPDF2 pandas
✅ Step 2: Mount Google Drive

python
Copy
Edit
from google.colab import drive
drive.mount('/content/drive')
✅ Step 3: Parse PDFs
Loop through files, extract text, structure rows.

✅ Step 4: Export CSV

python
Copy
Edit
df.to_csv("parsed_candidates_data.csv", index=False)
✅ Step 5: Connect to Power BI
Use Web connector or push to GitHub for refresh.

📊 Example Outputs
Structured files:

job_descriptions_structured.csv

parsed_candidates_data.csv

Built for direct use in Power BI dashboards.

📫 Contact
InsightForge (Demo Project)
📧 Email: sominiazi78@gmail.com
🔗 GitHub: github.com/Babar-maker76/job-postings-demo
