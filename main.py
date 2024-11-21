from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from main_window import MainWindow
import sys 

def main():
    app = QApplication([])   
    window = MainWindow()
    window.show()  
    app.exec()

if __name__ == "__main__":
    main()
    