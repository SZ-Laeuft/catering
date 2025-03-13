from PyQt5.QtWidgets import *
import sys

class Catering(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Title
        self.setWindowTitle("Oida")

        # QSS
        with open("qss", "r") as fh:
            app.setStyleSheet(fh.read())

        self.button = QPushButton("Oida", self)

        self.layout = QGridLayout()

        self.layout.addWidget(self.button, 0, 0)

app = QApplication(sys.argv)

# Create and show the window
window = Catering()
window.show()

# Start the application event loop
sys.exit(app.exec_())