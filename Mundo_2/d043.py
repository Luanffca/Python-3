# Desafio 043 
'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 
PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- À vista dinheiro/cheque: 10% desconto
- À vista no cartão: 5% de desconto.
- em até 2x no cartão: preço normal.
- 3X  ou mais no cartão 20% de juros.'''

produto = float(input("Qual o valor do produto: R$ "))
print('-='*30)
print(" ESCOLHA A FORMA DE PAGAMENTO.\n 1 - À vista dinheiro/cheque: 10% desconto. \n 2 - À vista no cartão: 5% de desconto.\n 3 - Em até 2x no cartão: preço normal.\n 4 - 3X  ou mais no cartão 20% de juros.")
print('-='*30)
pagamento = int(input("Digite o número que corresponde a forma de pagamento. "))
print('-='*30)
if pagamento == 1:
    avista = produto - produto * (10 / 100)
    print("Você ganhou 10% de desconto por pagar à vista.\n Valor do produto R$ {:.1f}.".format(avista))
elif pagamento == 2:
    cartao_avista = produto - produto * (5 / 100)
    print("Você ganhou 5% de desconsto por pagar á vista no cartão.\n Valor do produto R$ {:.1f}.".format(cartao_avista))
elif pagamento == 3:
    print("Você irá pagar o preço normal do produto.\n Valor do produto R$ {:.1f}.".format(produto))
elif pagamento == 4:
    tresmais = produto + produto * (20 / 100)
    print("Você vai pagar 20% a mais de juros por ter esconhedo a forma de pagameto 4.\n Valor do produto R$ {:.1f}".format(tresmais))
else:
    print("Opção Invalida. Tente Novamente.")