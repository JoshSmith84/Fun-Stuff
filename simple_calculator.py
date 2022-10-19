# simple_calculator.py - Practice project to work on my understanding of tkinter
# Author - Josh Smith

import tkinter

window = tkinter.Tk()

# Main geometry
window.title("Josh's Shitty Calculator")
window.geometry('640x480+200+200')
window_padding = 8
window['padx'] = window_padding

# Widget to display result
result = tkinter.Entry(window)
result.grid(row=0, column=0, sticky='nsew')

# Frame for key pad
key_pad = tkinter.Frame(window)
key_pad.grid(row=1, column=0, sticky='nsew')

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)],
        ]

row = 0
for key_row in keys:
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, text=key[0]).grid(row=row,
                                                  column=col,
                                                  columnspan=key[1],
                                                  sticky='ew')
        col += key[1]
    row += 1

window.mainloop()

# Got the base GUI done. Now need TODO the functions