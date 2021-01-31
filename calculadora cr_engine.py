import materias

ra = []
busca = 0
agrupamento = {}
nota = 0


def MenuPrincipal(materia):
    print("[1]: Adicionar RA | [2]: Consultar RA | [3]: Relatório das matérias | [0]: Sair")

    menu = int(input())

    if menu >= 4 or menu < 0:
        print("vai toma no seu cu filha da putinha")
        for x in range(1000):
            print("te conheço nessa porra?")

    if menu == 1:
        print("Digite seu RA:")
        ra.append(int(input()))
        print("Novo RA cadastrado com sucesso!")
        MenuPrincipal(1)


    elif menu == 2:
        print("Digite seu RA:")
        busca = int(input())
        for i in range(0, len(ra), 1):
            if busca == ra[i]:
                SegundoMenuCompleto(i)

            elif i == len(ra) - 1:
                print("RA não encontrado")
                MenuPrincipal(1)


    elif menu == 3:
        for i in range(len(materias.materia)):
            print(f"materia: {materias.materia[i]} /// num de creditos: {materias.creditos[i]}")
            MenuPrincipal(1)


def SegundoMenuCompleto(i):
    print(" [1]: Adicionar Matéria | [2]: Deletar Matéria | [3]: Listar matérias cursadas"
          "\n[4]: Listar matérias restantes | [5]: Calcular CR | [6]: Relatório das matérias | [0]: Sair")

    opcao = int(input())

    if opcao == 1:
        print("qual matéria deseja adicionar no seu RA?(CASO DESEJE VOLTAR E VER OS CODIGOS DE MATERIAS DIGITE 55")
        materia = input()
        print("qual nota vc tirou na materia? de 0 a 5 sendo A = 5 e F = 0")
        nota = input()

        if materia == "55":
            for i in range(len(materias.materia)):
                print(f"materia: {materias.materia[i]} /// num de creditos: {materias.creditos[i]}")
        else:

            print(materias.chaves.get(input().upper(materia)))
            agrupamento = {
                ra[i]: [materia, nota]


            }

  #  elif opcao == 2:
   # elif opcao == 3:
    #elif opcao == 4:
    #elif opcao == 5:
    #elif opcao == 6:
