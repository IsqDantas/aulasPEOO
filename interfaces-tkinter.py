import tkinter as tk


class MinhaApp(tk.Frame):
    def __init__(self, master=None):
        self.counter = 1
        self.fonte_padrao = "Verdana 10 italic bold"
        tk.Frame.__init__(self, master)

        self.msg = tk.Label(self, text="Lista TODO", font=self.fonte_padrao)
        self.msg.pack()

        entry_container = tk.Frame(self.master)
        entry_container["padx"] = 12
        entry_container["pady"] = 4
        entry_container.pack()

        self.entry_task_name = tk.Entry(entry_container, width=40)
        self.entry_task_name.pack()

        self.button_task_name = tk.Button(entry_container, text="", command=self.__adicionar_tarefa())

        self.pack()

    def __adicionar_tarefa(self):
        container = tk.Frame(self.master)
        container["padx"] = 12
        container["pady"] = 4
        container.pack()

        botao_feito = tk.Button(container, text="OK", command=self.__excluir_tarefa)
        item_todo = tk.Label(container, text="", font=self.fonte_padrao)

    def __excluir_tarefa(self):
        pass




def main():
    app = MinhaApp()
    app.master.title('Esse é o título da minha aplicação!')
    app.master.geometry('600x600')
    app.master.minsize(width=600, height=600)
    app.master.maxsize(width=800, height=800)
    app.mainloop()


if __name__ == '__main__':
    main()
