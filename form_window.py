from PyQt6.QtCore import QSize, QStringListModel, pyqtSignal
from PyQt6.QtWidgets import QMainWindow,QDialog,QLabel,QHBoxLayout, QPushButton, QLineEdit, QWidget, QListView, QVBoxLayout
from database import Database

class FormWindow(QDialog):
    submitted_data = pyqtSignal(dict)
    def __init__(self, parent= None, object = None, name=None, firstname=None, otchestvo=None, day_births=None, gender=None, address=None, phone_number=None, date_of_receipt=None, time_of_receipt=None):
        super().__init__(parent)
        if object is None:
            self.setWindowTitle("Добавление")
            self.button = QPushButton("Добавить")
        else:
            self.setWindowTitle("Изменение")
            self.button = QPushButton("Изменить")
            self.id = object.split(":")[0]

        self.button.clicked.connect(self.submit_data)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.create_name_input_widget("Имя", name))
        self.layout.addWidget(self.create_name_input_widget("Фамилия", firstname))
        self.layout.addWidget(self.create_name_input_widget("Отчество", otchestvo))
        self.layout.addWidget(self.create_name_input_widget("День рождения", day_births))
        self.layout.addWidget(self.create_name_input_widget("Пол", gender))
        self.layout.addWidget(self.create_name_input_widget("Адресс", address))
        self.layout.addWidget(self.create_name_input_widget("Номер телефона", phone_number))
        self.layout.addWidget(self.create_name_input_widget("Дата поступления", date_of_receipt))
        self.layout.addWidget(self.create_name_input_widget("Время поступления", time_of_receipt))
        self.setLayout(self.layout)

        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def create_name_input_widget(self, label_text, data=None):
        label = QLabel(label_text)
        if data is None:
            line_edit = QLineEdit()
        else:
            try:
                line_edit = QLineEdit(data)  
            except Exception as e:
                line_edit = QLineEdit("Invalid Input")
                print(f"Error processing data for {label_text}: {e}")

        input_layout = QHBoxLayout()
        input_layout.addWidget(label)
        input_layout.addWidget(line_edit, stretch=1)

        input_widget = QWidget()
        input_widget.setLayout(input_layout)
        return input_widget

        

    def submit_data(self):
        submitted = {}
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QWidget) and widget.layout(): #Check for QWidget and nested layouts
                line_edit = widget.findChild(QLineEdit)
                if line_edit:
                    label = widget.layout().itemAt(0).widget().text() #get label text
                    submitted[label] = line_edit.text()
        self.submitted_data.emit(submitted)
        self.close()

    def close(self):
        self.done(1) 
