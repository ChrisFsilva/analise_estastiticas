from for_sale import price_list
import statistics as st
import numpy as np



def metrics_itens(preco):
    # Calculando a media de cada salario da lista
    media = sum(preco) / len(preco)
    desvio = st.stdev(preco)
    # Calculando a moda, o valor da lista 'salario' será calculado pelo comando 'mode' na biblioteca 'statistics' apelidado de 'st'
    moda = st.multimode(preco)
    # Calculando a mediana, o valor da lista 'salario' será calculado pelo comando 'median' na biblioteca 'statistics' apelidado de 'st'
    mediana = st.median(preco)
    # Calculando a ampliantude
        # Colocando o maior valor da lista em na variavel max_value
    max_value = max(preco)
        # Colocando o menor valor da lista em na variavel min_value
    min_value = min(preco)
        # Calculando a amplitute maior valor - menor valor
    amplitute = max_value - min_value
    # Calculando a variância, o valor da lista 'salario' será calculado pelo comando np.var existente na biblioteca 'numpy' apelidado de 'np'
    variancia = np.var(preco)
    
    # teste de apresentação na tela
    print (f'A média de valores é R${media}')
    print (f'Sua mediana é R${mediana}')
    print (f'A média {media} é a soma dos valores dividida pela quantidade, enquanto a mediana {mediana} fornece uma ideia geral aproximada de onde os valores tendem a se concentrar.')
    print ('---------------------------------')
    print (f'As modas são R${moda}')
    print (f'A moda indica os valores que ocorrem com maior frequência em um conjunto de dados.')
    print ('---------------------------------')
    print (f'Sua amplitute é R${amplitute}')
    print ('---------------------------------')
    print (f'Sua variância é R${variancia}')
    print (f'A variância mede o quanto os dados estão distantes em relação à média.')
    print ('---------------------------------')
    print (f'Seu desvio é de R${desvio}')
    print (f'O desvio padrão é a raiz quadrada da variância, representando a dispersão dos dados na mesma unidade.')
    print ('')
    

metrics_itens(price_list)