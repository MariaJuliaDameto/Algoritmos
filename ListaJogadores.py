from Jogador import Jogador

class ListaJogadores:
    def __init__(self):
        self.raiz = None

    def adicionar_jogador(self, jogador):
        novo_jogador = Jogador(jogador.nome, jogador.numeroCamisa)
        novo_jogador.set_posicao(jogador.get_posicao())

        if self.raiz == None:
            self.raiz = novo_jogador
        else:
            jogador_atual = self.raiz
            jogador_anterior = None

            while jogador_atual != None and jogador_atual.numero_camisa < novo_jogador.numero_camisa:
                jogador_anterior = jogador_atual
                jogador_atual = jogador_atual.proximoJogador

            if jogador_anterior == None:
                novo_jogador.proximoJogador = self.raiz
                self.raiz = novo_jogador
            else:
                novo_jogador.proximoJogador = jogador_atual
                jogador_anterior.proximoJogador = novo_jogador

    def remover_jogador(self, numero_camisa):
        jogador_atual = self.raiz
        jogador_anterior = None

        while jogador_atual != None and jogador_atual.numero_camisa != numero_camisa:
            jogador_anterior = jogador_atual
            jogador_atual = jogador_atual.proximoJogador

        if jogador_atual == None:
            return False
        else:
            if jogador_anterior == None:
                self.raiz = jogador_atual.proximoJogador
            else:
                jogador_anterior.proximoJogador = jogador_atual.proximoJogador

            return True
        
    def buscarJogador(self, numero_camisa):
        jogador_atual = self.raiz

        while jogador_atual != None and jogador_atual.numero_camisa != numero_camisa:
            jogador_atual = jogador_atual.proximoJogador

        if jogador_atual == None:
            return None
        else:
            return jogador_atual
        
    def imprimirJogadores(self):
        jogador_atual = self.raiz

        while jogador_atual != None:
            print("Nome: " + jogador_atual.nome + " - Número da camisa: " + str(jogador_atual.numero_camisa) + " - Posição: " + jogador_atual.get_posicao())
            jogador_atual = jogador_atual.proximoJogador

    def imprimirJogadoresPosicao(self, posicao):
        jogador_atual = self.raiz

        while jogador_atual != None:
            if jogador_atual.get_posicao() == posicao:
                print("Nome: " + jogador_atual.nome + " - Número da camisa: " + str(jogador_atual.numero_camisa) + " - Posição: " + jogador_atual.get_posicao())
            jogador_atual = jogador_atual.proximoJogador

