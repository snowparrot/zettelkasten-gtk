from gi.repository import Gtk
from gi.repository import Granite
from Zettel import Zettel


class ZettelView(Gtk.Box): ## TODO: Schöner!
    def __init__(self, zettel=Zettel(), ):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.text_label = Gtk.Label()

        self.set_zettel(zettel)


        super().pack_start(self.text_label, True, True, 0)
        self.text_label.show()

    def set_zettel(self, zettel):

        self.zettel = zettel
        self.text_label.set_text(zettel.text)

    def get_zettel(self):
        return self.zettel