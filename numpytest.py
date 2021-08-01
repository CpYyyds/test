#test.py
import numpy as np
b = np.ones((4,5))
np.savetext('./aigou.csv',b,dtype='float16',delimiter=',')


