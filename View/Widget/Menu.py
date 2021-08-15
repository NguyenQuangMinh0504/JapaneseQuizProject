from tkinter import Menu, BooleanVar, messagebox
from Widget.Status import ActiveStatus
from Widget.AddingWord import VocabularyInput


class MainMenu(Menu):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # profile menu
        profile_menu = Menu(self)
        self.add_cascade(label='Profile', menu=profile_menu)
        profile_menu.add_command(label='Status', command=self.show_status)

        # setting menu
        setting_menu = Menu(self)
        self.add_cascade(label='Setting', menu=setting_menu)
        self.sound = BooleanVar(value=True)
        setting_menu.add_checkbutton(label='Sound', variable=self.sound)
        # typing_menu = Menu(setting_menu)
        # setting_menu.add_cascade(label='Typing', menu=typing_menu)
        # self.kanji = BooleanVar(value=True)
        # self.spelling = BooleanVar(value=True)
        # typing_menu.add_checkbutton(label='Kanji', variable=self.kanji)
        # typing_menu.add_checkbutton(label='Spelling', variable=self.spelling)

        # adding menu
        add_menu = Menu(self)
        self.add_cascade(label='Add', menu=add_menu)
        add_menu.add_command(label='Vocabulary', command=self.add_vocab)

        # help menu
        help_menu = Menu(self)
        self.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About...', command=self.show_about)

    def show_status(self):
        ActiveStatus(root=self)

    def add_vocab(self):
        VocabularyInput(self)

    @staticmethod
    def show_about():
        about_message = "Mimikara Oboeru App"
        about_detail = ("By Nguyễn Quang Minh\n",
                        "For further information please contact ngquangminh05042001@gmail.com")
        messagebox.showinfo(title="About", message=about_message, detail=about_detail)
