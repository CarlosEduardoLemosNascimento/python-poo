from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final

# Instanciar classes
#funcionário1 = Funcionario("José", 25, 1500)
#print(f"Nome: {funcionário1.nome}")

gerente1 = Gerente("Jorge", 35, 1000)
print(f"Nome: {gerente1.nome}")
print(f"Salário: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Pedro", 35, 1000, "123123")
print(f"Nome: {motoboy1.nome}")
print(f"Salário: {motoboy1.calcular_salario()}")