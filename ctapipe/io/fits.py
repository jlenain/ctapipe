"""
Dump data to FITS file
"""

from astropy import log
from astropy.io import fits
from ctapipe.io import containers

class DumpToFits:
    """
    Dump a container to FITS
    """

    def __init__(self, name="DumpToFits"):
        super().__init__(name)

    def quantity_to_tuple(self, qt,unit_str):
        """
        Splits a quantity into a tuple of (value,unit) where unit is FITS complient.
        Useful to write FITS header keywords with units in a comment.

        :param qt:
        :param unit_str:
        :return:
        """
        return qt.to(unit_str).value, qt.to(unit_str).unit.to_string(format='FITS')


    def write_container_to_fits(self, Container):
        """
        Dump a Container into a FITS file

        :param Container:
        :return:
        """
        if type(Container) is containers.MCEvent:
            write_mccontainer_to_fits(Container)

    def write_mccontainer_to_fits(self, Container, outfile=None):
        """

        :param Container:
        :return:
        """
        if outfile is None:
            log.error('Please provide a name for the output file.')
        else:

            header = ""
            hdu = fits.
            for event in Container:
                e = event.mc.energy.value

            hdu.writeto(outfile)