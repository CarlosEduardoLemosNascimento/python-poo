import os
os.system("cls || clear") # Limpar o terminal

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def exibir_endereco(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"

class Aluno:
    # Contrutor
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        # Atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def exibir_dados(self) -> str:
        return f"\nNome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco.exibir_endereco()} \n"
    
# Instanciar classe
aluno1 = Aluno("Marta", 22, Endereco("Rua A", 22))

print(aluno1.exibir_dados())