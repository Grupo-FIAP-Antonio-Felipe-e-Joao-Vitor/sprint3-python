from src.menu.limparTerminal import limparTerminal

import time

def gerenciarEscolha(escolha, menu):
    if menu == "menuInicial":
        match escolha.lower():
            case "1":
                from src.menu.menuCadastro import menuCadastro
                limparTerminal()
                menuCadastro()
            case "2":
                from src.menu.menuEntrar import menuEntrar
                limparTerminal()
                menuEntrar()
            case "q":
                limparTerminal()
                print("Saindo do sistema...")
                time.sleep(1)
                print("Saiu.")
                quit()
            case _:
                print("Escolha inválida. Tente novamente.")
                time.sleep(1)
                limparTerminal()
                from src.menu.menuInicial import menuInicial
                menuInicial()

    if menu == "menuCadastro":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.menuInicial import menuInicial
                menuInicial()
    if menu == "menuEntrar":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.menuInicial import menuInicial
                menuInicial()
    if menu == "menuPrincipal":
        match escolha.lower():
            case "1":
                limparTerminal()
                from src.menu.menuTorneios import menuTorneios
                menuTorneios()
            case "2":
                limparTerminal()
                from src.menu.verPerfil import verPerfil
                verPerfil()
            case "q":
                confirmar = str(input("Tem certeza de que deseja sair? [S/N]: "))
                if confirmar.lower() == "s":
                    limparTerminal()
                    from src.menu.menuEntrar import usuarioLogado
                    usuarioLogado.pop()
                    from src.menu.menuInicial import menuInicial
                    menuInicial()
                else:
                    limparTerminal()
                    from src.menu.menuPrincipal import menuPrincipal
                    menuPrincipal()
            case _:
                print("Escolha inválida. Tente novamente.")
                time.sleep(1)
                limparTerminal()
                from src.menu.menuPrincipal import menuPrincipal
                menuPrincipal()
    if menu == "painelADM":
        match escolha.lower():
            case "1":
                limparTerminal()
                from src.menu.mostrarUsuarios import mostrarUsuarios
                mostrarUsuarios()
            case "2":
                limparTerminal()
                from src.menu.gerenciarTorneios import gerenciarTorneios
                gerenciarTorneios()
            case "q":
                confirmar = str(input("Tem certeza de que deseja sair? [S/N]: "))
                if confirmar.lower() == "s":
                    limparTerminal()
                    from src.menu.menuEntrar import usuarioLogado
                    usuarioLogado.pop()
                    from src.menu.menuInicial import menuInicial
                    menuInicial()
                else:
                    limparTerminal()
                    from src.menu.menuPrincipal import menuPrincipal
                    menuPrincipal()
            case _:
                print("Escolha inválida. Tente novamente.")
                time.sleep(1)
                limparTerminal()
                from src.menu.menuPrincipal import menuPrincipal
                menuPrincipal()
    if menu == "mostrarUsuarios":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.menuPrincipal import menuPrincipal
                menuPrincipal()

    if menu == "verPerfil":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.menuPrincipal import menuPrincipal
                menuPrincipal()
    if menu == "gerenciarTorneios":
        match escolha.lower():
            case "1":
                limparTerminal()
                from src.torneios.mostrarTorneios import mostrarTorneios
                mostrarTorneios(True)
            case "2":
                limparTerminal()
                from src.torneios.criarTorneios import criarTorneios
                criarTorneios()
            case "v":
                limparTerminal()
                from src.menu.menuPrincipal import menuPrincipal
                menuPrincipal()
            case _:
                print("Escolha inválida. Tente novamente.")
                time.sleep(1)
                limparTerminal()
                from src.menu.gerenciarTorneios import gerenciarTorneios
                gerenciarTorneios()
    if menu == "criarTorneios":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.gerenciarTorneios import gerenciarTorneios
                gerenciarTorneios()
    if menu == "mostrarTorneiosADM":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.gerenciarTorneios import gerenciarTorneios
                gerenciarTorneios()
    if menu == "mostrarTorneiosUSER":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.menuTorneios import menuTorneios
                menuTorneios()
    if menu == "menuTorneios":
        match escolha.lower():
            case "1":
                limparTerminal()
                from src.torneios.mostrarTorneios import mostrarTorneios
                mostrarTorneios()
            case "2":
                limparTerminal()
                from src.torneios.menuInscricaoTorneio import menuInscricaoTorneio
                menuInscricaoTorneio()
            case "v":
                limparTerminal()
                from src.menu.menuPrincipal import menuPrincipal
                menuPrincipal()
            case _:
                print("Escolha inválida. Tente novamente.")
                time.sleep(1)
                limparTerminal()
                from src.menu.menuTorneios import menuTorneios
                menuTorneios()
    if menu == "menuInscricaoTorneio":
        match escolha.lower():
            case "v":
                limparTerminal()
                from src.menu.menuTorneios import menuTorneios
                menuTorneios()