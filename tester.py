import os
import numpy as np
import pandas as pd
import pickle as pck
os.chdir('/home/sahil/fundamentals8')
g=[]
with open('key_financial_ratios','rb') as d:
   try:
       while True:
         g.append(pck.load(d))
   except EOFError:
       pass
print(g)
