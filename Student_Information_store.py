from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import os, sys
import json
import sqlite3


class Face_Recognation_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognation System")

        # ==================== Variables ====================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_sec = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_blood = StringVar()
        self.var_nationality = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        self.selected_from_store = False
        self.search_var = StringVar()

        # ==================== Background Image ====================
        img_bg = Image.open(r"C:\Users\Asus\OneDrive\Desktop\Acadamic\Final Project\Face Recognation\UI Image\background.jpg")
        img_bg = img_bg.resize((1530, 790), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=3, y=0, width=1530, height=790)

        # ==================== Title Label ====================
        title_lbl = Label(
            bg_image,
            text="STUDENT RECORDS",
            font=('Algerian', 60, "bold"),
            bg='white',
            fg='#1E3A8A'
        )
        title_lbl.place(x=-130, y=0, width=1800, height=100)

        # ==================== Student Details Frame ====================
        main_frame = LabelFrame(
            bg_image, bd=10, relief=RIDGE,
            text="Student Directory",
            font=('times new roman', 12, 'bold')
        )
        main_frame.place(x=90, y=130, width=1350, height=650)

        # ==================== Search Frame ====================
        search_frame = LabelFrame(
            bg_image, bd=5, relief=RIDGE,
            text="Search", font=('times new roman', 12, 'bold')
        )
        search_frame.place(x=130, y=170, width=1300, height=70)

        search_label = Label(
            search_frame,
            text='Search :',
            font=('times new roman', 14, 'bold'),
            bg="lightgray",
            fg='black'
        )
        search_label.grid(row=0, column=0, padx=50, pady=5, sticky=W)

        # make search_entry a class variable
        self.search_entry = Entry(
            search_frame, textvariable=self.search_var,
            font=("times new roman", 13, "bold"),
            width=20, fg="gray"
        )
        self.search_entry.grid(row=0, column=1, padx=10, sticky="w")
        self.search_entry.insert(0, "Id")

        def on_entry_click(event):
            if self.search_entry.get() == "Id":
                self.search_entry.delete(0, "end")
                self.search_entry.config(fg="black")

        def on_focusout(event):
            if self.search_entry.get() == "":
                self.search_entry.insert(0, "Id")
                self.search_entry.config(fg="gray")

        self.search_entry.bind("<FocusIn>", on_entry_click)
        self.search_entry.bind("<FocusOut>", on_focusout)

        # ==================== Fixed Search Action ====================
        def search_action():
            user_id = self.search_var.get().strip()

            # validation
            if user_id == "" or user_id.lower() == "id":
                messagebox.showwarning("Warning", "Please enter a valid Student ID!", parent=self.root)
                return

            try:
                conn = sqlite3.connect("face_recognation.db")
                cursor = conn.cursor()

                cursor.execute("""
                    SELECT
                        Student_ID, Student_Name, Department, Course,
                        Year, Semester, Class_Section, Gender, Blood_Group,
                        Nationality, Email, Phone_No, Address, Teacher_Name,
                        Photo_Sample
                    FROM face_recognizer
                    WHERE CAST(Student_ID AS TEXT) LIKE ?
                """, (user_id,))

                rows = cursor.fetchall()

                # clear previous results
                self.student_table.delete(*self.student_table.get_children())

                if len(rows) == 0:
                    messagebox.showinfo("Result", f"No record found for Student ID: {user_id}", parent=self.root)
                else:
                    for row in rows:
                        self.student_table.insert('', END, values=row)

                conn.close()

            except sqlite3.Error as err:
                messagebox.showerror("Database Error", f"Error while searching:\n{err}", parent=self.root)

        search_button = Button(
            search_frame, text="Search",
            font=("times new roman", 12, "bold"),
            bg="#2c3e50", fg="white",
            command=search_action
        )
        search_button.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # ==================== Delete Button ====================
        delete_button = Button(
            search_frame,
            text='Delete',
            width=15,
            font=('times new roman', 13, 'bold'),
            bg="#BF2E24",
            fg='white',
            command=self.confirm_and_delete
        )
        delete_button.grid(row=0, column=3, padx=50, pady=5, sticky=W)

        # ==================== Refresh Button ====================
        Refresh_button = Button(
            search_frame, text='Refresh', width=15,
            font=('times new roman', 13, 'bold'),
            bg='#9E9E9E', fg='white',
            command=self.Refresh_form
        )
        Refresh_button.grid(row=0, column=4, pady=5, padx=50)

        # ==================== Table ====================
        table_frame = LabelFrame(
            bg_image, bd=5, relief=RIDGE,
            font=('times new roman', 12, 'bold')
        )
        table_frame.place(x=130, y=255, width=1300, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("id", "name", "dep", "course", "year", "sem",
                     "section", "gender", "blood", "nationality",
                     "email", "phone", "address", "teacher", "photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            selectmode="browse"
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        headings = ["Student ID", "Student Name", "Department", "Course", "Year", "Semester",
                    "Class Section", "Gender", "Blood Group", "Nationality",
                    "Email", "Phone No", "Address", "Teacher Name", "Photo Sample"]
        for col, text in zip(self.student_table["columns"], headings):
            self.student_table.heading(col, text=text)

        self.student_table["show"] = "headings"

        widths = [100, 120, 100, 100, 80, 100, 100, 80, 80, 100, 150, 100, 150, 120, 100]
        for col, width in zip(self.student_table["columns"], widths):
            self.student_table.column(col, width=width)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<Double-1>", self.open_selected_in_details)

        # Load data initially
        self.fetch_data()

        # ==================== Back Button ====================
        back_btn = Button(
            self.root,
            text="←",
            width=3, height=1, cursor="hand2",
            bg="#373773", fg="white",
            font=("Segoe UI Symbol", 11, "bold"),
            command=self.back_to_details
        )
        back_btn.place(x=10, y=110)

        back_btn.bind("<Enter>", lambda e: back_btn.config(bg="#e74c3c"))
        back_btn.bind("<Leave>", lambda e: back_btn.config(bg="#373773"))

    # ================== Fetch all data ==================
    def fetch_data(self):
        try:
            conn = sqlite3.connect("face_recognation.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM face_recognizer")
            rows = cursor.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.close()
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)

    # ================== Delete function ==================
    def confirm_and_delete(self):
        sel = self.student_table.selection()
        if not sel:
            messagebox.showwarning("No selection", "Please select a row to delete.", parent=self.root)
            return

        item_id = sel[0]
        values = self.student_table.item(item_id, "values")
        student_id = values[0]

        ok = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete Student ID {student_id}?",
            parent=self.root
        )
        if not ok:
            return

        deleted = self.delete_from_db(student_id)
        if deleted:
            self.fetch_data()
            messagebox.showinfo("Deleted", f"Student ID {student_id} deleted successfully.", parent=self.root)
        else:
            messagebox.showerror("Error", f"Failed to delete Student ID {student_id}", parent=self.root)

    def delete_from_db(self, student_id):
        try:
            conn = sqlite3.connect("face_recognation.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM face_recognizer WHERE Student_ID = ?", (student_id,))
            conn.commit()
            rowcount = cur.rowcount
            cur.close()
            conn.close()
            return rowcount > 0
        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            return False

    # ================== Open selected record ==================
    def open_selected_in_details(self, event=None):
        sel = self.student_table.selection()
        if not sel:
            return

        item_id = sel[0]
        values = self.student_table.item(item_id, "values")
        if len(values) < 15:
            messagebox.showerror("Error", "Incomplete data!", parent=self.root)
            return

        student = {
            "id": str(values[0]),
            "name": values[1],
            "dept": values[2],
            "course": values[3],
            "year": str(values[4]),
            "sem": values[5],
            "section": values[6],
            "gender": values[7],
            "blood": values[8],
            "nationality": values[9],
            "email": values[10],
            "phone": str(values[11]),
            "address": values[12],
            "teacher": values[13],
            "photo": values[14],
        }

        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            temp_path = os.path.join(base_dir, "temp.json")
            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump(student, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to write temp.json:\n{e}", parent=self.root)
            return

        try:
            self.root.destroy()
        finally:
            details_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Student_Details.py")
            subprocess.Popen([sys.executable, details_path])

    # ================== Back function ==================
    def back_to_details(self):
        details_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Student_Details.py")
        if not os.path.exists(details_path):
            messagebox.showerror("Path Error", f"Student_Details.py not found:\n{details_path}", parent=self.root)
            return
        self.root.destroy()
        subprocess.Popen([sys.executable, details_path])

    # ================== Refresh ==================
    def Refresh_form(self):
        self.var_dep.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_sec.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_blood.set("")
        self.var_nationality.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.selected_from_store = False

        #  Reset search box & placeholder
        self.search_var.set("")
        self.search_entry.delete(0, "end")
        self.search_entry.insert(0, "Id")
        self.search_entry.config(fg="gray")

        #  Refresh table data
        self.fetch_data()


# ==================== Run Main Application ====================
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognation_System(root)
    root.mainloop()
