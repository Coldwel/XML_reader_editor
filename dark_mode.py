from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import xml.dom.minidom


def prettify(xml_string):
        """Return a pretty-printed XML string for the given input XML string."""
        dom = xml.dom.minidom.parseString(xml_string)
        return dom.toprettyxml()


class DarkMode:
    def __init__(self, widget):
        self.widget = widget
        self.is_dark = False

    def toggle(self):
        self.is_dark = not self.is_dark
        self.update()

    def update(self):
        palette = QPalette()
        if self.is_dark:
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, Qt.black)
        else:
            palette.setColor(QPalette.Window, Qt.white)
            palette.setColor(QPalette.WindowText, Qt.black)
            palette.setColor(QPalette.Base, Qt.white)
            palette.setColor(QPalette.AlternateBase, Qt.white)
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.black)
            palette.setColor(QPalette.Text, Qt.black)
            palette.setColor(QPalette.Button, Qt.white)
            palette.setColor(QPalette.ButtonText, Qt.black)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(0, 0, 238))
            palette.setColor(QPalette.Highlight, QColor(0, 0, 238))
            palette.setColor(QPalette.HighlightedText, Qt.white)
        self.widget.setPalette(palette)
