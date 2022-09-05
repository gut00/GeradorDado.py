from cProfile import run
from logging import exception
import random

class simuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem ='deseja jogar o dado?. '
        
    def Iniciar(self):
        try:
            resposta = input(self.mensagem)
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDado()
            elif resposta == 'não' or resposta == 'n':
                print('até a proxima')
            else:
                print('você deve digitar sim ou não')
        except:
            print('ocorreu um erro ao receber sua rsposta')

    def GerarValorDado(self):  
        print('o dado caiu com o numero',random.randint(self.valor_minimo, self.valor_maximo),'para cima')

simulador = simuladorDado()
simulador.Iniciar()
    