from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + " " + digits

    @staticmethod
    def check_card_number(number):
        sample = "XXXX-XXXX-XXXX-XXXX"
        count = -1
        if len(number) != len(sample):
            return False
        else:
            for i in sample:
                count += 1
                if i is "X":
                    if number[count] in digits:
                        pass
                    else:
                        return False
                if i is "-":
                    if number[count] is "-":
                        pass
                    else:
                        return False
        return True

    @classmethod
    def check_name(cls, name):
        if len(name.split()) != 2:
            return False
        else:
            for i in name:
                if i in cls.CHARS_FOR_NAME:
                    pass
                else:
                    return False
        return True

