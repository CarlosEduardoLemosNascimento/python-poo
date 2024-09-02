import os

# Limpar o terminal
os.system("cls || clear")

class Livro:
    #Contrutor
    def __init__(self, titulo: str, autor: str, numeroDePaginas: int, preco:float ) -> None:
        pass
        #Atributos
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"Título: {self.titulo} \nAutor: {self.autor} \nNº de Páginas: {self.numeroDePaginas} \nPreço: {self.preco}"

#instanciar classe
livro1 = Livro("Título do livro 1", "Autor do livro 1", 100, 10.90)
livro2 = Livro("Título do livro 2", "Autor do livro 2", 200, 20.90)

print(livro1.exibir_dados())
print()
print(livro2.exibir_dados())
