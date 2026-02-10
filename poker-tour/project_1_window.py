import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont

class AudienceDisplay(QMainWindow):
    # This is the main audience window, which will recieve updates from the admin window
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audience Display")
        self.setGeometry(100, 100, 800, 600) #Aternatively, we could use self.showFullScreen() to set audience window to Full Screen.

        # Central window & Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Large display label (Includes Timer, blinds)
        self.display_label = QLabel("Waiting for updates...")
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Large Text & bold font
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.display_label.setFont(font)

        layout.addWidget(self.display_label)

        #Sytle Guide
        self.setStyleSheet("""
                QMainWindow {
                    background-color: #1a1a1a;
                    }
                    QLabel {
                        color: #00ff00;
                        padding: 20px;
                    }
        """)

    def update_display(self, text):
        self.display_label.setText(text)

class AdminWindow(QMainWindow):
    message_signal = pyqtSignal(str)

    def __init__(self, audience_window):
        super().__init__()
        self.audience_window = audience_window
        self.setWindowTitle("Admin Pannel")
        self.setGeometry(100, 100, 800, 600)

        # Central Widget & Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        #input areas
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a message to display")
        layout.addWidget(QLabel("Control Panel:"))
        layout.addWidget(self.input_field)

        #Buttons
        self.send_button = QPushButton("send to Audience Display")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        # Quick action buttons
        self.quick_btn1 = QPushButton("show 'Break Time'")
        self.quick_btn1.clicked.connect(lambda: self.send_quick_message("break Time"))
        layout.addWidget(self.quick_btn1)

        self.quick_btn2 = QPushButton("show 'Tournoment Started'")
        self.quick_btn2.clicked.connect(lambda: self.send_quick_message("Tournoment started"))
        layout.addWidget(self.quick_btn2)

        # add stretch to push to the top
        layout.addStretch()

        # Connect Signal to audeince window, update method
        self.message_signal.connect(self.audience_window.update_display)

    def send_message(self):
        text = self.input_field.text()
        if text:
            self.message_signal.emit(text)
            self.input_field.clear()

    def send_quick_message(self, message):
        self.message_signal.emit(message)

def main():
    app = QApplication(sys.argv)

    audience = AudienceDisplay()
    audience.show()

    admin = AdminWindow(audience)
    admin.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()


