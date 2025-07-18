
# 📂 InsightForge | HR Recruitment Automation Demo

_Automated, scalable, and professional recruitment analytics from job posting to candidate selection._

---

## 📑 Table of Contents
- [🎯 Project Overview](#-project-overview)
- [📊 Process Flow Diagram](#-process-flow-diagram)
- [📁 Repository Contents](#-repository-contents)
- [🛠️ Technologies Used](#-technologies-used)
- [📝 How to Use This Repository](#-how-to-use-this-repository)
- [🏃‍♂️ Running the Colab Notebook](#-running-the-colab-notebook--detailed-steps)
- [📊 Example Outputs](#-example-outputs)
- [📫 Contact](#-contact)

---

## 🎯 Project Overview

This project demonstrates how to automate and visualize the full recruitment pipeline using Power BI, Python, and Google Sheets.

**Key Features:**
- ✅ Generate polished job posting PDFs  
- ✅ Auto-generate candidate CVs with structured mock data  
- ✅ Parse job and candidate data using Google Colab + Python  
- ✅ Store all data with GitHub version control  
- ✅ Sync interview scores via Google Sheets  
- ✅ Build live dashboards in Power BI (fully interactive)

---

## 📊 Process Flow Diagram

![Process Flow](./sample-output/Process_Flow_Diagram.png)

This diagram outlines the complete recruitment automation workflow, from job publishing to final selection, integrating Power BI, Google Sheets, Colab, and GitHub.

---

## 📁 Repository Contents

| Folder/File | Description |
|-------------|-------------|
| `/job-postings` | 50+ job posting PDFs |
| `/CandidatesCVs` | 300+ candidate CVs mapped by Job ID |
| `/parsed-candidate-texts` | Raw extracted text from CVs |
| `/sample-output` | Parsed structured CSV files |
| `colab-parsing-notebook.ipynb` | Colab script to parse PDFs to CSV |
| `Interview_Panel_Input.xlsx` | Interview panel score entry sheet |
| `README.md` | This documentation |

---

## 🛠️ Technologies Used

- **Python (PyPDF2, pandas)** – PDF parsing  
- **Google Colab** – Free cloud environment  
- **GitHub** – File storage & version control  
- **Power BI** – Data visualization and automation  
- **Google Sheets** – Manual interview input + sync  
- **Dropbox/Google Drive** – Structured file storage  

---

## 📝 How to Use This Repository

### 📂 1️⃣ Download Job Postings  
Navigate to `/job-postings`, download individual job PDFs or the complete set.

### 📂 2️⃣ Download Candidate CVs  
Navigate to `/CandidatesCVs`, download CVs for parsing or audit.

### 📄 3️⃣ Edit Interview Scores  
Open `Interview_Panel_Input.xlsx` in Excel or Google Sheets to enter scores.

### ⚙️ 4️⃣ Run Parsing Notebook  
Open `colab-parsing-notebook.ipynb` in Google Colab and follow the notebook instructions:
- Parse PDFs
- Export structured CSV
- Connect to Power BI

---

## 🏃‍♂️ Running the Colab Notebook – Detailed Steps

**✅ Step 1: Install Dependencies**
```python
!pip install PyPDF2 pandas
```

**✅ Step 2: Mount Google Drive**
```python
from google.colab import drive
drive.mount('/content/drive')
```

**✅ Step 3: Parse PDFs**
Loop through the folder, extract text, and structure it into rows.

**✅ Step 4: Export CSV**
```python
df.to_csv("parsed_candidates_data.csv", index=False)
```

**✅ Step 5: Connect to Power BI**
Use Power BI’s Web connector or sync the file via GitHub for automated refresh.

---

## 📊 Example Outputs

- `job_descriptions_structured.csv`
- `parsed_candidates_data.csv`

These are cleaned and formatted to feed directly into Power BI dashboards for real-time tracking and insights.

---

## 📫 Contact

For queries, collaboration, or integration support:

**InsightForge – Babar Hayat**  
📧 Email: sominiazi78@gmail.com  
🔗 GitHub: [job-postings-demo](https://github.com/Babar-maker76/job-postings-demo)  
🌐 LinkedIn:(https://www.linkedin.com/in/babar-hayat-50582216a/)
## 💼 Hire Me on Upwork

You can now order this project as a service on Upwork:

🔗 [🔗 Order Now – InsightForge on Upwork](https://www.upwork.com/freelancers/~01f033a1a1aa53fe28?p=1945733170006990848)


---

