def exibir_menu(titulo:str, opcoes:dict):
    """
    titulo: string
    opcoes: dict -> {numero: (descricao, funcao)}
    """
    while True:
        print("\n" + "=" * 40)
        print(f"{titulo: ^40}",)
        print("=" * 40)

        for numero, (descricao, _) in opcoes.items():
            print(f"{numero} - {descricao}")

        print("0 - Voltar")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "0":
            break

        if escolha.isdigit() and int(escolha) in opcoes:
            _, funcao = opcoes[int(escolha)]
            funcao()
        else:
            print("Opção inválida.")