from src.cadastro.emailValido import emailValido
from src.cadastro.nomeValido import nomeValido
from src.menu.cabecalho import cabecalho
from src.dados.usuarios import usuarioLogado
from src.dados.torneios import torneios
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.menu.limparTerminal import limparTerminal
from src.torneios.idValido import idValido
import time


def menuInscricaoTorneio():
    cabecalho("INSCRIÇÕES")

    if usuarioLogado[0]["inscrito"] != None:
        print("Você já está participando de um torneio.")
        input("Pressione <ENTER> para voltar")
        gerenciarEscolha("v", "menuInscricaoTorneio")

    else:
        print("[V] Voltar para o menu inicial")

        idTorneioEscolhido = str(input("Digite o ID do torneio que quer participar: "))
        gerenciarEscolha(idTorneioEscolhido, "menuInscricaoTorneio")
        while idValido(idTorneioEscolhido) == False:
            print("Este ID não existe.")
            idTorneioEscolhido = str(input("Digite um ID válido (ex: 1): "))
            gerenciarEscolha(idTorneioEscolhido, "menuInscricaoTorneio")

        torneioEscolhido = next((torneio for torneio in torneios if torneio["id"] == int(idTorneioEscolhido)), None)

        if torneioEscolhido["ativo"] == False:
            print("Este torneio já foi finalizado.")
            input("Pressione <ENTER> para voltar")
            gerenciarEscolha("v", "menuInscricaoTorneio")

        else:
            limparTerminal()
            print(f"Esse é um torneio que envolve {torneioEscolhido["times"]} equipes de {torneioEscolhido["jogadoras"]} jogadoras")
            print("[1] Se inscrever sozinho")
            print("[2] Se inscrever com um time completo")
            print("[V] Voltar para o menu inicial")
            escolha = str(input("O que quer fazer: "))
            if escolha == "1":
                limparTerminal()
                print("Inscrição feita com sucesso.")
                usuarioLogado[0]["inscrito"] = idTorneioEscolhido
                torneioEscolhido["usuariosInscritos"].append(usuarioLogado[0]["email"])
                input("Pressione <ENTER> para voltar")
                gerenciarEscolha("v", "menuInscricaoTorneio")
            if escolha == "2":
                limparTerminal()
                print("[V] Voltar para o menu inicial")
                print(f"{usuarioLogado[0]["nome"]} será o capitão do time.")
                print("Insira as informações das demais jogadoras.")
                timeFormado = [usuarioLogado[0]["email"]]
                for jogadora in range(int(torneioEscolhido["jogadoras"]) - 1):
                    nomeJogadora = str(input(f"Nome da {jogadora + 1}ª jogadora: "))
                    gerenciarEscolha(nomeJogadora, "menuInscricaoTorneio")
                    while nomeValido(nomeJogadora) == False:
                        nomeJogadora = str(input(f"Digite nome e sobrenome da {jogadora + 1}ª jogadora: "))
                        gerenciarEscolha(nomeJogadora, "menuInscricaoTorneio")

                    emailJogadora = str(input(f"Email da {jogadora + 1}ª jogadora: "))
                    gerenciarEscolha(emailJogadora, "menuInscricaoTorneio")
                    while emailValido(emailJogadora) == False:
                        emailJogadora = str(input(f"Digite um email válido da {jogadora + 1}ª jogadora: "))
                        gerenciarEscolha(emailJogadora, "menuInscricaoTorneio")
                    timeFormado.append(emailJogadora)
                print("Time inscrito com sucesso.")
                usuarioLogado[0]["inscrito"] = idTorneioEscolhido
                torneioEscolhido["usuariosInscritos"].append(timeFormado)
                print(f"{usuarioLogado[0]["nome"]} receberá um email avisando sobre o local do torneio")
                input("Pressione <ENTER> para voltar")
                gerenciarEscolha("v", "menuInscricaoTorneio")

            else:
                print("Escolha inválida. Tente novamente.")
                time.sleep(1)
                limparTerminal()
                menuInscricaoTorneio()