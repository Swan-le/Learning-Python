import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

class CountdownTimer(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setWindowTitle("Countdown Timer")
       self.setGeometry(100, 100, 500, 400)

        #Timer State
       self.time_remain = 600
       self.is_running = False

       # Setup UI
       self.setup_ui()

       #Creat Qtimer object, this triggers update every second
       self.timer = QTimer()
       self.timer.timeout.connect(self.update_timer)
    def setup_ui(self):
        # Central user interface
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        #timer Display Large LCD style
        self.timer_display = QLabel(self.format_time(self.time_remain))
        self.timer_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Large Bold Font 
        font = QFont("Helvetica", 100, QFont.Weight.Bold)
        self.timer_display.setFont(font)

        main_layout.addWidget(self.timer_display)

        # Control Button Layout (Horrizonatal)
        button_layout = QHBoxLayout()

        # Start & Pause buttons 
        self.start_pause_btn = QPushButton("Start")
        self.start_pause_btn.clicked.connect(self.toggle_timer)
        button_layout.addWidget(self.start_pause_btn)

        # Reset Button
        self.reset_btn = QPushButton("Restart")
        self.reset_btn.clicked.connect(self.reset_timer)
        button_layout.addWidget(self.reset_btn)

        #add 1 minute button 
        self.add_time_btn = QPushButton("Add +1 Minute")
        self.add_time_btn.clicked.connect(self.add_minute)
        button_layout.addWidget(self.add_time_btn)

        main_layout.addLayout(button_layout)

        #Styling
        self.setStyleSheet(""" 
            QMainWindow {
                background-color: #2c3e50;
            }
            QLabel {
                color: #ecf0f1;
                background-color: #34495e;
                border: 3px solid #1abc9c;
                border-radius: 10px;
                padding: 30px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)

    def format_time(self, seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"
    
    def update_timer(self):
        if self.time_remain > 0:
            self.time_remain -= 1
            self.timer_display.setText(self.format_time(self.time_remain))

            if self.time_remain <= 60:
                self.timer_display.setStyleSheet("""
                    color: #e74c3c;
                    background-color: #34495e;
                    border: 3px solid #e74c3c;
                    border-radius: 10px;
                    padding: 30px;
                """)
        else:
            self.timer.stop()
            self.is_running = False
            self.start_pause_btn.setText("start")
            self.timer_display.setText("00:00")
            # Add sound Alert here
            print("Time's up!")
    
    def toggle_timer(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_pause_btn.setText("Resume")
        else:
            self.timer.start(1000) #1000 = 1 second
            self.is_running = True
            self.start_pause_btn.setText("Pause")

    def reset_timer(self):
        self.timer.stop()
        self.is_running = False
        self.time_remain = 600 #Reset to 10 minutes
        self.timer_display.setText(self.format_time(self.time_remain))
        self.start_pause_btn.setText("Start")
        
        # Reset color to normal
        self.timer_display.setStyleSheet("""
            color: #ecf0f1;
            background-color: #34495e;
            border: 3px solid #1abc9c;
            border-radius: 10px;
            padding: 30px;
        """)

    def add_minute(self):
        self.time_remain += 60
        self.timer_display.setText(self.format_time(self.time_remain))

def main():
    app = QApplication(sys.argv)
    timer = CountdownTimer()
    timer.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()

