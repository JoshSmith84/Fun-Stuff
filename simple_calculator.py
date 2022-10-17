# simple_calculator.py - Practice project to work on my understanding of tkinter
# Author - Josh Smith

import tkinter

window = tkinter.Tk()

# Main geometry
window.title("Josh's Shitty Calculator")
window.geometry('320x240+200+200')
window['padx'] = 8
window['pady'] = 8

# 6 Rows (0-5)
# 4 columns (0-3)
for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(6):
    window.rowconfigure(i, weight=1)

# Widget to display result
result = tkinter.Entry(window)
result.grid(row=0, column=0, columnspan=4, sticky='nsew')

#  C and CE buttons
c_button = tkinter.Button(window, text='C')
ce_button = tkinter.Button(window, text='CE')
c_button.grid(row=1, column=0, sticky='nsew')
ce_button.grid(row=1, column=1, sticky='nsew')

# 7, 8, 9, +
seven_button = tkinter.Button(window, text='7')
eight_button = tkinter.Button(window, text='8')
nine_button = tkinter.Button(window, text='9')
plus_button = tkinter.Button(window, text='+')
seven_button.grid(row=2, column=0, sticky='nsew')
eight_button.grid(row=2, column=1, sticky='nsew')
nine_button.grid(row=2, column=2, sticky='nsew')
plus_button.grid(row=2, column=3, sticky='nsew')


# 4, 5, 6, -
four_button = tkinter.Button(window, text='4')
five_button = tkinter.Button(window, text='5')
six_button = tkinter.Button(window, text='6')
minus_button = tkinter.Button(window, text='-')
four_button.grid(row=3, column=0, sticky='nsew')
five_button.grid(row=3, column=1, sticky='nsew')
six_button.grid(row=3, column=2, sticky='nsew')
minus_button.grid(row=3, column=3, sticky='nsew')

# 1, 2, 3, *
one_button = tkinter.Button(window, text='1')
two_button = tkinter.Button(window, text='2')
three_button = tkinter.Button(window, text='3')
times_button = tkinter.Button(window, text='*')
one_button.grid(row=4, column=0, sticky='nsew')
two_button.grid(row=4, column=1, sticky='nsew')
three_button.grid(row=4, column=2, sticky='nsew')
times_button.grid(row=4, column=3, sticky='nsew')

# 0, = (spans two columns), /
zero_button = tkinter.Button(window, text='0')
equal_button = tkinter.Button(window, text='=')
div_button = tkinter.Button(window, text='/')
zero_button.grid(row=5, column=0, sticky='nsew')
equal_button.grid(row=5, column=1, columnspan=2, sticky='nsew')
div_button.grid(row=5, column=3, sticky='nsew')

window.mainloop()

# Got the base GUI done. Now need TODO the functions