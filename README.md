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
## 📊 Process Flow Diagram

## 📊 Process Flow Diagram

<div align="center">
<svg width="900" height="600" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="600" fill="#ffffff"/>
  
  <!-- Styles -->
  <style>
    .box { fill: #e0e7ff; stroke: #3730a3; stroke-width: 2; rx: 10; }
    .arrow { stroke: #000; stroke-width: 2; marker-end: url(#arrowhead); }
    .label { font-family: Arial, sans-serif; font-size: 14px; fill: #111827; }
  </style>
  
  <!-- Arrowhead Definition -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#000"/>
    </marker>
  </defs>
  
  <!-- Boxes -->
  <rect x="50" y="30" width="300" height="50" class="box"/>
  <rect x="50" y="120" width="300" height="50" class="box"/>
  <rect x="50" y="210" width="300" height="50" class="box"/>
  <rect x="50" y="300" width="300" height="50" class="box"/>
  <rect x="400" y="300" width="200" height="50" class="box"/>
  <rect x="400" y="380" width="200" height="50" class="box"/>
  <rect x="50" y="470" width="300" height="50" class="box"/>
  
  <!-- Labels -->
  <text x="200" y="60" text-anchor="middle" class="label">Generate Job Postings PDFs</text>
  <text x="200" y="150" text-anchor="middle" class="label">Generate Candidate CV PDFs</text>
  <text x="200" y="240" text-anchor="middle" class="label">Store & Version Control (GitHub)</text>
  <text x="200" y="330" text-anchor="middle" class="label">Parsing Scripts (Colab)</text>
  <text x="500" y="330" text-anchor="middle" class="label">Raw Text Files</text>
  <text x="500" y="410" text-anchor="middle" class="label">Structured CSV Files</text>
  <text x="200" y="500" text-anchor="middle" class="label">Power BI Dashboards</text>
  
  <!-- Arrows -->
  <line x1="200" y1="80" x2="200" y2="120" class="arrow"/>
  <line x1="200" y1="170" x2="200" y2="210" class="arrow"/>
  <line x1="200" y1="260" x2="200" y2="300" class="arrow"/>
  <line x1="200" y1="350" x2="400" y2="350" class="arrow"/>
  <line x1="500" y1="350" x2="500" y2="380" class="arrow"/>
  <line x1="200" y1="350" x2="200" y2="470" class="arrow"/>
</svg>
</div>



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
