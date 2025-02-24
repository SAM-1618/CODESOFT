import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import math

class ChatBotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.a = "XEN"

    def initUI(self):
        self.setWindowTitle("ChatBot")
        self.setGeometry(100, 100, 500, 600)

        
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(18, 18, 18))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(18, 18, 18))
        palette.setColor(QPalette.AlternateBase, QColor(18, 18, 18))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.setPalette(palette)

        
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Arial", 12))
        self.text_area.setStyleSheet("background-color: #121212; color: #ffffff; padding: 10px;")

        
        self.input_area = QLineEdit(self)
        self.input_area.setFont(QFont("Arial", 12))
        self.input_area.setStyleSheet("background-color: #333333; color: #ffffff; padding: 10px;")
        self.input_area.returnPressed.connect(self.handle_input)

        
        self.send_button = QPushButton("Send", self)
        self.send_button.setFont(QFont("Arial", 12))
        self.send_button.setStyleSheet(
            "background-color: #4caf50; color: white; padding: 10px; border-radius: 5px;"
        )
        self.send_button.clicked.connect(self.handle_input)

        
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.input_area)
        layout.addWidget(self.send_button)

       
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show()

    def handle_input(self):
     user_input = self.input_area.text().lower()
     self.text_area.append(f"You: {user_input}")

     if 'hello'  or 'hi'  or 'hey' or 'hii' in user_input:
        response = f"{self.a}: Hello! How can I assist you today?"
     elif 'what can you do'  or 'what are your functionalities' in user_input:
        response = f"{self.a}: I can chat with you, do some basic math, for doing math you need to give command like '''solve 5+8''' and answer your questions!"
     elif 'how are you'  or 'how are you doing' in user_input:
        response = f"{self.a}: I am just a bot, but I am doing great! How about you?"
     elif 'your name' in user_input:
        response = f"{self.a}: I am {self.a}, your personalized chatbot."
     elif 'thank you' or 'thanks' in user_input:
        response = f"{self.a}: You're welcome! If you have more questions, feel free to ask."
     elif 'bye'  or 'goodbye'  or 'good bye' in user_input:
        response = f"{self.a}: Goodbye!"
     elif 'solve' in user_input:
        try:
            expression = user_input.split('solve')[-1].strip()
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            response = f"{self.a}: The result is {result}"
        except Exception as e:
            response = f"{self.a}: I'm sorry, I couldn't solve that problem. Please ensure it's a valid expression."
     else:
        response = "Chatbot: I'm sorry, I don't understand that. Can you please rephrase that?"

    # Display the chatbot's response in the text area
     self.text_area.append(response)
    # Clear the input area after sending the message
     self.input_area.clear()





if __name__ == '__main__':
       app = QApplication(sys.argv)
       ex = ChatBotUI()
       sys.exit(app.exec_())
