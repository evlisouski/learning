class Graph:
    def __init__(self, data):
        self.data = data
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(" ".join(str(x) for x in self.data))


    def show_graph(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(f"Графическое отображение данных: {' '.join(str(x) for x in self.data)}")

    def show_bar(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(f"Столбчатая диаграмма: {' '.join(str(x) for x in self.data)}")

    def set_show(self, fl_show):
        self.is_show = fl_show


input_row = "8 11 10 -32 0 7 18"
data_graph = list(map(int, input_row.split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()
print(gr.data)
input_row = "8 11 10 -32 0 7 5"
data_graph = list(map(int, input_row.split()))
gr2 = Graph(data_graph)
print(gr2.data)
print(gr.data)
