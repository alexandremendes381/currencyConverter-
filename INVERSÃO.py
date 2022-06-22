
from time import sleep
import requests
import json
continuar = True
while continuar == True:


    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = cotacao.json()
    cotacao_do_dolar = cotacao['USDBRL']['bid']
    cotacao_do_euro = cotacao['EURBRL']['bid']
    cotacao_do_bitcoin = cotacao['BTCBRL']['bid']
    sleep(0.5)
    print('\033[32;40m''COTAÇÕES NO MOMENTO EXATO''\033[m ')

    sleep(1)
    menu = """
    1 -> Cotação reais para dollar 
    2 -> Cotação dolar para reais
    3 -> Cotação reias para euro
    4 -> Cotação euro para reais
    5 -> Cotação reais para bitcoin
    6 -> Cotação bitcoin para reais
    """

    print(menu)

    sleep(0.5)
    opicao = int(input('Qual a opção desejada ? '))
    if opicao >= 7:
        print('\033[31;40m''opção invalida''\033[m')
        exit(opicao)

    valor = float(input('qual valor gostaria de cotar em reais ? '))
    sleep(1)
    if opicao == 1:
        print('opção escolhida COTAÇÃO REAIS PARA DOLAR')
        valores_1 = valor / float(cotacao_do_dolar)
        print ('o valor do dolar neste momento e {} com a conversão fica o valor {:.3f} '.format(cotacao_do_dolar,valores_1))

    elif opicao == 2:
        print('opção escolhida DOLAR PARA REAIS')
        valores_2 = valor * float(cotacao_do_dolar)
        print('o valor do dolar neste momento e {} com a conversão fica o valor {:.3f} '.format(cotacao_do_dolar,valores_2))

    elif opicao == 3:
        print('opção escolhida COTAÇÃO REAIS PARA EURO')
        valores_3 = valor / float(cotacao_do_euro)
        print('o valor do bitcoin neste momento e {} com a conversão fica o valor {:.3f} '.format(cotacao_do_euro,valores_3))

    elif opicao == 4:
        print('opção escolhida COTAÇÃO EURO PARA REAIS')
        valores_4 = valor * float(cotacao_do_euro)
        print('o valor do dolar neste momento e {} com a conversão fica o valor {:.3f} '.format(cotacao_do_euro, valores_4))

    elif opicao == 5:
        print('opção escolhida COTAÇÃO DE REAIS PARA BITCOIN')
        valores_5 = valor / float(cotacao_do_bitcoin)
        print('o valor do euro neste momento e {} com a conversão fica o valor {:.3f} '.format(cotacao_do_bitcoin, valores_5))

    elif opicao == 6:
        print('opção escolhida COTAÇÃO BITCOIN PARA REAIS')
        valores_6 = valor * float(cotacao_do_bitcoin)
        print('o valor do bitcoin neste momento e {} com a conversão fica o valor {:.3f} '.format(cotacao_do_bitcoin, valores_6))

    print('cotação do dolar {} cotação do euro {} cotaçã do bitcoin {}'.format(cotacao_do_dolar, cotacao_do_euro,
                                                                           cotacao_do_bitcoin))
    sleep(1.5)
    recebe = int(input('Deseja continuar?\n 1 = (sim) \n 2 = (não) \nqual opção ?'))
    if recebe == 1:
        sleep(0.5)
        continuar = True
        print('\033[4;36m''ok iremos reiniciar nosso sistema''\033[m')
    if recebe == 2:
        sleep(0.5)
        continuar = False
        print('\033[31;40m''OK, muito obrigado por usar o nosso sitema nos agradecemos!!''\033[m')






