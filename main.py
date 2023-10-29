import tkinter as tk
from tkinter import ttk

vars = [] # tk.StringVar() array

def measure():
    '''
    "Measure" button calls this function
    '''
    for var in vars:
        var[0].set('A')
        var[1].set('B')

# window
window = tk.Tk()
window.title("SolarCell Tester v0.1")
# window.geometry("400x200")

# title
title_label = ttk.Label(master=window, text="SolarCell Tester", font='Calibri 24 bold')
title_label.grid(row=0,column=0,columnspan=2,)



# cells
for i in range(10):
    #one cell
    cell_frame = tk.LabelFrame(master=window, text='Cell {cell:d}'.format(cell=i+1))
    cell_frame.grid(row=i//2+1, column=i%2, padx=10, pady=10)

    # textvariable
    var_v = tk.StringVar()
    var_v.set('0')

    var_i = tk.StringVar()
    var_i.set('0.0')
    vars.append([var_v, var_i])

    v_label = tk.Label(master=cell_frame, text='OCV(V) ',relief='groove', justify='left',padx=5)
    i_label = tk.Label(master=cell_frame, text='SCC(mA)',relief='groove', justify='left',padx=5)

    v_label.grid(row=1,column=1, padx=10, pady=5, sticky='W')
    i_label.grid(row=2,column=1, padx=10, pady=5)

    v_data_lbl = tk.Label(master=cell_frame, textvariable=vars[i][0], relief='sunken', width=4)
    i_data_lbl = tk.Label(master=cell_frame, textvariable=vars[i][1], relief='sunken', width=4)

    v_data_lbl.grid(row=1, column=2, padx=10, pady=5)
    i_data_lbl.grid(row=2, column=2, padx=10, pady=5)

# buttons
measr_btn = tk.Button(master=window, text='Measure', command=measure)
measr_btn.grid(row=13,column=1,padx=10,pady=10, sticky='E')

# run 
window.mainloop()