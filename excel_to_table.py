# Prog name : excel_to_table.py

from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd
from pandastable import Table

class create_df:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    # Place the frame on root window

          # Creating label widgets
          self.message_label = Label(self.f,text='Convert Excel to Pandas DF/tkintertable',font=('Arial', 14))

          # Buttons
          self.confirm_button = Button(self.f,text='Convert', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_df)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)

     def conv_to_df(self):

         try:

             empsal_df = pd.read_excel("empsal.xls")
             if (len(empsal_df)== 0):
                    msg.showinfo('No records', 'No records')
             else:
                    msg.showinfo('Pandas DF created', 'Pandas DF created')
                    print(empsal_df)   # To print in IDLE shell

             #Now display the DF in 'Table' object under'pandastable' module
             self.f = Frame(root, height=200, width=300)
             self.f.pack(fill=BOTH,expand=1)
             self.table = Table(self.f, dataframe=empsal_df,read_only=True)
             self.table.show()

         except  FileNotFoundError as e:
             msg.showerror('Error in opening file', e.msg)

#--------------------------------------------------
root=Tk()
root.title('Conversion of Excel data to DF/Tkintertable')
root.geometry('800x600')
conv_csv = create_df(root)
root.mainloop()
