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
                pass
            case "2":
                pass
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
                pass
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