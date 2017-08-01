from __future__ import print_function, division

"""


FITS file keywords and astropy.table
    http://docs.astropy.org/en/stable/io/unified.html#fits

The FITS keywords associated with an HDU table are represented in the meta
ordered dictionary attribute of a Table. After reading a table one can view the
available keywords in a readable format using:

>>> for key, value in t.meta.items():
...     print('{0} = {1}'.format(key, value))

This does not include the internal FITS keywords that are required to specify
the FITS table properties (e.g. NAXIS, TTYPE1). HISTORY and COMMENT keyords
are treated specially and are returned as a list of values.

Conversely, the following shows examples of setting user keyword values for a
table t:

>>> t.meta['MY_KEYWD'] = my value
>>> t.meta['COMMENT'] = ['First comment', 'Second comment', 'etc']
>>> t.write('my_table.fits', overwrite=True)

The keyword names (e.g. MY_KEYWD) will be automatically capitalized prior to
writing.

At this time, the meta attribute of the Table class is simply an ordered
dictionary and does not fully represent the structure of a FITS header
(for example, keyword comments are dropped).


"""


from astropy.io import fits

def explore_table_header(infile=None, header=None, debug=True):

    from astropy.table import Table

    table = Table.read(infile)

    help(table.meta.items)
    for ikey, (key, value) in enumerate(table.meta.items()):
        print('{0}: {1} = {2}'.format(ikey, key, value))

    if debug: raw_input("Press ENTER to continue: ")

    return


def explore_fits_header(infile=None, header=None, debug=True):


    # read with astropy.io.fits
    hdulist = fits.open(infile)
    # help(fits)
    # help(hdulist)

    hdulist.info()
    print('type(hdulist):', type(hdulist), len(hdulist))
    print('Number of HDUs:', len(hdulist))
    print('hdulist.filename:', hdulist.filename())

    header = hdulist[1].header

    print(header)

    print('type(header):', type(header), len(header))
    print(type(header[0]), len(header[0]))
    print(header[0], header.comments)
    print(header[0].cards)
    # print(header[0].comments)

    help(header)
    for (icard, card) in enumerate(header):
        print(icard, icard + 1, card, header[icard])


    itest = header

    help(header)

    # print(header)


    if debug: raw_input("Press ENTER to continue: ")

    return



def fix_units(header=None):


    # for key in hdu1.keys():

    # galact longitude
    if TTYPE == 'L' and unit == '':
        units = 'deg'


if __name__ == "__main__":


    inpath = '/data/desardata/MachineLearning/VHS_DR4_ESO/'
    filename = 'fs472446409191_v20110814_00914_586174.fits'

    infile = inpath + filename

    explore_header_table(infile=infile, header=None)

    explore_header_fits(infile=infile, header=None)


    # read astropy.Table
    table = Table.read(infile)
