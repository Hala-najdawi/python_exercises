#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
from tkinter import *
from tkinter import messagebox
from functools import reduce

class Employee:
      def __init__(self):
        # CREATE DATABASE FILE AND CONNECT TO IT
        self.__conn = sqlite3.connect('OrgDB.db')
        self.__c = self.__conn.cursor()

        # CREATE EMPLOYEES TABLE
        query = """CREATE TABLE IF NOT EXISTS employees (
                        number int, name text, gender text,
                        nationality text, dob text, address text,
                        department text, salary real )
        """
        self.__c.execute(query)
        self.__conn.commit()

      def add_record(self, employee: {}):
       query = f""" INSERT INTO employees VALUES (
              {employee["number"]},
             '{employee["name"]}',
             '{employee["gender"]}',
             '{employee["nationality"]}',
             '{employee["dob"]}',
             '{employee["address"]}',
             '{employee["department"]}',
              {employee["salary"]}
       )""" 
       self.__c.execute(query)
       self.__conn.commit()

      def get_record(self,condition=""):
        query = f"SELECT * from employees {condition}"
        records = self.__c.execute(query)
        return list(records)
      def __del__(self):
        self.__conn.close()
employees_list = []
root = Tk(className="My First GUI")
root.geometry('500x500+500+100')
top = Menu(root)
root.config(menu=top)
def add_employee():
        add_window = Toplevel(root)
        add_window.title('Add New Employee')
        add_window.geometry('700x500+500+100')
        Label(add_window, text="Add New Employee").grid()
        number = Label(add_window, text="Number").place(x=30, y=40)
        name = Label(add_window, text="Name").place(x=30, y=60)
        gender = Label(add_window, text="Gender").place(x=30, y=80)
        nationality = Label(add_window, text="Nationality").place(x=30, y=100)
        dob = Label(add_window, text="DOB").place(x=30, y=120)
        address = Label(add_window, text="Address").place(x=30, y=140)
        department = Label(add_window, text="Department").place(x=30, y=160)
        salary = Label(add_window, text="Salary").place(x=30, y=180)

        number_value = IntVar()
        name_value = StringVar()
        gender_value = StringVar()
        nationality_value = StringVar()
        dob_value = StringVar()
        address_value = StringVar()
        department_value = StringVar()
        salary_value = StringVar()

        Entry(add_window, textvariable=number_value).place(x=100, y=40)
        Entry(add_window, textvariable=name_value).place(x=100, y=60)
        Entry(add_window, textvariable=gender_value).place(x=100, y=80)
        Entry(add_window, textvariable=nationality_value).place(x=100, y=100)
        Entry(add_window, textvariable=dob_value).place(x=100, y=120)
        Entry(add_window, textvariable=address_value).place(x=100, y=140)
        Entry(add_window, textvariable=department_value).place(x=100, y=160)
        Entry(add_window, textvariable=salary_value).place(x=100, y=180)

        def save_employee():
            employees = Employee()
            employees.add_record({
                "number": number_value.get(),
                "name": name_value.get(),
                "gender": gender_value.get(),
                "nationality": nationality_value.get(),
                "dob": dob_value.get(),
                "address": address_value.get(),
                "department": department_value.get(),
                "salary": salary_value.get()
            })

        Button(add_window, text="Save Record", command=save_employee).place(x=30, y=200)

    
def veiw_employee(columns='*', condition=""):
        c=Toplevel(root)
        employees = Employee()
        records = employees.get_record()

        data = 'Number \t\t Name \t\t Gender \t\t Nationality \t\t DOB \t\t Address \t\t Department \t\t Salary \n'
        Label(c, text=data).grid()

        for employee in records:
            record = f"{employee[0]} \t\t {employee[1]} \t\t {employee[2]} \t\t {employee[3]} \t\t " \
                     f"{employee[4]} \t\t {employee[5]} \t\t {employee[6]} \t\t {employee[7]} \n"
            Label(c, text=record).grid()
top = Menu(root)
root.config(menu=top)
file = Menu(top, tearoff=0)
file.add_command(label="Exit", command=root.destroy)
top.add_cascade(label="File", menu=file)
employees = Menu(top, tearoff=0)
employees.add_command(label='Add', command=add_employee)
employees.add_command(label='View', command=veiw_employee)
top.add_cascade(label="Employees", menu=employees)
root.mainloop()

