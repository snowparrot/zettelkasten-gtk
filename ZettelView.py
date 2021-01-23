from gi.repository import Gtk
from gi.repository import Granite
from Zettel import Zettel


class ZettelView(Gtk.Box): ## TODO: Schöner!
    ## TODO: GtkBox
    def __init__(self, zettel=Zettel(), letters_per_line = 80):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self._letters_per_line = letters_per_line

        self.text_label = Gtk.Label()

        self.set_zettel(zettel)


        super().pack_start(self.text_label, True, True, 0)
        self.text_label.show()

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

        self.text_label.set_text(
            f"""{zettel.title} \t {zettel.name}
            {" ".join(zettel.tags)}
            {intern_text}
            """
            )

    def get_zettel(self):
        return self._zettel
