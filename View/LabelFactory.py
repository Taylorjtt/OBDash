import customtkinter

from View.Colors import Colors


def getLargeLabel(root,text):
    label = customtkinter.CTkLabel(root, text=text)
    label.configure(font=('Myriad', 110,'bold'), text_color=Colors.white)
    return label;

def getLargeData(root, initialData):
    label = customtkinter.CTkLabel(root, text=initialData)
    label.configure(font=('Myriad', 130,'bold'), text_color=Colors.yellow)
    return label
