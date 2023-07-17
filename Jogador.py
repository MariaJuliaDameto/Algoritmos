class Jogador:
    def __init__(self, nome, numeroCamisa):
        self.nome = nome
        self.numero_camisa = numeroCamisa
        self.__posicao = None
        self.proximoJogador = None

    def get_posicao(self):
        return self.__posicao

    def set_posicao(self, posicao):
        self.__posicao = posicao
    
