import tkinter as tk
from tkinter import ttk
from Setting import Load
from View.Controller import Control


class FirstFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        data = Load.Load.load_unit_complete()
        k = 1
        self.dict = []
        for i in range(4):
            for j in range(3):
                label = "Unit {}".format(k)
                dict[label] = tk.Button(self, text=label)
                dict[label].grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
                if data[label]:
                    dict[label].config(highlightbackground='green')
                else:
                    dict[label].config(highlightbackground='red')
                k += 1


class QuizFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        unit_select_frame = self.UnitSelectFrame(self)
        unit_select_frame.pack()
        label_input_frame = self.LabelInputFrame(self)
        label_input_frame.pack()

    class UnitSelectFrame(tk.Frame):
        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            ttk.Label(self, text='Unit').grid(row=0, column=0)
            self.unit_select_spin_box = ttk.Combobox(self, textvariable=tk.StringVar(), values=list(range(1, 12)))
            self.unit_select_spin_box.grid(row=0, column=1)
            self.select_unit_button = ttk.Button(self, text='Select')
            self.select_unit_button.grid(row=0, column=2)

    class LabelInputFrame(tk.Frame):
        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            ttk.Label(self, text='Kanji').grid(row=0, column=0, sticky=tk.W, padx=5)
            self.kanji_input = ttk.Entry(self)
            self.kanji_input.grid(row=1, column=0)


            # self.kanji_input.config(validate='all',
            #                         validatecommand=(parent.register(parent.validate), '%d'))
            # self.kanji_input.bind('<Return>', parent.handle)


            ttk.Label(self, text='Spelling').grid(row=0, column=1, sticky=tk.W, padx=5)
            self.spelling_input = ttk.Entry(self)
            self.spelling_input.grid(row=1, column=1)
            # self.spelling_input.config(validate='all',
            #                            validatecommand=(parent.register(parent.validate), '%d'))
            # self.spelling_input.bind('<Return>', parent.handle)

            # self.button = tk.Button(self, text='Check', command=parent.handle)
            # self.button.grid(row=1, column=2)
