# This piece of code aims to plot children galaxy sources from a PhoSim image and the corresponding src catalog.

import lsst.afw.display
import lsst.afw.image
import lsst.afw.table

exposure = lsst.afw.image.ExposureF("/Users/rliu/Downloads/Hackweek/DC2/lsst_e_138143_f5_R22_S11_E000.fits.gz")
src = lsst.afw.table.SourceCatalog.readFits("/Users/rliu/Downloads/Hackweek/DC2/output/src/lsst_e_138143_f5_R22_S11_E000/src.fits")

galaxyObjects = src[(src['deblend_nChild'] == 0) &
                    (src['calib_psfCandidate'] == False) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e1'] < 1.5) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e1'] > -1.5) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e2'] < 1.5) &
                    (src['ext_shapeHSM_HsmShapeRegauss_e2'] > -1.5)]
print "\nIn the src catalog, there are \n%i galaxies; " %(len(galaxyObjects))

psfSources = src[(src['calib_psfUsed'] == True)]
print "%i sources used as PSF; " %(len(psfSources))

rejectedPsfSources = src[(src['calib_psfCandidate'] == True) &
                         (src['calib_psfUsed'] == False)]
print "%i sources considered as PSF candidates but later rejected.\n" %(len(rejectedPsfSources))


display = lsst.afw.display.Display(frame=0)
display.mtv(exposure)
with display.Buffering():
    for record in galaxyObjects:
        display.dot(record.getShape(), record.getX(), record.getY())

with display.Buffering():
    for star in psfSources:
        display.dot("+", star.getX(), star.getY(), size=10, ctype='red')

with display.Buffering():
    for rej in rejectedPsfSources:
        display.dot("+", rej.getX(), rej.getY(), size=10, ctype='orange')
