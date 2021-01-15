from gi.repository import Gtk
from gi.repository import Granite
from Zettel import Zettel


class ZettelView(Gtk.Box):
    def __init__(self, zettel=Zettel()):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.zettel = zettel
        self.label = Gtk.Label(label=zettel.text)


        super().pack_start(self.label, True, True, 0)
        self.label.show()

    def set_zettel(self, zettel):

        self.zettel = zettel
        self.label = Gtk.Label(zettel.text)