from tkinter import *
import sys
import os
import subprocess

class Empsal:

    # Constructor
    def __init__(self, root):

        self.main_lbl=Label(root, text='Employee Salary Prediction', fg='royalblue', font=('Arial', 40, 'bold underline'))
        self.main_lbl.place(x=300, y=300)

        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.mysql_menu)
        # Now create menu items under menubar
        self.mysql_menu.add_command(label='Build/Display from CSV', command=self.create_csv)
        self.mysql_menu.add_command(label='Convert CSV to Excel', command=self.csv_to_xls)
        self.mysql_menu.add_command(label='Display data from Excel', command=self.excel_to_table)

        # Now add a separator
        self.mysql_menu.add_separator()
        # Now create a Exit menu
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports/Data Visualization', menu=self.data_menu)
        self.data_menu.add_command(label='Sum, Mean, Std Deviation (Gender wise)', command=self.gender_wise_calc)
        self.data_menu.add_command(label='State wise mean expenses and bar graph', command=self.state_wise_mean_calc)
        self.data_menu.add_command(label='State wise total expenses and bar graph', command=self.state_wise_total_calc)
        self.data_menu.add_command(label='Scatter Plot Experience vs Salary', command=self.scatter_plot)

        # Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.predict_salary)


    def create_csv(self):
        os.system("python.exe create_csv.py")
    def csv_to_xls(self):
        os.system("python.exe csv_to_xls.py")
    def excel_to_table(self):
        os.system("python.exe excel_to_table.py")
    def gender_wise_calc(self):
        os.system("python.exe gender_wise_calc.py")
    def state_wise_mean_calc(self):
        os.system("python.exe state_wise_mean_calc.py")
    def state_wise_total_calc(self):
        os.system("python.exe state_wise_total_calc.py")
    def scatter_plot(self):
        os.system("python.exe scatter_plot.py")
    def predict_salary(self):
        os.system("python.exe predict_salary.py")
#=====================================================================================================

root=Tk()
root.title('Employee HR Database Maintenance with Python and Tkinter GUI')

obj=Empsal(root)
root.geometry('800x600')
root.mainloop()
