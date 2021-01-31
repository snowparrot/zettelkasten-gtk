from os import terminal_size
from Zettel import Zettel
from gi.repository import Gtk
from gi.repository import Granite
from ZettelList import ZettelList
from ZettelView import ZettelView
from Zettel import Zettel


class SearchWindow(Gtk.Window):
    def __init__(self) -> None: 
        ## Suchanzeige vom Fenster abstrahieren, clearen des Inhalts muss möglich sein
        super().__init__(title="Suchfenster")
        self.set_size_request(1000, 1000)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.sw = Gtk.ScrolledWindow()

        self.search_view = SearchListView()

        search_box = Gtk.Box(spacing=6)

        self.search_button = Gtk.Button()
        self.search_button.set_label("Suchen")

        self.search_entry = Gtk.Entry()
        self.search_entry.set_text("gesellschaft")

        search_box.pack_start(self.search_entry, True, True, 0)
        search_box.pack_start(self.search_button, False, False, 0)

        self.vbox.pack_start(search_box, False, False, 0)
        self.vbox.pack_start(self.sw, True, True, 0)

        self.sw.add_with_viewport(self.search_view)

        self.add(self.vbox)

    def add_view_into_search_view(self, view):
        self.search_view.add_view(view)

 

    def clear_search_view(self):
        self.sw.remove(self.sw.get_child())
        self.search_view = SearchListView()
        self.sw.add_with_viewport(self.search_view)
        self.show_all()

        


class SearchListView(Gtk.Box):
    def __init__(self) -> None:
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    def add_view(self, view):
        self.pack_start(view, True, True, 0)

if __name__ == "__main__":
    zuri = "/home/snowparrot/NextCloud/Zettelkasten"
    zlist = ZettelList(zuri)
    first_time = True

    ## gtw
    window = SearchWindow()
    window.show_all()
    window.connect("destroy", Gtk.main_quit)
    def on_search_button(button):
        ## Todo: Suchtreffer markieren
        ## Todo: Anzahl Suchtreffer anzeigen (Bei 0 schönen Satz)
        ## Todo: Ordnung der Ergebnisse verbessern
        global first_time 
        if not first_time:
            window.clear_search_view()

        search_term = window.search_entry.get_text()
        results = zlist.search(search_term)
        

        search_label = Gtk.Label(label=f"Suche: {search_term}")
        
        window.add_view_into_search_view(search_label)
        search_label.show()

        for result in results:
            new_zettel_view = ZettelView(result)
            new_zettel_view.set_halign(Gtk.Align.CENTER)
            window.add_view_into_search_view(new_zettel_view)
            new_zettel_view.show()

        first_time = False
        
        

    window.search_button.connect("clicked", on_search_button)
    
    Gtk.main()