from tkinter import *

class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg='pink')

        self.MainFrame = Frame(
            self.root,
            bd=10,
            width=330,
            height=480,
            relief=RIDGE,
            bg='deep pink'
        )
        self.MainFrame.grid()
    
        self.WidgetFrame = Frame(
            self.MainFrame,
            bd=10,
            width=310,
            height=440,
            relief=RIDGE, 
            bg='light pink'
        )
        self.WidgetFrame.grid()

        self.lbDisplay = Label(
            self.WidgetFrame, 
            width=30,
            height=2,
            bg='white',
            font=('Quicksand', 14, 'bold'),
            anchor='e'
        )
        self.lbDisplay.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.input_button = ""

        self.create_button("←", 1, 0)
        self.create_button("CE", 1, 1)
        self.create_button("C", 1, 2)
        self.create_button("±", 1, 3)

        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("+", 2, 3)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("*", 4, 3)

        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("=", 5, 2)
        self.create_button("/", 5, 3)

    def create_button(self, text, row, column):
        btnWidget = Button(
            self.WidgetFrame, 
            text=text,
            width=6,
            height=2,
            bd=4,
            bg='light pink',
            font=('Quicksand', 14, 'bold'),
            command=lambda: self.button_click(text)
        )
        btnWidget.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):

        if text == "←":
            self.input_button = self.input_button[:-1]

        elif text in ("CE", "C"):
            self.input_button = ""

        elif text == "±":
            if self.input_button:
                if self.input_button.startswith("-"):
                    self.input_button = self.input_button[1:]
                else:
                    self.input_button = "-" + self.input_button

        elif text == "=":
            try:
                self.input_button = str(eval(self.input_button))
            except:
                self.input_button = "Error"

        else:
            self.input_button += text

        # update display EVERY time
        if self.input_button == "":
            self.lbDisplay.config(text="0")
        else:
            self.lbDisplay.config(text=self.input_button)


if __name__ == "__main__":
    root = Tk()
    app = Calculator(root)
    root.mainloop()