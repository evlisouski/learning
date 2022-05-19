# Инструкция raise специально вызывает исключение

# raise ZeroDivisionError("Деление на ноль")

# e = ZeroDivisionError("Деление на ноль")
# raise e


class ExceptionPrint(Exception):
    """Общий класс наследования для демонстрации возможности иерархии наследования"""


class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтера"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):  # переопределение метода __str__ для отображения ошибки в консоли
        return f"Ошибка: {self.message}"


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")

    def send_to_print(self, data):
        return False


p = PrintData()
# p.print("123")
try:
    p.print("123")
except ExceptionPrintSendData:
    print("Принтер не отвечает")
except ExceptionPrint:
    print("Общая ошибка печати")
else:
    print("Печать")
