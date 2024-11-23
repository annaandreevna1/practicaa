 
from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QHBoxLayout,QPushButton, QWidget, QListView, QVBoxLayout
from database import Database
from form_window import FormWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Главная")
        self.resize(800,600)
 
        list_model = QStringListModel()
        list_model.setStringList(self.get_patients())
 
        list_widget = QWidget()
        self.list_view = QListView(list_widget)
        self.list_view.setModel(list_model)
        self.list_view.resize(800,600)
 
        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_patients)
        self.del_button = QPushButton("Удалить")
        self.del_button.clicked.connect(self.del_patients)
        self.edit_button = QPushButton("Изменить")
        self.edit_button.clicked.connect(self.edit_patients)
        self.update_button = QPushButton("Обновить")
        self.update_button.clicked.connect(self.update_list_view_patients)
 
        buttons = QHBoxLayout()
        buttons.addWidget(self.add_button)
        buttons.addWidget(self.del_button)
        buttons.addWidget(self.edit_button)
        buttons.addWidget(self.update_button)
        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons)
 
        layout = QVBoxLayout()
        layout.addWidget(buttons_widget)
        layout.addWidget(list_widget)
        widget = QWidget()
        widget.setLayout(layout)
 
        self.setCentralWidget(widget)
 
    def get_patients(self):
        db = Database()
        result_raw = db.get_patients()
        result = []
        for r in result_raw:
            result.append(str(r["id"])+ "."+ r["name"]+ " "+ r["firstname"]+ " "+ r["otchestvo"] )
        return result
 
    def get_list_model_patients(self):
        list_model = QStringListModel()
        list_model.setStringList(self.get_patients())
        return list_model
    
    def update_list_view_patients(self):
        self.list_view.setModel(self.get_list_model_patients())
 
    def del_patients(self):
        db = Database()
        indexes = self.list_view.selectedIndexes()
        for index in indexes:
            id = str(index.data()).split(":")[0]
            db.del_patients(id)
        self.update_list_view_patients()
    
    
    def add_patients(self):
        form_window = FormWindow(self)
        form_window.submitted_data.connect(self.handle_submitted_data)  
        if form_window.exec() == 1: 
            # db.add_patients(form_window.name_text.text()) is REMOVED
            self.update_list_view_patients()
 
    def handle_submitted_data(self, data):
        db = Database()
        db.add_patients(data) 
        self.update_list_view_patients()
 
    def edit_patients(self):
        if len(self.list_view.selectedIndexes()) <= 0: return
        form_window = FormWindow(self, str(self.list_view.selectedIndexes()[0].data()))
        if form_window.exec() == 1:
            self.update_list_view_patients()