class Viber:
    messages = {}

    @classmethod
    def add_message(cls, msg):
        cls.messages[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.messages.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        if id(msg) in cls.messages:
            obj = cls.messages.get(id(msg))
            obj.fl_like = False if obj.fl_like is True else True

    @classmethod
    def show_last_message(cls, number):
        messages_text = []
        for key, val in cls.messages:
            messages_text.append(val.text)
        for i in range(number):
            print(messages_text[-i])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)

class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.total_messages()