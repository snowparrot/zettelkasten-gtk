from Zettel import Zettel
from gi.repository import Gtk
from gi.repository import Granite
from ZettelList import ZettelList
from ZettelView import ZettelView
from Zettel import Zettel


class SearchWindow(Gtk.Window): ##TODO:gtk Box
    def __init__(self) -> None:
        super().__init__(title="Suchfenster")
        self.set_size_request(1000, 1000)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.sw = Gtk.ScrolledWindow()
        self.search_grid = Gtk.Grid()
        #self.vbox_sw = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        search_box = Gtk.Box(spacing=6)

        self.search_button = Gtk.Button()
        self.search_button.set_label("Suchen")

        self.search_entry = Gtk.Entry()
        self.search_entry.set_text("gesellschaft")

        search_box.pack_start(self.search_entry, True, True, 0)
        search_box.pack_start(self.search_button, False, False, 0)

        self.vbox.pack_start(search_box, False, False, 0)
        self.vbox.pack_start(self.sw, True, True, 0)

        self.sw.add_with_viewport(self.search_grid)
        self._first_element = True


        self.add(self.vbox)

    def add_view_into_scrollable(self, view):
        if self._first_element:
            self.search_grid.attach(view, 1, 0, 1, 1)
            self._first_element = False
            self._last_attached_widget = view
        else:
            self.search_grid.attach_next_to(view, self._last_attached_widget, 
                Gtk.PositionType.BOTTOM, 1, 1)
            self._last_attached_widget = view




if __name__ == "__main__":
    zuri = "/home/snowparrot/NextCloud/Zettelkasten"
    zlist = ZettelList(zuri)


    ## gtk
    window = SearchWindow()
    window.show_all()
    window.connect("destroy", Gtk.main_quit)
    def on_search_button(button):
        search_term = window.search_entry.get_text()

        results = zlist.search(search_term)
        search_label = Gtk.Label(label=f"Suche: {search_term}")
        
        window.add_view_into_scrollable(search_label)
        search_label.show()

        for result in results:
            new_zettel_view = ZettelView(result)
            window.add_view_into_scrollable(new_zettel_view)
            new_zettel_view.show()
        

    window.search_button.connect("clicked", on_search_button)
    
    Gtk.main()