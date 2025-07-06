# 📂 job-postings-demo

# 🎯 Professional HR Automation Demo

This repository showcases an end-to-end workflow for publishing, parsing, and managing job postings and candidate applications in a modern HR system.

---

## 🎯 Project Overview

This project demonstrates how to:

✅ Generate professional job posting PDFs ready for public distribution.

✅ Store and version control all job postings in a transparent, accessible repository.

✅ Generate realistic candidate CV PDFs linked to each job.

✅ Automate parsing of structured data from PDFs using Google Colab and Python.

✅ Prepare cleaned data outputs (CSV, Excel, Google Sheets) ready for analysis in Power BI or other reporting tools.

✅ Capture and record interview scores in an Excel file (`Interview_Panel_Input.xlsx`).

---
![Process Flow](./WorkFlow.svg)
## 📁 Repository Contents

| Folder/File | Description |
|-------------|-------------|
| `/job-postings` | 51 individual job posting PDFs (12 used in the demo) |
| `/candidate-cvs` | 300 candidate CV PDFs linked to Job IDs |
| `/parsed-candidate-texts` | Parsed raw text files of candidate CVs |
| `/sample-output` | Example parsed CSV files |
| `colab-parsing-notebook.ipynb` | Example Google Colab script for parsing PDFs into structured data |
| `Interview_Panel_Input.xlsx` | Excel file to manually enter interview scores |
| `README.md` | Project documentation |

---

## 🛠️ Technologies Used

**Python** (`PyPDF2`, `pandas`) for PDF parsing

**Google Colab** for free cloud-based workflows

**GitHub** for file hosting and version control

**Power BI** for data visualization (demo-ready)

**Dropbox / Google Drive** for storage and distribution

---

## 📝 How to Use This Repository

📂 **1️⃣ Download Job Postings PDFs**

- Navigate to the `/job-postings` folder.
- Download any individual PDF or the entire folder.

📂 **2️⃣ Download Candidate CVs**

- Navigate to `/candidate-cvs`.
- Download individual files or all files as a ZIP.

📂 **3️⃣ Download Parsed Candidate Text Files**

- Navigate to `/parsed-candidate-texts`.
- Review or use the raw extracted text data.

📄 **4️⃣ Download or Edit the Interview Scores**

- Open `Interview_Panel_Input.xlsx`.
- Enter interview panel scores and save.

⚙️ **5️⃣ Run the Colab Notebook**

- Open `colab-parsing-notebook.ipynb` in [Google Colab](https://colab.research.google.com/).
- Follow the instructions to:
  - Parse PDFs
  - Export data
  - Connect to Power BI

---

## 🏃‍♂️ Running the Colab Notebook – Detailed Steps

### ✅ Step 1: Install Dependencies

```python
!pip install PyPDF2 pandas
```

### ✅ Step 2: Mount Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
```

### ✅ Step 3: Load and Parse PDFs

Follow the code in the notebook to:

- Loop through the PDFs
- Extract text using `PyPDF2`
- Clean and structure the output

### ✅ Step 4: Export CSV

```python
df.to_csv("parsed_candidates_data.csv", index=False)
```

### ✅ Step 5: Download or Move Outputs

Download to your local machine or push to Google Sheets.

---

## 📊 Example Outputs

Example cleaned data:

- `job_postings.csv`
- `candidates.csv`

These files are structured for real-time dashboards in Power BI.

---

## 📫 Contact

**Acme HR Solutions (Demo Project)**  
💼 Email: sominiazi78@gmail.com

---

✅ **Full documentation and project files:**  
[https://github.com/Babar-maker76/job-postings-demo](https://github.com/Babar-maker76/job-postings-demo)
