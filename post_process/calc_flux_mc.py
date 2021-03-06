import glob
import os
import subprocess
import wxdata as wxdata2
#from pylab import *
from numpy import *
import numpy

frames = 40
Ly = 12.8
wci = 0.1

if os.path.exists('ssrecon_wv_2.pin'):
	d = ['ssrecon_wv_0','ssrecon_wv_1','ssrecon_wv_2']
elif os.path.exists('ssrecon_wv_1.pin'):
	d = ['ssrecon_wv_0','ssrecon_wv_1']
else:
	d = ['ssrecon_wv_0']

for m in range(0,len(d)):
	flux  = numpy.zeros(frames+1, numpy.float)

		
	for n in range(0,frames+1):
		dh = wxdata2.WxData(d[m], n)
		q = dh.read('qnew')
		dx = (q.grid.upperBounds[1]-q.grid.lowerBounds[1])/q.grid.numPhysCells[1]
		ny = int(round(q.grid.numPhysCells[1]/2))
		by = q[:, ny, 14]
		
		flux[n] = dx*numpy.sum( numpy.fabs(by) )
		dh.close()
		
        flux = flux/(2*Ly)
        flux = 2*wci*flux/flux[0] # rescale to match GEM conditions

	numpy.savetxt((d[m]+str('.dat')),flux)
