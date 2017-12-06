# This piece of code aims to plot second moments of detected objects againt their flux.

import lsst.afw.display
import lsst.afw.image
import lsst.afw.table
import numpy
import os
from matplotlib import pylab as plt
import pylab

exposure = lsst.afw.image.ExposureF("/Users/rliu/Downloads/Hackweek/DC2/lsst_e_138143_f5_R22_S11_E000.fits.gz")
catalog = lsst.afw.table.SourceCatalog.readFits("/Users/rliu/Downloads/Hackweek/DC2/output/src/lsst_e_138143_f5_R22_S11_E000/src.fits")

xx = []
yy = []
xy = []
flux = []
for record in catalog:
    if record.get('deblend_nChild')==0:
        xx.append(record.get('base_SdssShape_xx'))
        yy.append(record.get('base_SdssShape_yy'))
        xy.append(record.get('base_SdssShape_xy'))
        flux.append(record.get('base_SdssShape_flux'))
xx = numpy.array(xx)
yy = numpy.array(yy)
xy = numpy.array(xy)
flux = numpy.array(flux)
print "There are %i deblended children sources." %(len(xx))

plt.gca()
plt.scatter(flux, xx+yy, alpha=.5, label='ixx+iyy')
# plt.scatter(flux, xx, alpha=.5, label='ixx')
# plt.scatter(flux, yy, alpha=.5, label='iyy')
# plt.scatter(flux, xy, alpha=.5, label='ixy')

plt.xlabel('SDSS_Flux')
plt.ylabel('SDSS_SecondMoment')
#plt.loc(1)
plt.legend(loc='upper right')
pylab.xlim([-0.01e7,1.6e7])
pylab.ylim([-20,300])
plt.show()
