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