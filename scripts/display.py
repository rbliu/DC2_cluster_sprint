# This piece of code aims to plot children galaxy sources from a PhoSim image and the corresponding src catalog.
# by Binyang Liu, Dec 5, 2017

import lsst.afw.display
import lsst.afw.image
import lsst.afw.table

exposure = lsst.afw.image.ExposureF("/Users/rliu/Downloads/Hackweek/DC2/eimages/lsst_e_138143_f5_R22_S11_E000.fits.gz")
src = lsst.afw.table.SourceCatalog.readFits("/Users/rliu/Downloads/Hackweek/DC2/calibrated/src/R22/S11.fits")

galaxyObjects = src[(src['deblend_nChild'] == 0) &
                    (src['calib_psfCandidate'] == False) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e1'] < 1.5) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e1'] > -1.5) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e2'] < 1.5) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e2'] > -1.5)]

possibleGalaxies = src[(src['deblend_nChild'] > 0) & (src['deblend_nChild'] <5)]

psfSources = src[(src['calib_psfUsed'] == True)]

rejectedPsfSources = src[(src['calib_psfCandidate'] == True) &
                         (src['calib_psfUsed'] == False)]

pointSource = src[(src['base_ClassificationExtendedness_value'] == 0)]
extendedSource = src[(src['base_ClassificationExtendedness_value'] == 1)]

print "\nIn the src catalog, there are \n%i galaxies; " %(len(galaxyObjects))
print "%i sources used as PSF; " %(len(psfSources))
print "%i sources considered as PSF candidates but later rejected.\n" %(len(rejectedPsfSources))


display = lsst.afw.display.Display(frame=0)
display.mtv(exposure)
with display.Buffering():
    for record in galaxyObjects:
        display.dot(record.getShape(), record.getX(), record.getY())

with display.Buffering():
    for sc in possibleGalaxies:
        display.dot(sc.getShape(), sc.getX(), sc.getY(), ctype='blue')

with display.Buffering():
    for star in psfSources:
        display.dot("+", star.getX(), star.getY(), size=10, ctype='red')

with display.Buffering():
    for rej in rejectedPsfSources:
        display.dot("+", rej.getX(), rej.getY(), size=10, ctype='orange')

# with display.Buffering():
#     for point in pointSource:
#         display.dot("+", point.getX(), point.getY(), size=10, ctype='yellow')
#
# with display.Buffering():
#     for extended in extendedSource:
#         display.dot(extended.getShape(), extended.getX(), extended.getY(), ctype='red')
