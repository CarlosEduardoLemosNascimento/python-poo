import os
from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, id:int, nome:str, idade:int, salario:float, setor:Setor, sexo:Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
    
    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNOME: {self.nome}"
                f"\nIDADE: {self.idade}"
                f"\nSALÁRIO: {self.salario}"
                f"\nSETOR: {self.setor.value}"
                f"\nSEXO: {self.sexo.value}"
        )

# Instanciando

os.system("cls || clear")

funcionario_1 = Funcionario(1, "João", 22, 1000, Setor.FINANCEIRO, Sexo.MASCULINO)

print(funcionario_1)