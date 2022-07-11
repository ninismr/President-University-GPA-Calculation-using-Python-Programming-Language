from PyQt5.QtWidgets import (
    QApplication, QLayout, QWidget, QPushButton, QFormLayout, 
    QLineEdit, QLabel, QComboBox, QTableWidget, 
    QTableWidgetItem
)

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Grade Point Average Calculator')
        self.resize(750, 750)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.name_input1 = QLabel('')
        self.studentID_input1 = QLabel('')
        self.major_input1 = QLabel('')
        self.class_input1 = QLabel('')
        self.batch_input1 = QLabel('')
        self.empty1_label = QLabel('')
        self.result_label = QLabel('')
        self.empty2_label = QLabel('')
        self.A_label = QLabel('')
        self.A_min_label = QLabel('')
        self.B_plus_label = QLabel('')
        self.B_label = QLabel('')
        self.B_min_label = QLabel('')
        self.C_plus_label = QLabel('')
        self.C_label = QLabel('')
        self.D_label = QLabel('')
        self.E_label = QLabel('')
        self.empty3_label = QLabel('')
        self.totIdx_label = QLabel('')
        self.totCrs_label = QLabel('')
        self.totGPA_label = QLabel('')
        self.empty4_label = QLabel('')
        self.button = QPushButton('Click Here to Calculate Your GPA')
        self.button.clicked.connect(self.show_window)

        self.layout.addRow(self.name_input1)
        self.layout.addRow(self.studentID_input1)
        self.layout.addRow(self.major_input1)
        self.layout.addRow(self.class_input1)
        self.layout.addRow(self.batch_input1)
        self.layout.addRow(self.empty1_label)
        self.layout.addRow(self.result_label)
        self.layout.addRow(self.empty2_label)
        self.layout.addRow(self.A_label)
        self.layout.addRow(self.A_min_label)
        self.layout.addRow(self.B_plus_label)
        self.layout.addRow(self.B_label)
        self.layout.addRow(self.B_min_label)
        self.layout.addRow(self.C_plus_label)
        self.layout.addRow(self.C_label)
        self.layout.addRow(self.D_label)
        self.layout.addRow(self.E_label)
        self.layout.addRow(self.empty3_label)
        self.layout.addRow(self.totIdx_label)
        self.layout.addRow(self.totCrs_label)
        self.layout.addRow(self.totGPA_label)
        self.layout.addRow(self.empty4_label)
        self.layout.addRow(self.button)
        self.button.setStyleSheet('background-color: #C0C0C0;')

    def show_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.show()


