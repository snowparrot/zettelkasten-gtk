from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Granite
from gi.repository import GtkSource



class ZettelWindow(Gtk.Window):
    def __init__(self, title="Füge Zettel hinzu") -> None:
        super().__init__(title=title)
        self.text_view = Gtk.TextView()

        self.header_bar = Gtk.HeaderBar()
        self.header_bar_button = Gtk.Button. new_from_icon_name('document-save', Gtk.IconSize.LARGE_TOOLBAR)

        self.header_bar.set_show_close_button(True)
        self.header_bar.props.title = title
        self.set_titlebar(self.header_bar)

        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")


        self.header_bar.pack_start(self.header_bar_button)

        self.text_view.get_buffer().set_text(
            """
# Title

#schlagwort
            
## Text
             
            
## Quelle
## Links  
         
"""
        )

        self.add(self.text_view)

def on_save_button(button):


if __name__ == "__main__":

    win = ZettelWindow()
    win.connect("destroy", Gtk.main_quit)

    def on_save_button(button):
        pass

    win.connect("clicked", on_save_button)
    win.show_all()

    Gtk.main()



