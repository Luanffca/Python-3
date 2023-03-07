import requests
import os

def baixar_arquivo(url, endereco):
    # FAZ REQUISICAO AO SERVIDOR
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload Finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == '__main__':
    baixar_arquivo('https://ifce.edu.br/instituto/documentos-institucionais/resolucoes/2022/resolucao-01.pdf/view','resolucao_2022_01.pdf')

if __name__ == '__main__':
    BASE_URL = 'https://ifce.edu.br/instituto/documentos-institucionais/resolucoes/2022/resolucao-01.pdf/view'
    OUTPUT_DIR = 'output'
    
    for i in range(1,1):
        nome_arquivo = os.path.join(OUTPUT_DIR,'resolucao_2022_{}.pdf'.format(i))
        baixar_arquivo(BASE_URL,'resolucao_2022_01.pdf')