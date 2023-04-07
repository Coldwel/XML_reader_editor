import os
import sys
from PyQt5 import QtCore, QtWidgets
from dark_mode import DarkMode
from dark_mode import prettify


class XmlEditor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Driver XML Comment Viewer')
        self.setGeometry(100, 100, 1000, 800)

        self.folder_path = None
        self.xml_files = []

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.browse_button = QtWidgets.QPushButton('Browse')
        self.browse_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.browse_button)

        self.view_button = QtWidgets.QPushButton('View')
        self.view_button.clicked.connect(self.view_files)
        self.view_button.setEnabled(False)
        self.layout.addWidget(self.view_button)

        self.file_list = QtWidgets.QListWidget()
        self.layout.addWidget(self.file_list)

        self.edit_button = QtWidgets.QPushButton('Edit')
        self.edit_button.clicked.connect(self.edit_file)
        self.edit_button.setEnabled(False)
        self.layout.addWidget(self.edit_button)

        self.text_edit = QtWidgets.QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.save_button = QtWidgets.QPushButton('Save')
        self.save_button.clicked.connect(self.save_file)
        self.save_button.setEnabled(False)
        self.layout.addWidget(self.save_button)

        self.dark_mode_button = QtWidgets.QPushButton('Dark')
        self.dark_mode_button.setFixedSize(50, 20)
        self.dark_mode_button.clicked.connect(self.toggle_dark_mode)
        self.layout.addWidget(self.dark_mode_button, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

        self.dark_mode = DarkMode(self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.show()

    def select_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Folder", os.path.expanduser("~"), QtWidgets.QFileDialog.ShowDirsOnly
        )

        if folder_path:
            self.folder_path = folder_path
            self.xml_files = []
            self.file_list.clear()
            self.view_button.setEnabled(True)

    def view_files(self):
        if not self.folder_path:
            return

        self.xml_files = []
        self.file_list.clear()

        for dirpath, dirnames, filenames in os.walk(self.folder_path):
            for filename in filenames:
                if filename.endswith(".xml"):
                    file_path = os.path.join(dirpath, filename)
                    self.file_list.addItem(filename)
                    self.xml_files.append(file_path)

        if self.xml_files:
            self.edit_button.setEnabled(True)
        else:
            QtWidgets.QMessageBox.warning(self, 'No XML files', 'No XML files found in the selected folder.')

    def edit_file(self):
        if not self.xml_files:
            return

        selected_file = self.xml_files[self.file_list.currentRow()]

        with open(selected_file) as f:
            xml_content = f.read()

        pretty_xml = prettify(xml_content)
        self.text_edit.setPlainText(pretty_xml)

        self.save_button.setEnabled(True)

    def save_file(self):
        if not self.xml_files:
            return

        selected_file = self.xml_files[self.file_list.currentRow()]
        with open(selected_file, "w") as f:
            f.write(self.text_edit.toPlainText())

    def toggle_dark_mode(self):
        self.dark_mode.toggle()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = XmlEditor()
    sys.exit(app.exec_())
