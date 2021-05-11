# Martinez, Ryan James J.
# BS STAT II
# CSC151N
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import csv
import os


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Information System")
        self.root.geometry("900x400+0+0")
        self.root.config(bg="gray15")
        self.root.resizable(False, False)
        self.data = dict()
        self.temp = dict()
        self.filename = "StudentInformation.csv"

        Student_Name = StringVar()
        Student_ID = StringVar()
        Student_YearLevel = StringVar()
        Student_Gender = StringVar()
        Student_Course = StringVar()
        SearchBar_Var = StringVar()

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w') as csv_file:
                fieldnames = ["ID Number", "Name", "Course", "Year Level", "Gender"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

        else:
            with open(self.filename, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["ID Number"]] = {'Name': row["Name"], 'Course': row["Course"],
                                                   'Year Level': row["Year Level"], 'Gender': row["Gender"]}
            self.temp = self.data.copy()

        def addData():
            with open(self.filename, "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_ID.get() == "" or Student_Name.get() == "" or Student_Course.get() == "" or Student_YearLevel.get() == "" or Student_Gender.get() == "":
                    tkinter.messagebox.showinfo("Student Information System", "Please Fill In the Box with *")
                else:
                    self.data[Student_ID.get()] = {'Name': Student_Name.get(), 'Course': Student_Course.get(),
                                                   'Year Level': Student_YearLevel.get(),
                                                   'Gender': Student_Gender.get()}
                    self.save_data()
                    tkinter.messagebox.showinfo("Student Information System", "Student Recorded Successfully")
                    clear()
                displayData()

        def displayData():
            self.studentlist.delete(*self.studentlist.get_children())
            with open(self.filename) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    IDNumber = row['ID Number']
                    Name = row['Name']
                    Course = row['Course']
                    YearLevel = row['Year Level']
                    Gender = row['Gender']
                    self.studentlist.insert("", 0, values=(IDNumber, Name, Course, YearLevel, Gender))

        def deleteData():
            x = self.studentlist.focus()
            if x == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a record from the table.")
                return
            id_no = self.studentlist.item(x, "values")[0]
            
            result = tkinter.messagebox.askquestion("Student Information System","Delete Record?")
            if result == "yes":
                self.data.pop(id_no, None)
                self.save_data()
                self.studentlist.delete(x)
                tkinter.messagebox.showinfo("Student Information System", "Student Record Deleted Successfully")
            else:
                pass

        def searchData():
            x = self.SearchBar.get()
            if x in self.data:
                vals = list(self.data[x].values())
                self.studentlist.delete(*self.studentlist.get_children())
                self.studentlist.insert("", 0, values=(x, vals[0], vals[1], vals[2], vals[3]))
            elif x == "":
                tkinter.messagebox.showerror("Student Information System", "Student not found.")
                return
            else:
                tkinter.messagebox.showerror("Student Information System", "Student not found.")
                return
            
        def Refresh():
            displayData()

        def editData():
            x = self.studentlist.focus()
            if x == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a record from the table.")
                return
            values = self.studentlist.item(x, "values")
            Student_ID.set(values[0])
            Student_Name.set(values[1])
            Student_Course.set(values[2])
            Student_YearLevel.set(values[3])
            Student_Gender.set(values[4])

        def clear():
            Student_ID.set("")
            Student_Name.set("")
            Student_Course.set("")
            Student_YearLevel.set("")
            Student_Gender.set("")
            
        def updateData():
            with open(self.filename, "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_ID.get() == "" or Student_Name.get() == "" or Student_Course.get() == "" or Student_YearLevel.get() == "" or Student_Gender.get() == "":
                    tkinter.messagebox.showinfo("Student Information System", "Please Fill In the Box with *")
                else:
                    self.data[Student_ID.get()] = {'Name': Student_Name.get(), 'Course': Student_Course.get(),
                                                   'Year Level': Student_YearLevel.get(),
                                                   'Gender': Student_Gender.get()}
                    self.save_data()
                    tkinter.messagebox.showinfo("Student Information System", "Student Updated Successfully")
                    clear()
                displayData()

        MainFrame = Frame(self.root, bg="Light Gray")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, padx=285, pady=15, bg="gray15", relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame, font=("Poppins", 16), text="STUDENT INFORMATION SYSTEM", bg ="gray15", fg="snow")
        self.lblTitle.grid()

        DataFrame = Frame(MainFrame, width=450, height=200, padx=15, pady=15, bg="RoyalBlue1", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        StudentInfoFrame = LabelFrame(DataFrame, width=400, height=300, padx=16, bg="RoyalBlue1", relief=RIDGE,
                                      font=('Poppins', 15), text="REGISTER:", fg = "snow")
        StudentInfoFrame.pack(side=LEFT)

        StudentDetailsFrame = LabelFrame(DataFrame, width=370, height=300, padx=20, pady=2, bg="RoyalBlue1", fg="snow",
                                         relief=RIDGE, font=('Poppins', 15), text="STUDENT DETAILS:")
        StudentDetailsFrame.pack(side=RIGHT)

        
        self.lblStudentID = Label(StudentInfoFrame, font=("Poppins", 10), text="Student ID:*", padx=5, pady=5,
                                  bg="RoyalBlue1", fg="snow")
        self.lblStudentID.grid(row=0, column=0, sticky=W)
        self.lblStudentIDFormat = Label(StudentInfoFrame, font=("Poppins", 9), text="(YYYY - NNNN)", bg="RoyalBlue1", fg="snow")
        self.lblStudentIDFormat.grid(row=1, column=1, sticky=W)
        self.txtStudentID = Entry(StudentInfoFrame, font=("Poppins", 10), textvariable=Student_ID, width=30)
        self.txtStudentID.grid(row=0, column=1)

        self.lblStudentName = Label(StudentInfoFrame, font=("Poppins", 10), text="Full Name:*", padx=5, pady=5,
                                    bg="RoyalBlue1", fg="snow")
        self.lblStudentName.grid(row=2, column=0, sticky=W)
        self.txtStudentName = Entry(StudentInfoFrame, font=("Poppins", 10), textvariable=Student_Name, width=30)
        self.txtStudentName.grid(row=2, column=1)
        self.lblStudentNameFormat = Label(StudentInfoFrame, font=("Poppins", 9),
                                          text="(Surname, Firstname Middle Initial)",bg="RoyalBlue1", fg="snow")
        self.lblStudentNameFormat.grid(row=3, column=1, sticky=W)

        self.lblStudentYearLevel = Label(StudentInfoFrame, font=("Poppins", 10), text="Year Level:*", padx=5, pady=5,
                                        bg="RoyalBlue1", fg="snow")
        self.lblStudentYearLevel.grid(row=4, column=0, sticky=W)
        self.txtStudentYearLevel = ttk.Combobox(StudentInfoFrame,
                                                value=["1st Year", "2nd Year", "3rd Year", "4th Year", "5th Year"],
                                                state="readonly", font=("Poppins", 10), textvariable=Student_YearLevel,
                                                width=27)
        self.txtStudentYearLevel.grid(row=4, column=1)

        self.lblStudentGender = Label(StudentInfoFrame, font=("Poppins", 10), text="Gender:*", padx=5, pady=5,
                                      bg="RoyalBlue1", fg="snow")
        self.lblStudentGender.grid(row=5, column=0, sticky=W)
        self.txtStudentGender = ttk.Combobox(StudentInfoFrame, value=["Male", "Female"], font=("Poppins", 10),
                                             state="readonly", textvariable=Student_Gender, width=27)
        self.txtStudentGender.grid(row=5, column=1)

        self.lblStudentCourse = Label(StudentInfoFrame, font=("Poppins", 10), text="Course:*", padx=5, pady=5,
                                      bg="RoyalBlue1", fg="snow")
        self.lblStudentCourse.grid(row=6, column=0, sticky=W)
        self.txtStudentCourse = Entry(StudentInfoFrame, font=("Poppins", 10), textvariable=Student_Course, width=30)
        self.txtStudentCourse.grid(row=6, column=1)
        self.SearchBar = Entry(StudentDetailsFrame, font=("Poppins", 10), textvariable=SearchBar_Var, width=12)
        self.SearchBar.place(x=8, y=3)
        self.SearchBar.insert(0,'Search here')
        self.lblOwner = Label(self.root, font=("Poppins", 11), text="Submitted by: Martinez, Ryan James J.", bg ="gray15", fg="snow")
        self.lblOwner.place(x=17,y=376)

        #Treeview
        
        scrollbar = Scrollbar(StudentDetailsFrame, orient=VERTICAL)
        scrollbar.grid(row=1, column=1, sticky='ns')

        self.studentlist = ttk.Treeview(StudentDetailsFrame,
                                        columns=("ID Number", "Name", "Course", "Year Level", "Gender"),
                                        yscrollcommand=scrollbar.set)

        self.studentlist.heading("ID Number", text="ID Number", anchor=CENTER)
        self.studentlist.heading("Name", text="Name")
        self.studentlist.heading("Course", text="Course")
        self.studentlist.heading("Year Level", text="Year Level")
        self.studentlist.heading("Gender", text="Gender")
        self.studentlist['show'] = 'headings'

        self.studentlist.column("ID Number", width=80, anchor=CENTER, stretch=False)
        self.studentlist.column("Name", width=140, stretch=False)
        self.studentlist.column("Course", width=85, anchor=CENTER, stretch=False)
        self.studentlist.column("Year Level", width=80, anchor=CENTER, stretch=False)
        self.studentlist.column("Gender", width=80, anchor=CENTER, stretch=False)

        self.studentlist.grid(row=1, column=0, padx=8)
        scrollbar.config(command=self.studentlist.yview)
        
        #Buttons

        self.btnAddID = Button(StudentInfoFrame, text="Add", font=('Poppins', 10), height=1, width=10, bd=4,
                               bg="RoyalBlue3", fg="snow", command=addData)
        self.btnAddID.grid(row=7, column=1)
        self.btnUpdate = Button(StudentInfoFrame, text="Update", font=('Poppins', 10), height=1, width=10, bd=3,
                                bg="RoyalBlue3", fg="snow", command=updateData)
        self.btnUpdate.place(x=25,y=193)
        self.btnClear = Button(StudentInfoFrame, text="Clear", font=('Poppins', 10), height=1, width=10, bd=4,
                               bg="RoyalBlue3", fg="snow", command=clear)
        self.btnClear.grid(row=8, column=1)
        self.btnDelete = Button(StudentDetailsFrame, text="Delete", font=('Poppins', 10), height=1, width=10,
                                bg="RoyalBlue3", fg="snow", command=deleteData)
        self.btnDelete.place(x=386)
        self.btnSelect = Button(StudentDetailsFrame, text="Select", font=('Poppins', 10), height=1, width=10,
                              bg="RoyalBlue3", fg="snow", command=editData)
        self.btnSelect.place(x=291)
        self.btnSearch = Button(StudentDetailsFrame, text="Search", font=('Poppins', 10), height=1, width=10,
                                bg="RoyalBlue3", fg="snow", command=searchData)
        self.btnSearch.place(x=103)
        self.btnRefresh = Button(StudentDetailsFrame, text="Show All", font=('Poppins', 10), height=1, width=10,
                              bg="RoyalBlue3", fg="snow", command=Refresh)
        self.btnRefresh.grid(row=0, column=0)
        
        
        
        displayData()

    def save_data(self): 
        temps = []
        with open(self.filename, "w", newline='') as update:
            fieldnames = ["ID Number", "Name", "Course", "Year Level", "Gender"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp = {"ID Number": id}
                for key, value in val.items(): 
                    temp[key] = value 
                temps.append(temp) 
            writer.writerows(temps) 

        
if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
