import csv
import random
import string
import re
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from fpdf import FPDF

FILENAME = "students.csv"
FIELDS = ["ID", "Name", "Email", "Amount_Paid", "Debt", "Course_Access", "Discount"]
MAX_FEE = 300.0


def generate_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


def initialize_file():
    try:
        with open(FILENAME, mode="x", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
    except FileExistsError:
        pass


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None


def add_student_gui():
    name = simpledialog.askstring("Input", "Student's name:")
    if not name:
        return

    email = simpledialog.askstring("Input", "Student's email:")
    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email.")
        return

    try:
        amount_paid = float(simpledialog.askstring("Input", f"Amount paid (max {MAX_FEE}€):"))
    except:
        messagebox.showerror("Invalid Amount", "Please enter a valid number.")
        return

    if amount_paid < 0:
        messagebox.showerror("Invalid Amount", "Amount cannot be negative.")
        return

    debt = max(0, MAX_FEE - amount_paid)
    access = "Yes" if debt == 0 else "No"
    discount = max(0, amount_paid - MAX_FEE)
    student_id = generate_id()

    with open(FILENAME, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            "ID": student_id,
            "Name": name,
            "Email": email,
            "Amount_Paid": amount_paid,
            "Debt": debt,
            "Course_Access": access,
            "Discount": discount
        })

    messagebox.showinfo("Success", f"Student added with ID: {student_id}")


def show_students_gui(filter_access=None):
    window = tk.Toplevel()
    window.title("Student List")

    tree = ttk.Treeview(window, columns=FIELDS, show="headings")
    for field in FIELDS:
        tree.heading(field, text=field)
        tree.column(field, width=100)

    with open(FILENAME, mode="r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if filter_access is None or row["Course_Access"] == filter_access:
                tree.insert("", "end", values=[row[field] for field in FIELDS])

    tree.pack(fill="both", expand=True)


def update_payment_gui():
    student_id = simpledialog.askstring("Input", "Enter student ID:")
    if student_id is None:
        return  # User cancelled
    student_id = student_id.upper()

    updated_data = []
    found = False

    with open(FILENAME, mode="r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["ID"] == student_id:
                try:
                    extra = float(simpledialog.askstring("Input", "Extra payment (€):"))
                    if extra < 0:
                        messagebox.showerror("Error", "Payment must be positive.")
                        return

                    total = float(row["Amount_Paid"]) + extra
                    debt = max(0, MAX_FEE - total)
                    access = "Yes" if debt == 0 else "No"
                    discount = max(0, total - MAX_FEE)

                    row["Amount_Paid"] = str(total)
                    row["Debt"] = str(debt)
                    row["Course_Access"] = access
                    row["Discount"] = str(discount)
                    found = True
                except:
                    messagebox.showerror("Error", "Invalid payment.")
                    return
            updated_data.append(row)

    if found:
        with open(FILENAME, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(updated_data)
        messagebox.showinfo("Success", "Payment updated.")
    else:
        messagebox.showerror("Error", "Student not found.")


def export_to_pdf():
    try:
        pdf = FPDF(orientation="L")  # "L" pour Landscape (paysage)
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        with open(FILENAME, mode="r", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "Students Report", ln=True, align="C")
            pdf.ln(10)

            pdf.set_font("Arial", size=12)

            # Header
            for field in FIELDS:
                pdf.cell(40, 10, field, border=1)
            pdf.ln()

            # Data rows
            for row in reader:
                for field in FIELDS:
                    pdf.cell(40, 10, str(row[field]), border=1)
                pdf.ln()

        pdf.output("students_report.pdf")
        messagebox.showinfo("Success", "PDF exported successfully as students_report.pdf")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export PDF: {str(e)}")


def export_receipt_pdf():
    student_id = simpledialog.askstring("Input", "Enter student ID for receipt:").upper().strip()

    try:
        with open(FILENAME, mode="r", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            student = next((row for row in reader if row["ID"] == student_id), None)

        if student is None:
            messagebox.showerror("Error", "Student not found.")
            return

        pdf = FPDF(orientation="L")
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        # Titre du reçu
        pdf.cell(0, 10, "Payment Receipt", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", size=12)

        # Création du tableau : 2 colonnes (Label | Value)
        col_width_label = 50
        col_width_value = 120
        row_height = 10

        for field in FIELDS:
            pdf.cell(col_width_label, row_height, f"{field}:", border=1)
            pdf.cell(col_width_value, row_height, str(student[field]), border=1)
            pdf.ln(row_height)

        filename = f"receipt_{student_id}.pdf"
        pdf.output(filename)
        messagebox.showinfo("Success", f"Receipt exported successfully as {filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to export receipt: {str(e)}")


def main():
    initialize_file()

    root = tk.Tk()
    root.geometry("520x300")
    root.title("Student Management System")

    btn1 = tk.Button(root, text="Add Student", command=add_student_gui)
    btn2 = tk.Button(root, text="Show All Students", command=lambda: show_students_gui())
    btn3 = tk.Button(root, text="Show Students WITH Access", command=lambda: show_students_gui("Yes"))
    btn4 = tk.Button(root, text="Show Students WITHOUT Access", command=lambda: show_students_gui("No"))
    btn5 = tk.Button(root, text="Update Payment", command=update_payment_gui)
    btn6 = tk.Button(root, text="Export to PDF", command=export_to_pdf)  # <= NOUVEAU
    btn7 = tk.Button(root, text="Export Receipt (PDF)", command=export_receipt_pdf)
    btn8 = tk.Button(root, text="Quit", command=root.quit)

    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8]:
        btn.pack(padx=10, pady=5, fill='x')

    root.mainloop()


if __name__ == "__main__":
    main()
