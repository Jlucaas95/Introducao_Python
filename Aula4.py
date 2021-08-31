a = int(input('Digite a nota do primeiro bimestre: '))
while a > 10 or a < 0:
    a = int(input('Voce digitou errado a nota do primeiro bimestre '))
b = int(input('Digite a nota do segundo bimestre: '))
while b > 10:
        b = int(input('Voce digitou errado a nota do primeiro bimestre '))
c = int(input('Digite a nota do terceiro bimestre: '))
while c > 10:
        c = int(input('Voce digitou errado a nota do terceiro bimestre '))
d = int(input('Digite a nota do quarto bimestre: '))
while d > 10:
        d = int(input('Voce digitou errado a nota do quarto bimestre '))

media = (a + b + c + d) / 4
print('media:  {}'.format(media))


























# while nota > 10:
#     nota = int(input('Entre com a nota'))
#     nota = int(input('Nota inválida.Entre com a nota correta'))
#     print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a += 1











# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for  x in range (1, num+1):
#             resto = num % x
#             #print(x, resto)
#             if resto == 0:
#                 div +=1
#     if div ==2:
#         print(num)
