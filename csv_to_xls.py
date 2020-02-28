# csv_to_xls.py
# Conversion from CSV data to Microsoft Excel (xls) file


import pandas as pd
from   tkinter import *
from tkinter import messagebox as msg

from pandastable import Table
from tkintertable import TableCanvas

class csv_to_excel_class:

    def __init__(self, root):
          self.f = Frame(root, height=200, width=300)
          self.f.pack()    # Place the frame on root window

          # Creating label widgets
          self.message_label = Label(self.f,text='Conversion of CSV to Excel file',font=('Arial', 14))

          #self.t1 = Text(self.f)
          #self.t1.grid(row=6, column=0)

          # Buttons
          self.confirm_button = Button(self.f,text='Convert', padx=10, pady=15, font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_xls)
          self.exit_button = Button(self.f,text='Exit', padx=10, pady=15, font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)

    def conv_to_xls(self):
          try:

            empsal_df = pd.read_csv('empsal.csv')
            empsal_df = empsal_df.set_index('empno')
            print(empsal_df)

            # Next - Pandas DF to Excel file on disk
            if(len(empsal_df) == 0):
               msg.showinfo('No Rows Selected', 'CSV has no rows')
            else:

               with pd.ExcelWriter('empsal.xls') as writer:     # saves in the current directory
                    empsal_df.to_excel(writer,'EmpsalSheet')
                    writer.save()
                    msg.showinfo('Excel file ceated', 'Excel File created')
            self.f = Frame(root, height=200, width=300)
            self.f.pack(fill=BOTH,expand=1)
            self.table = Table(self.f, dataframe=empsal_df,read_only=True)
            self.table.show()

          except FileNotFoundError as e:
            msg.showerror('Error in opening file', e)


#--------------------------------------------------
root=Tk()
root.title('Conversion of Employee HR CSV data to Excel')
root.geometry('800x600')
conv_disp_tab = csv_to_excel_class(root)
root.mainloop()
