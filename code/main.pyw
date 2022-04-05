from PyQt5 import QtWidgets, QtGui, QtCore
from solver import solve
from sympy import Matrix


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # инитиализация надписей
        self.labelList = (
            QtWidgets.QLabel('Начальное состояние системы:'),
            QtWidgets.QLabel('Конечное состояние системы:'),
            QtWidgets.QLabel('Промежутки времени:'),
        )
        self.setSettingsToLabel()

        # инитиализация полей ввода
        self.lineEditList = tuple([QtWidgets.QLineEdit() for _ in range(3)])
        self.setSettingsToLineEdit()

        # инитиализация менеджера компоновки
        self.form = QtWidgets.QFormLayout()
        self.form.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)

        self.addToWidgetsLayout()
        self.setLayout(self.form)

    def event(self, e):
        """
        Функция унаследованная у QWidget. 
        Отвечает за обратку событий поступающих от пользователя
        собственная реализация написана только для enter.
        :param e: event - событие поступающее от пользователя.
        :no return:
        """
        if e.type() == QtCore.QEvent.KeyPress:
            if e.key() == QtCore.Qt.Key_Return and self.isParamsCorrect():
                self.startSolve()
            elif e.key() == QtCore.Qt.Key_Return and not self.isParamsCorrect():
                print('Введённые параметры некорректны')
        return QtWidgets.QWidget.event(self, e)

    def setSettingsToLabel(self):
        """
        Добавление некоторых свойств к надписям.
        Вынесено в отдельную функцию, чтобы не засорять init.
        :no return:
        """
        for label in self.labelList:
            label.setFont(QtGui.QFont('Times', 10))  # Установка размера и стиля шрифта

    def setSettingsToLineEdit(self):
        """
        Добавление некоторых свойств к однострочным полям ввода.
        Вынесено в отдельную функцию, чтобы не засорять init.
        :no return:
        """
        for lineEdit in self.lineEditList:
            lineEdit.setInputMask("Вектор: 9,9,9,9;_")  # Установка маски ввода

    def addToWidgetsLayout(self):
        """
        Добавляет все компонненты в Layout(Компновщик, используется FormLayout)
            для оформления в виде (надпись - текстовое поле).
        Также добавляет информационную надпись (корректные данные или нет).
        :no return:
        """
        # Добавление конструкций формата(надпись - текстовое поле)
        for label, lineEdit in zip(self.labelList, self.lineEditList):
            self.form.addRow(label, lineEdit)

    def getText(self):
        """
        Собирает данные из полей ввода и добавляет их в список. При добавлении проверяет являются корректными.
        :return: param_list - список параметров полученных из LineEdit(однострочные поля ввода)
        """
        param_list = []
        for lineEdit in self.lineEditList:
            if lineEdit.hasAcceptableInput():
                param_list.append(lineEdit.text())
        return param_list

    def isParamsCorrect(self):
        """
        Проверяет явлюятся ли параметры корректными
        (Если параметр является некорректным, то он в param_list не добавляется)
        :return: bool значение.
        """
        return len(self.getText()) == 3

    def startSolve(self):
        """
        Передаёт параметры в solver.py по нажатию enter и сразу вызывает функцию solve
        solve - главная фунция решателя.
        :no return:
        """
        data = self.paramsToNums()
        x0, xT, times_num = self.parse_input_args(data)
        solve(x0, xT, times_num)

    def parse_input_args(self, data):
        vectors, times = data[0:2], data[2]
        x0 = Matrix(vectors[0])
        xT = Matrix(vectors[1])
        return x0, xT, times

    def paramsToNums(self):
        """
        Переводит строковое представление параметров в численное, сразу готовое к использованию.
        Это происходит здесь, чтобы solver.py  не тратил на это время.
        :return: num_data - список параметров переведённый в List(int) и просто int зависимости от поставленной задачи
        """
        num_data = []
        data = self.getText()
        for row in data:
            num_data.append(eval(row[8:]))
        return num_data


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Python Application")
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec_())
