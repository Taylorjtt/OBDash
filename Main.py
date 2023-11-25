from datetime import datetime



import customtkinter

from View.DashView import DashView
from app import App


def updatePresenter(newPresenter):
    presenter = newPresenter


if __name__ == "__main__":
    print(datetime.now())
    customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    App.root = customtkinter.CTk()
    App.root.attributes('-fullscreen', True)
    App.root.geometry('1024x600')
    App.view = DashView()
    print(App.view)
    # run itself again after 1000 ms
    App.root.update_idletasks()
    print("The width of Tkinter window:", App.root.winfo_width())
    print("The height of Tkinter window:", App.root.winfo_height())


    App.root.mainloop()