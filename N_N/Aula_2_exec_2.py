from aula_2_2 import *

p = Projeto("Projeto 1", "15-02-2019", "31-12-2019")
print(p.nome)
p.nome = "Teste"                                                #SET
print("Após o Teste: ", p.nome, "\n")                           #GET

pe = Pessoa("Mateus", "23-02-2000")

a = Atividade("Atividade 1", 1, pe,"17-02-2019", "19-02-2019")
print("Nome da pessoa da Atividade 1: ", a.pessoa.nome)                   
print("Status: ", a.status)                                     #Imprime "Ativa"
a.finalizar_atividade()                                        #Imprime "Finalizada!"
print("Status: ", a.status)                                     #Imprime "Finalizada!"
print("Pessoa: ", a.pessoa)                                     #Imprime retorna o __str__

print("\n")
pa = Projeto_Atividade(p, a)
print(pa.atividade.nome)
