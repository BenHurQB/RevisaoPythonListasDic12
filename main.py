#12) Uma pesquisa de mercado foi feita para decidir qual design de uma marca infantil mais agrada crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

#Tabela de votos da marca
#Design 1 - 1334 votos
#Design 2 - 982 votos
#Design 3 - 1751 votos
#Design 4 - 210 votos
#Design 5 - 1811 votos

#COPIAR CÓDIGO
#Adapte os dados fornecidos a você para uma estrutura de dicionário e a partir dele, informe o design vencedor e a porcentagem de votos recebidos.



def procuraMaiorValor(tabela):
  maior = max(tabela.values())
  return maior
  
def procurarOVencedor(tabela):
  chaveProcurada = ''
  for chave, valor in tabela.items():
    if valor == maior:
      chaveProcurada = chave
  return chaveProcurada

def imprimirVencedorPercentual():
  print(f'\n{chaveProcurada} foi Design Vencedor!!!\n')
  print(f'\n{percentual} % foi percentual alcançado pelo vencedor\n')
  
def percentualVencedor(tabela):
  soma = sum(tabela.values())
  percentual = round(tabela[chaveProcurada] / soma * 100)
  return percentual
  
#Declaracao de variaveis

tabela = {'Design 1':1334, 'Design 2':982, 'Design 3':1751, 'Design 4': 210, 'Design 5':1811 }
maior = procuraMaiorValor(tabela)
chaveProcurada = procurarOVencedor(tabela)
percentual = percentualVencedor(tabela)
imprimirVencedorPercentual() 
