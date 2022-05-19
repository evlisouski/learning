def func2():
    try:
      return 1 / 0
    except:
        print("func2 error")



def func1():
    try:
        return func2()
    except:
        print("func1 error")


func1()
# обрабатывать ошибки можно на любом уровне
