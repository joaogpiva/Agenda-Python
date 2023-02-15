class Compromisso():
    def __init__(self, data, hora, duracao, descricao):
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.descricao = descricao
    
    def imprimir(self):
        result = ""
        result += f"Data: {self.data}\n"
        result += f"Hora: {self.hora}\n"
        result += f"Duração: {self.duracao} horas\n"
        result += f"Descrição: {self.descricao}\n"

        return result

agenda = []

def addCompromisso():
    c = Compromisso(input("Digite a data: "), 
                    input("Digite o horário: "), 
                    input("Digite a duração (em horas): "), 
                    input("Forneça uma descrição do evento: "))

    for compromisso in agenda:
        if compromisso.data == c.data and compromisso.hora == c.hora:
            print("Essa data e horário já estão reservados para um compromisso existente.")
            return
    
    agenda.append(c)
    print("\nCompromisso adicionado!")

def listCompromisso():
    result = ""
    for c in agenda:
        result += c.imprimir() + "\n"

    if result == "":
        print("Agenda Vazia")
    else:
        print(result)

print("I==========I")
print("I  Agenda  I")
print("I==========I")

while True:
    print("\n")
    print("1 - Adicionar novo compromisso")
    print("2 - Consultar compromisso")
    print("3 - Atualizar compromisso")
    print("4 - Excluir compromisso")
    print("5 - Listar todos")
    print("6 - Sair\n")

    op = input("Selecione uma opção: ")

    match op:
        case "1":
            addCompromisso()
        case "2":
            getCompromisso()
        case "3":
            updateCompromisso()
        case "4":
            deleteCompromisso()
        case "5":
            listCompromisso()
        case "6":
            print("Finalizando...")
            break
        case other:
            print("Opção inválida!")
