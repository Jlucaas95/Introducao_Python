from Aula7televisao import Televisao
from Aula7calculadora1 import Calculadora
from Aula8_contadorpalavras import contador_letras
if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra de lista: {}'.format(total_letras))