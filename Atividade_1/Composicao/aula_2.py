class Projeto:
    def __init__(self,nome,data_inicio,data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim

class Pessoa:
    def __init__(self,nome,data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc

    def __str__(self):
        return "Pessoa: " + self.nome + "DataNasc: " + self.data_nasc

class Atividade:
    status = "ativa"                        #Instância de Classe
    
    def __init__(self, nome, prioridade, pessoa, projeto, data_inicio, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.pessoa = pessoa                #FK
        self.projeto = projeto              #FK
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def finalizar_atividade(self):
        self.status = "Finalizada!"







    
