# Program name : predict_salary.py


from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import os.path
from tkinter import messagebox as msg
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


# Linear Regression Model starts from here
# Reading only 'expyr' and 'salary' from empsal.csv
class Predict_salary:

    def __init__(self, root):
        self.f = Frame(root, height=350, width=500)
        self.f.pack()  # Place the frame on root window

        # Creating label widgets
        self.message_label = Label(self.f, text='Predict Salary given Experience in years', font=('Arial', 14))
        self.expyr_label = Label(self.f, text='Enter Experience in years:', font=('Arial', 14))
        self.input_expyr = Entry(self.f, text='', width=3, font=('Arial', 14))
        self.predicted_salary_label = Label(self.f, text='', font=('Arial', 15))
        # Buttons
        self.confirm_button = Button(self.f, text='Predict Salary Expected', font=('Arial', 14), bg='Orange',
                                     fg='Black', command=self.predict_salary)
        self.exit_button = Button(self.f, text='Exit', font=('Arial', 14), bg='Yellow',
                                  fg='Black', command=root.destroy)

        # Placing the widgets using grid manager
        self.message_label.grid(row=1, column=0)
        self.confirm_button.grid(row=2, column=0)
        self.exit_button.grid(row=2, column=2)
        self.expyr_label.grid(row=3, column=0)
        self.input_expyr.grid(row=3, column=1)
        self.predicted_salary_label.grid(row=4, column=0)

    def predict_salary(self):

        try:

            if os.path.exists('empsal.csv'):
                emp_expr_sal_df = pd.read_csv('empsal.csv', usecols=['expyr', 'salary'])
                print(emp_expr_sal_df)

                expr = emp_expr_sal_df.iloc[:, :-1].values  # expyr is Experience. :-1 picks up as 2D
                salary = emp_expr_sal_df.iloc[:, 1].values

                # Split Train Test data
                X_train, X_test, y_train, y_test = train_test_split(expr, salary, test_size=1 / 3, random_state=0)
                regressor = LinearRegression()
                regressor.fit(X_train, y_train)

                # Prediction. Input years of exp   - field 'expyr' is independent variable (must be 2D)
                # Variable for which prediction to be made must be 2D, so [[ ]]
                # Dependent variable is Salary (y) = m X (x=Exp) + b  ( Eqn :y = mx +c

                # Testing in IDLE shell for a hard coded 8 years expr
                X_new = np.array([[8.0]])  # 8 years expr
                prediction = regressor.predict(X_new)
                print('For 8 yrs exp, salary prediction :%.2f' % prediction)

                # Now input expyr from keyboard using 'Entry' widget of tkinter
                new_expr = DoubleVar()
                new_expr = float(self.input_expyr.get())
                new_expr = [[new_expr]]  # Converting the input in 2D
                prediction = regressor.predict(new_expr)  # prediction is numpy ndarray. Need to access 0th element
                prediction = ("%.2f" % prediction[0])  # Set to 2 decimal places

                self.predicted_salary_label.config(text='Predicted Salary :' + str(prediction))
                print('Predicted Salary:', prediction)  # To print in IDLE shell


        except FileNotFoundError as e:
            msg.showerror('CSV file not found', e)


# --------------------------------------------------
root = Tk()
root.title('Predict Salary given experience in years')
root.geometry('800x600')
conv_csv = Predict_salary(root)
root.mainloop()
