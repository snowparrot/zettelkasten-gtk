from gi.repository import Gtk
from gi.repository import Granite
from SearchContainer import SearchContainer


class MainWindow(Gtk.Window):

    def __init__(self) -> None:
        super().__init__(title="Zettelkasten")
        self.set_default_size(500, 500)

        self.sc = SearchContainer()
        self.add(self.sc)



if __name__ == "__main__":
    window = MainWindow()
    window.show_all()
    window.connect("destroy", Gtk.main_quit)

    Gtk.main()



