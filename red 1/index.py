import numpy as np
from keras.models import  Sequential
from keras.layers.core import Dense

# cargamos las comninaciones de las compuertas XOR
training_data=np.array([[0,0],[0,1],[1,0],[1,1]],"float32")

# y estos son los resultados que se obtienen en el mismo orden 
target_data=np.array([[0],[1],[1],[0]],"float32")

