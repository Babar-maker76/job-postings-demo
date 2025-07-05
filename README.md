# 📂 job-postings-demo

## 🎯 Professional HR Automation Demo

This repository showcases an end-to-end workflow for publishing, parsing, and managing job postings and candidate applications in a modern HR system.

---

## 📘 Project Overview

This project demonstrates how to:

✅ Generate **51 professional job posting PDFs**, of which **12 are included as a demonstration dataset** in Power BI.

✅ Store and version control all job postings in a transparent, accessible repository.

✅ Generate realistic candidate CV PDFs linked to each job.

✅ Automate parsing of structured data from PDFs using Google Colab and Python.

✅ Prepare cleaned data outputs (CSV, Excel, Google Sheets) ready for analysis in Power BI or other reporting tools.

✅ Manually record interview panel scores in an Excel file for integration into dashboards.

✅ Visualize and analyze recruitment KPIs through interactive Power BI dashboards.

---

## 📁 Repository Contents

| Folder/File                       | Description                                                   |
|-----------------------------------|---------------------------------------------------------------|
| `/job-postings`                   | 51 individual job posting PDFs (professionally formatted; 12 used for Power BI demo) |
| `/candidate-cvs`                  | 300 candidate CV PDFs linked to job IDs                      |
| `Interview_Panel_Input.xlsx`      | Excel sheet to manually enter interview scores               |
| `colab-parsing-notebook.ipynb`    | Google Colab script for parsing PDFs into structured data    |
| `/sample-output`                  | Example parsed CSV files                                     |
| `/screenshots`                    | Dashboard screenshots                                        |
| `README.md`                       | Project documentation                                        |

---

## 🛠️ Technologies Used

- **Python** (`PyPDF2`, `pandas`) for PDF parsing
- **Google Colab** for free cloud-based workflows
- **GitHub** for file hosting and version control
- **Power BI** for data visualization (demo-ready)
- **Dropbox / Google Drive** for storage and distribution

---

## 📝 How to Use This Repository

1️⃣ **Download Job Postings PDFs**
- Navigate to the `/job-postings` folder.
- Download any individual PDF or the entire folder.

2️⃣ **Download Candidate CVs**
- Navigate to `/candidate-cvs`.
- Download individual files or all files as a ZIP.

3️⃣ **Run the Colab Notebook**
- Open `colab-parsing-notebook.ipynb` in [Google Colab](https://colab.research.google.com/).
- Follow these steps to parse your data:

---

### 🛠️ Running the Colab Notebook – Detailed Steps

**Step 1: Install Dependencies**
```python
!pip install PyPDF2 pandas
