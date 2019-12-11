import csv
import time

grafo_paradas = {}
start=time.time()
nome_col_cabecalho = 'parada'

#abre o csv e monta um dicionário de PARADAS (POINTS- valores) para cada LINHA (chave)
with open('paradas-teste.csv', 'r', newline='') as arqe:
    arqreader = csv.reader(arqe, delimiter=';')
    par_ant = ('', '', '', '', '')
    for par in arqreader:
        if par[0] != nome_col_cabecalho:
                # se a LINHA DE ONIBUS atual é a mesma do par anterior lido, entao faz o arco entre as paradas (POINT)
                if par[3] == par_ant[3]:
                    if par_ant[2] in grafo_paradas.keys():
                        grafo_paradas[par_ant[2]].append(par[2])
                    else:
                        grafo_paradas[par_ant[2]] = [par[2]]

                #atualiza o par_ant e vai tratar o próximo    
                par_ant = par


def encontra_menor_caminho(grafo, parada_inicio, parada_fim, caminho=None):
    if caminho == None:
        caminho = []
        
    caminho = caminho + [parada_inicio]
    if parada_inicio == parada_fim:
        return caminho
    
    if not grafo.get(parada_inicio):
        return None
    
    menorcaminho = None
    for noh in grafo[parada_inicio]:
        if noh not in caminho:
            novocaminho = encontra_menor_caminho(grafo, noh, parada_fim, caminho)
            if novocaminho:
                if not menorcaminho or len(novocaminho) < len(menorcaminho):
                    menorcaminho = novocaminho
                    
    return menorcaminho

###INICIO DO PROGRAMA - DIGITAR PONTO DE INICIO E DE FIM PARA TRAÇAR O MENOR CAMINHO:
print("Digite o ponto de saída")
pto_saida = input()
print("Digite o ponto de chegada")
pto_chegada = input()

r = encontra_menor_caminho(grafo_paradas, pto_saida, pto_chegada)
if r:
    print('Menor caminho encontrado: ', r)
else:
    print('Não existe caminho possível entre os pontos')
