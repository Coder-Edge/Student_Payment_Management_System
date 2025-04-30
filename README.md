# Student Payment Management System 🎓 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-%234D4D4D.svg?style=for-the-badge&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-239120?style=for-the-badge&logo=csv&logoColor=white)
![PDF](https://img.shields.io/badge/PDF-FF0000?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)

#### Video Demo:  <URL HERE>
## 📘 Project Description

This is a mini-project built in Python using Tkinter for the GUI. It aims to help manage student payment records for a course or training. The application allows you to:

- Add new students with payment details.
- Check who has paid or not.
- Update payment information.
- Export student lists and individual receipts to PDF.

It's a simple yet practical solution for administrators or small training centers to track and manage student payments efficiently.

---

## 🛠️ Main Features

- **📋 Add New Students** :
Allows the user to input a student’s name, email, and amount paid via a graphical interface. Automatically calculates the student’s debt, determines course access eligibility, and assigns a unique ID. The new entry is saved in students.csv.


- **👀 View Students (Filterable)** :
Displays all student records in a table format. You can filter the view to show:

  - All students

  - Only those with course access (fully paid)

  - Only those without course access (still in debt)


- **💳 Update Student Payments** :
Lets the user input additional payments for a student using their unique ID. The system updates the total amount paid, recalculates debt, discount, and course access rights accordingly, and then saves the new data.


- **📄 Export All Data to PDF**
Generates a structured PDF report (students_report.pdf) listing all students and their data in a landscape table format. Useful for printing or archiving.


- **🧾 Export Individual Payment Receipts** :
Creates a personal PDF receipt for a selected student, summarizing their payment and access information. This can be used as proof of payment.


- **✅ Email Validation & Basic Data Checks** :
Ensures all entered email addresses follow a valid format and that numerical values (payments) are within logical bounds. Users are notified immediately in case of incorrect input.


- **💾 Local CSV Data Storage** :
All student data is saved in students.csv. This ensures persistence between sessions, allowing you to reopen and manage existing data anytime without needing a database.


- **🧮 Debt & Discount Calculation** :
Automatically calculates any remaining debt if the student has underpaid or computes a discount if the payment exceeds the course fee.


- **🔓 Course Access Status** :
Automatically grants "Yes" for course access if the student has fully paid, or "No" if any debt remains.
---

## 🧰 Technologies Used

- **Python 3** : 
The main programming language used throughout the project. It handles the graphical interface, calculation logic, file operations, and PDF exports.


- **Tkinter** – GUI interface :
Python’s standard library for building graphical user interfaces (GUIs). It's used to:

  - Create the app's windows and buttons
  - Display user input dialogs
  - Manage user interaction in a visual format
  

- **FPDF** – For generating PDF reports : 
A Python library for easily generating PDF files. It is used to:

  - Create a full PDF report of all students (students_report.pdf)
  - Generate individual PDF receipts for each student


- **CSV (Comma-Separated Values)** : The data storage format used in this project. All student records (name, email, amount paid, etc.) are saved in the students.csv file, allowing fast and easy management without a database.


- **Regex (Regular Expressions)** :
Used to validate user-entered email addresses. This prevents saving incorrectly formatted emails and improves data quality.

---

## 🗂️ Project structure

```text
student-management-system/
├── project.py           # Main GUI application
├── test_project.py      # Unit tests for main functionalities
├── students.csv         # CSV data file (auto-created)
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```
---

## 📦 Requirements

- Python 3.x  
- Required libraries (install via pip if not available):
  ```bash
  pip install requirements.txt
---
## 📜 License
This project is open-source and free to use under the MIT License.

---

## 👤 Author
### Nathan LUKAMBA
#### 📧 Email: nathanlukamba82@gmail.com