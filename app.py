


class App:
    presenter = None;
    view = None
    root = None
    presenterStack = []
    viewStack = []


    @staticmethod
    def nextState(newView, newPresenter):
        App.presenter.stop()
        for widgets in App.root.winfo_children():
            widgets.destroy()
        App.presenter.stop()
        App.presenterStack.append(App.presenter)
        App.viewStack.append(App.view)
        App.view = newView()
        App.presenter = newPresenter()

    @staticmethod
    def back():
        App.presenter.stop()
        App.presenter = App.presenterStack.pop()
        for widgets in App.root.winfo_children():
            widgets.destroy()
        App.view = App.viewStack.pop()
        App.view.__init__()
        App.presenter.__init__()