class SecondWindow(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.setWindowTitle('Grade Point Average Calculator')
        self.resize(750, 750)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.parent = parent

        self.name_label = QLabel('Name: ')
        self.name_input = QLineEdit()
        self.studentID_label = QLabel('Student ID: ')
        self.studentID_input = QLineEdit()
        self.major_label = QLabel('Major: ')
        self.major_combobox = QComboBox()
        self.major_combobox.addItems(['Accounting', 'Business Administration', 'Management', 
        'Actuarial Science', 'Civil Engineering', 'Industrial Engineering', 
        'Mechanical Engineering', 'Electrical Engineering', 
        'Environmental Engineering', 'Visual Communication Design', 
        'Information Technology', 'Information System', 
        'International Relations', 'Communication', 'Law', 
        'Primary School Teacher Education'])
        self.class_label = QLabel('Class: ')
        self.class_input = QLineEdit()
        self.batch_label = QLabel('Batch: ')
        self.batch_combobox = QComboBox()
        self.batch_combobox.addItems(['2017', '2018', '2019', '2020']) 

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Subject Name', 'Score'])

        self.button_addLine = QPushButton('Add Subject')
        self.button_removeLine = QPushButton('Remove Subject')
        self.button_calcGPA = QPushButton('Calculate GPA')

        self.layout.addRow(self.name_label, self.name_input)
        self.layout.addRow(self.studentID_label, self.studentID_input)
        self.layout.addRow(self.major_label, self.major_combobox)
        self.layout.addRow(self.class_label, self.class_input)
        self.layout.addRow(self.batch_label, self.batch_combobox)
        self.layout.addRow(self.table)
        self.layout.addRow(self.button_addLine)
        self.layout.addRow(self.button_removeLine)
        self.layout.addRow(self.button_calcGPA)

        self.button_addLine.setStyleSheet('background-color: #C0C0C0;')
        self.button_removeLine.setStyleSheet('background-color: #C0C0C0;')
        self.button_calcGPA.setStyleSheet('background-color: #C0C0C0;')
        
        self.table.itemChanged.connect(self.on_change)
        self.button_addLine.clicked.connect(self.add_row)
        self.button_removeLine.clicked.connect(self.remove_row)
        self.button_calcGPA.clicked.connect(self.calculate)

    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

    def remove_row(self):
        row_count = self.table.rowCount()
        self.table.removeRow(row_count - 1)

    def calculate(self, score):
        total_index = 0
        A = 0
        A_min = 0
        B_plus = 0
        B = 0
        B_min = 0
        C_plus = 0
        C = 0
        D = 0
        E = 0

        for row in range(0, self.table.rowCount()):
            stringscore = (self.table.item(row, 1))
            score = float(stringscore.text())

            if score >= 85:
                index = 4.00
                grade = 'A'
            elif score >= 80 and score < 85:
                index = 3.67
                grade = 'A-'
            elif score >= 75 and score < 80:
                index = 3.33
                grade = 'B+'
            elif score >= 70 and score < 75:
                index = 3.00
                grade = 'B'
            elif score >= 67 and score < 70:
                index = 2.67
                grade = 'B-'
            elif score >= 64 and score < 67:
                index = 2.33
                grade = 'C+'
            elif score >= 60 and score < 64:
                index = 2.00
                grade = 'C'
            elif score >= 55 and score < 60:
                index = 1.00
                grade = 'D'
            elif score < 55:
                index = 0.00
                grade = 'E'

            total_index += float(index * 3)
            A += (grade == 'A')
            A_min += (grade == 'A-')
            B_plus += (grade == 'B+')
            B += (grade == 'B')
            B_min += (grade == 'B-')
            C_plus += (grade == 'C+')
            C += (grade == 'C')
            D += (grade == 'D')
            E += (grade == 'E')
        
        total_credits = self.table.rowCount() * 3
        cum_GPA = float(total_index / total_credits)

        self.parent.name_input1.setText('Name: ' + self.name_input.text())
        self.parent.studentID_input1.setText('Student ID: ' + self.studentID_input.text())
        self.parent.major_input1.setText('Major: ' + self.major_combobox.currentText())
        self.parent.class_input1.setText('Class: ' + self.class_input.text())
        self.parent.batch_input1.setText('Batch: ' + self.batch_combobox.currentText())
        self.parent.result_label.setText('Result: ')
        self.parent.A_label.setText('Grade A: %d' % A)
        self.parent.A_min_label.setText('Grade A-: %d' % A_min)
        self.parent.B_plus_label.setText('Grade B+: %d' % B_plus)
        self.parent.B_label.setText('Grade B: %d' % B)
        self.parent.B_min_label.setText('Grade B-: %d' % B_min)
        self.parent.C_plus_label.setText('Grade C+: %d' % C_plus)
        self.parent.C_label.setText('Grade C: %d' % C)
        self.parent.D_label.setText('Grade D: %d' % D)
        self.parent.E_label.setText('Grade E: %d' % E)
        self.parent.totIdx_label.setText('Total Index: %.2f' % total_index)
        self.parent.totCrs_label.setText('Total Credits: %d' % total_credits)
        self.parent.totGPA_label.setText('Cumulative GPA: %.2f' % cum_GPA)
        self.close()

    def on_change(self, item):
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText('')
        elif col == 1 and (float(item.text()) <= 0 or float(item.text()) >= 100):
            item.setText('')


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()