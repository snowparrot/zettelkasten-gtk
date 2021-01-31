
import gi
import locale
import gettext
import argparse
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gio, Gdk, Granite, GObject
from SearchWindow import SearchWindow
from ZettelList import ZettelList
from Zettel import Zettel
from ZettelView import ZettelView



zuri = "/home/snowparrot/NextCloud/Zettelkasten"
zlist = ZettelList(zuri)
first_time = True

window = SearchWindow()
window.show_all()
window.connect("destroy", Gtk.main_quit)
def on_search_button(button):
    ## Todo: Suchtreffer markieren
    ## Todo: Anzahl Suchtreffer anzeigen (Bei 0 schönen Satz)
    ## Todo: Ordnung der Ergebnisse verbessern

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