import numpy as np
import pyfits
from pyfits import update

qtdDescartes = 0
qtdZeros = 0
qtdUns = 0
totalElementos = 0
hdulist = pyfits.open("round1_test_set.fits")
hdulist.info()

y = pyfits.BinTableHDU
y = hdulist.copy()

prihdr = hdulist[1].header
tbdata = hdulist[1].data
matriz = np.zeros((71622, 286))
print(matriz.shape)


matriz[2][35]= tbdata[54][279]
print(matriz[2][35])
matriz[0][0] = tbdata[0][0]
print(matriz[0][0])

#for i in range(71622):
#    for j in range(286):
#        matriz[i][j] = tbdata[i][j]

print(tbdata.shape)
for k in range(71622):
    totalElementos = totalElementos + 1
    if (tbdata[k][279]== 0.0):
        qtdZeros = qtdZeros + 1
        print("entrou")
    if (tbdata[k][279]== 1):
        qtdUns = qtdUns + 1
        print("entrou1")
    if (tbdata[k][279]== -999):
        print("Linha:", k," com elemento de valor -999")
        print(tbdata.shape)
        #tbdata.remove(tbdata[k]) não funciona
        #tbdata[k].remove()  não funciona
        qtdDescartes = qtdDescartes + 1

    
print("\n Concluído!")

y[1].data = tbdata
y[1].writeto("filtrado.fits")

print("Estatísticas: ")
print("Quantidade de elementos descartados = ", qtdDescartes)
print("Quantidade de 0 = ", qtdZeros)
print("Quantidade de 1 = ", qtdUns)
print((100*qtdDescartes)/totalElementos, "% dos elementos foram descartados")
print((100*qtdZeros)/totalElementos, "% dos elementos de valor igual a 0")
print((100*qtdUns)/totalElementos, "% dos elementos de valor igual a 1")
print(100*((totalElementos)-(qtdDescartes-qtdUns-qtdZeros))/totalElementos, "% dos elementos diferentes de -999, 0 ou 1")


#cria nova tabela fits
#a1 = np.array(['NGC1001', 'NGC1002', 'NGC1003'])
#a2 = np.array([11.1, 12.3, 15.2])
#col1 = pyfits.Column(name='target', format='12A', array=a1)
#col2 = pyfits.Column(name='V_mag', format='E', array=a2)                      
hdulist.close()
