import sys
import qrcode
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR kod olusturucu")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)

        self.generate_button = QPushButton("olustur")
        self.generate_button.clicked.connect(self.qr_code_olustur)
        self.layout.addWidget(self.generate_button)

        self.qr_label = QLabel()
        self.layout.addWidget(self.qr_label)

    def qr_code_olustur(self):
        text = self.textbox.text()
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")

            pixmap =QPixmap("qrcode.png")
            self.qr_label.setPixmap(pixmap)
            self.qr_label.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
