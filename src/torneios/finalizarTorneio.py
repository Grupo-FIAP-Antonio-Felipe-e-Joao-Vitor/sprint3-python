from src.dados.usuarios import usuarios
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.torneios.idValido import idValido
from src.dados.torneios import torneios


def finalizarTorneio():
    print('[V] Voltar para o menu inicial')
    idTorneio = str(input("Digite o ID do torneio que quer finalizar: "))
    gerenciarEscolha(idTorneio, "finalizarTorneio")
    while idValido(idTorneio) == False:
        print("ID não existe")
        idTorneio = str(input("Digite um ID válido (ex: 1): "))
        gerenciarEscolha(idTorneio, "finalizarTorneio")

    torneioEscolhido = torneios[int(idTorneio) - 1]
    if torneioEscolhido["ativo"] == False:
        print("Esse torneio já foi finalizado.")
        input("Pressione <ENTER> para voltar")
        gerenciarEscolha("v", "finalizarTorneio")
    if torneioEscolhido["ativo"] == True:
        print("Torneio finalizado com sucesso.")
        torneioEscolhido["ativo"] = False
        for usuario in usuarios:
            if usuario["inscrito"] == idTorneio:
                usuario["inscrito"] = None
            else:
                usuario["inscrito"] = usuario["inscrito"]

        input("Pressione <ENTER> para voltar")
        gerenciarEscolha("v", "finalizarTorneio")