from gi.repository import Gtk
from gi.repository import Granite
from Zettel import Zettel


class ZettelView(Gtk.Grid): ## TODO: Schöner!
    ## https://developer.gnome.org/gtk3/stable/ch30s02.html

    ## text nur in v expand, h fill
    def __init__(self, zettel=Zettel(), letters_per_line = 80):
        super().__init__()
        self._letters_per_line = letters_per_line

        self.text_label = Gtk.Label()
        self.text_label.set_hexpand(False)
        self.text_label.set_vexpand(False)
        
        self.title_label = Gtk.Label()
        self.tag_label = Gtk.Label()
        self.name_label = Gtk.Label()

        self.set_zettel(zettel)

        self.attach(self.title_label, 0, 0, 1, 1)
        self.attach_next_to(self.name_label, self.title_label,
                             Gtk.PositionType.RIGHT, 1, 1)
        self.attach_next_to(self.tag_label, self.title_label,
                        Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(self.text_label, self.tag_label,
                        Gtk.PositionType.BOTTOM, 1, 1)  

        self.text_label.show()
        self.tag_label.show()
        self.name_label.show()
        self.title_label.show()


    def set_zettel(self, zettel):

        self._zettel = zettel

        ## creates text which is in order with self._letters_per_line
        intern_text = ""
        n_letters_line = 0

        for word in zettel.text.split(" "):
            if n_letters_line + len(word) < self._letters_per_line:
                intern_text += word + " "
                n_letters_line += len(word) + 1
            else:
                intern_text += "\n" + word + " "
                n_letters_line = len(word) + 1

        self.title_label.set_text(zettel.title)
        self.name_label.set_text(zettel.name)
        self.tag_label.set_text(" ".join(zettel.tags))
        self.text_label.set_text(intern_text)


    def get_zettel(self):
        return self._zettel
