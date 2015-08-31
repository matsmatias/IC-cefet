import numpy as np
import pyfits
from pyfits import update

hdulist = pyfits.open("filtrado.fits")

y = pyfits.BinTableHDU
y = hdulist.copy()
n = 71622
somatorio = np.zeros(286)
dp = np.zeros(286)

prihdr = hdulist[1].header
tbdata = hdulist[1].data

#Desvio padrão
for i in range(286):
    
    u = np.average(tbdata[i])
    
    for j in range(71622):
        somatorio[i] = somatorio[i] + (tbdata[j][i] - u)

    dp[i] = np.sqrt(somatorio[i] / n)
    
#Normalizar
for i in range(286):
    
    u = np.average(tbdata[i])
    
    for j in range(71622):
        tbdata[j, i] = (tbdata[j, i] - u) / dp

tbdata.writeto("normalizado.fits")
        


            


    
        
