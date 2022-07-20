"""
Voce deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que deverá incrementar a velocidade em uma unidade
3) Metodo frear que devera decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor da direção com valores possiveis: Norte, Sul, Leste, Oeste
2) metodo girar para direita
3) metodo girar para esquerda

  N
O   L
  S

    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade()
    1
    >>> motor.acelerar()
    >>> motor.velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()]
    >>> 'norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'sul'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'leste'
"""
NORTE = 'norte'
SUL = 'sul'
LESTE = 'leste'
OESTE = 'oeste'
class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self, velocidade):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self, direcao):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

class Direcao:
    def __init__(self):
        self.valor = 'norte'
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, velocidade):
        self.velocidade = velocidade + 1

    def frear(self, velocidade):
        if (velocidade > 2):
            self.velocidade = velocidade - 2
        else:
            self.velocidade = 0


def __init__(self, direcao, motor):
    self.direcao = direcao
    self.motor = motor

if __name__=='__main__':
  Carro.acelerar()