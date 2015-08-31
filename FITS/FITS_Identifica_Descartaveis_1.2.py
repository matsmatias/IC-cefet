import numpy as np
import pyfits
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import pyfits
from pyfits import update

hdulist = pyfits.open("round1_test_set.fits")
new = pyfits.open("new.fits")
#hdulist.info()
y = pyfits.BinTableHDU
y = hdulist.copy()
prihdr = hdulist[1].header

tbdata = hdulist[1].data
#newdata = new[1].data
#teste = tbdata.field(279)
#for n in range(500):  FUNCIONANDO
    #teste = tbdata.field(279)#
   # if ((tbdata[n][279]!= 1) and (tbdata[n][279]!= 2)):
       # tbdata[n][279] = 0.0
       # print(tbdata[n][279])
        #del tbdata[n][279]#
    #else:#
        #newdata.write(tbdata[n][279])#


for n in range(71622):
    for k in range(286):
        if (tbdata[n][k]== -999):
            print(tbdata[n][k])
            tbdata[n][k] = 0.0
               

        
        
#update(y, tbdata, 1)
y[1].data = tbdata
y[1].writeto("novo2.fits")        

n = np.arange(100.0)
#hdu = pyfits.PrimaryHDU(n)
#hdulist = pyfits.HDUList([hdu])
#hdulist.writeto("new.fits")

hdulist.close()



#if ((tbdata[n].field(279)!= 1) and (tbdata[n].field(279)!= 2)):
    #print (tbdata[n].field(279) )
