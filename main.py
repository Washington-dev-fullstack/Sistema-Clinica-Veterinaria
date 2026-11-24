from abc import ABC, abstractmethod
import os

class Animal(ABC):
    def __init__(self, nome, especie):
        self.nome = nome
        self._especie = especie

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome do animal não pode ser vazio ou apenas espaços")
        self._nome = valor

    @property
    def especie(self):
        return self._especie

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome, "Cachorro")

    def emitir_som(self):
        return f"{self.nome} está emitindo som: Au au!"

class Gato(Animal):
    def __init__(self, nome: str):
        super().__init__(nome, "Gato")

    def emitir_som(self):
        return f"{self.nome} está emitindo som: Miau!"

class Passaro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome, "Pássaro")

    def emitir_som(self):
        return f"{self.nome} está emitindo som: Piu piu!"

class Consulta:
    def __init__(self, animal: Animal, veterinario: str, data: str):
        if not isinstance(animal, Animal):
            raise TypeError("O parâmetro 'animal' precisa ser uma instância de uma classe derivada de Animal.")

        self._animal = animal
        self.veterinario = veterinario
        self._data = data

    @property
    def animal(self):
        return self._animal

    @property
    def veterinario(self):
        return self._veterinario

    @veterinario.setter
    def veterinario(self, valor):
        if not valor.strip():
            raise ValueError("O nome do veterinário não pode ser vazio.")
        self._veterinario = valor

    @property
    def data(self):
        return self._data

    def realizar(self):
        print("\n" + "="*40)
        print("      RESUMO DA CONSULTA MÉDICA      ")
        print("="*40)
        print(f"Data da Consulta: {self.data}")
        print(f"Veterinário(a)  : {self.veterinario}")
        print(f"Paciente        : {self.animal.nome} ({self.animal.especie})")
        print(f"Som do Paciente : {self.animal.emitir_som()}")
        print("="*40)

if __name__ == "__main__":
    lista_animais = []
    lista_consultas = []

    while True:
        print("-"*30)
        print("      MENU DA CLÍNICA      ")
        print("-"*30)
        print("1. Cadastrar Novo Animal")
        print("2. Agendar Consulta")
        print("3. Exibir Resumo de Todas as Consultas")
        print("4. Sair do Sistema")
        print("-"*30)
        
        try:
            opcao = int(input("\nInsira o número correspondente a sua escolha: "))
            os.system("clear")
        except ValueError:
            os.system("clear")
            print("É nescessário que insira um número válido (1, 2, 3 ou 4).\n")
            continue

        if opcao == 1:
            print("Qual é a espécie do animal?")
            print("1. Cachorro")
            print("2. Gato")
            print("3. Pássaro")
            tipo = input("\nEscolha a espécie (1/2/3): ")
            nome = input("Qual o nome do animal? ")
            os.system("clear")

            try:
                if tipo == '1':
                    novo_animal = Cachorro(nome)
                elif tipo == '2':
                    novo_animal = Gato(nome)
                elif tipo == '3':
                    novo_animal = Passaro(nome)
                else:
                    print("Opção de espécie inválida!")
                    continue

                lista_animais.append(novo_animal)
                print(f"{novo_animal.especie} '{novo_animal.nome}' cadastrado com sucesso!\n")
            
            except ValueError as e:
                print(f"Erro ao cadastrar: {e}")

        elif opcao == 2:
            if not lista_animais:
                print("Não tem animais cadastrados. Por favor, cadastre um animal primeiro (Opção 1).")
                continue

            print("--- Escolha o Paciente ---")
            for i, animal in enumerate(lista_animais):
                # Mostramos i + 1 para a lista começar em 1 na tela (mais amigável para o usuário)
                print(f"{i + 1}. {animal.nome} ({animal.especie})")

            try:
                # Subtraímos 1 para voltar ao índice real da lista (que começa em 0)
                escolha_animal = int(input("\nDigite o número do paciente: ")) - 1
                
                if 0 <= escolha_animal < len(lista_animais):
                    paciente_selecionado = lista_animais[escolha_animal]
                    vet = input("Nome do(a) Veterinário(a): ")
                    data = input("Data da consulta (ex: 20/05/2026): ")
                    os.system("clear")

                    nova_consulta = Consulta(paciente_selecionado, vet, data)
                    lista_consultas.append(nova_consulta)
                    print("Consulta agendada com sucesso!\n")
                else:
                    print("Número de paciente inválido.\n")
            
            except (ValueError, TypeError) as e:
                print(f"Erro ao agendar: {e}")

        elif opcao == 3:
            if not lista_consultas:
                print("Nenhuma consulta agendada ainda.\n")
            else:
                for consulta in lista_consultas:
                    consulta.realizar()

        elif opcao == 4:
            print("Saindo do sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.\n")