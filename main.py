from Jogador import Jogador
from ListaJogadores import ListaJogadores

def main():
    def imprimirMenu():
        print("1 - Adicionar jogador")
        print("2 - Remover jogador")
        print("3 - Buscar jogador")
        print("4 - Imprimir jogadores")
        print("5 - Sair")
        print()

    def adicionarJogador():
        nome = input("Digite o nome do jogador: ")
        numero_camisa = int(input("Digite o número da camisa do jogador: "))
        posicao = input("Digite a posição do jogador: ")

        jogador = Jogador(nome, numero_camisa)
        jogador.set_posicao(posicao)

        lista.adicionar_jogador(jogador)

    def removerJogador():   
        numero_camisa = int(input("Digite o número da camisa do jogador: "))

        if lista.remover_jogador(numero_camisa):
            print("Jogador removido com sucesso!")
        else:
            print("Jogador não encontrado!")

    def buscarJogador():
        numero_camisa = int(input("Digite o número da camisa do jogador: "))

        jogador = lista.buscarJogador(numero_camisa)

        if jogador == None:
            print("Jogador não encontrado!")
        else:
            print("Nome: " + jogador.nome + " - Número da camisa: " + str(jogador.numero_camisa) + " - Posição: " + jogador.get_posicao())

    def imprimirJogadores():
        lista.imprimirJogadores()

    lista = ListaJogadores()

    while True:
        imprimirMenu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionarJogador()
        elif opcao == 2:
            removerJogador()
        elif opcao == 3:
            buscarJogador()
        elif opcao == 4:
            imprimirJogadores()
        elif opcao == 5:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
