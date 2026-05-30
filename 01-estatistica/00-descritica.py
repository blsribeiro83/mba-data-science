#MEDIDAS DE POSIÇÃO
#====================

#MÉDIA - soma de todos os valores dividos pela quantitade
#Sensível a outliers (um valor extremo puxa a média)

import numpy as np

lista_desc = [1, 2, 3, 4, 5, 6, 6]
np.mean(lista_desc)  # resultado: 3.857

#MEDIANA - valor que divide a amostra ao meio:
#50% dos valores estão abaixo, 50% acima
#Robusta a outliers (o CEO rico não distorce)

np.median(lista_desc)  # resultado: 4.00