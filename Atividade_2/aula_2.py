class Artigos:
    def __init__(self,autor,titulo):
        self.autor = autor
        self.titulo = titulo
        
    def __str__(self):
        return "Autor: " + autor + " Titulo: " + titulo 

class Autor(Pessoa):
    def __init__(self,evento,nome,email):
        super().__init__(evento,nome,email)
        

class PessoaFisica(Pessoa):
    pass

class PessoaJuridica(Pessoa):
    pass

class Pessoa:
    def __init__(self,evento,nome,email):
        self.evento = evento
        self.nome = nome
        self.email = email

    def __str__(self):
        return "Evento: " + evento + " NomePessoa: " \
        + nome + " Email: " + email

class evento:
    def __init__(self,nome,data_inicio,data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __str__(self):
        return "NomeEvento: " + nome + \
               " DataInicio: " + data_inicio + " DataFim: " + data_fim
