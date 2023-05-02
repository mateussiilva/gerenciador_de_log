from main import (
    parse_html,organizar_impressao,
    informacoes_uteis)
from tkinter import Tk,mainloop,Label
from setings import HEIGHT,WIDTH


class Window:
    def __init__(self) -> None:
        self.__root = Tk()
        # configurações da janela
        self.__root.title("Gerenciador de LOG")
        self.__root.geometry(f"{WIDTH}x{HEIGHT}")
        self.__root.mainloop()
        

if __name__ == "__main__":
    janela = Window()