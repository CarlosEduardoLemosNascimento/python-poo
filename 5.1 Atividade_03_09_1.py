from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nENDEREÇO"
                f"\nLogradouro: {self.logradouro}" 
                f"\nNúmero: {self.numero}"
                f"\nCidade: {self.cidade}"
                    )

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}" 
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"\nEndereço: {self.endereco}"
                    )

class Engenheiro(Funcionario):
    def __init__(self, nome: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        salario_final = 1000
        return salario_final
    
      
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        salario_final = 1000
        return salario_final

# Instanciando classes
engenheiro1 = Engenheiro("Jorge", "71 9999-9999", "jorge@provedor.com", "1234",
                         Endereco("Rua A", 123, "casa", "40.000-000", "Salvador"))
print("\n=== DADOS DO ENGENHEIRO ===")
print(engenheiro1)

medico1 = Medico("Jorge", "71 9999-9999", "jorge@provedor.com", "1234",
                         Endereco("Rua A", 123, "casa", "40.000-000", "Salvador"))
print("\n=== DADOS DO MEDICO ===")
print(medico1)