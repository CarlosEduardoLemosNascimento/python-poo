from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep \nCidade: {self.cidade}}"

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        BONIFICACAO = 1.1
        salario_final = self.salario
        return salario_final
    
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        salario_final = self.salario
        return salario_final

engenheiro1 = Engenheiro("")
print(f"Nome: {gerente1.nome}")
print(f"Salário: {gerente1.calcular_salario()}")