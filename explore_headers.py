from __future__ import print_function, division

"""

TODO: need to add Vega system after mag i.e. mag; Vega system


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


see also: http://almaost.jb.man.ac.uk/help/FITSFIXER.py


"""

import numpy as np
from astropy.io import fits

from astropy.table import Table


def mk_phase3_newheader(header=None, debug=True):
    """

    make a new header with keywords sorted by field/column

    """

    keyword_list_mandatory = ['TTYPE', 'TFORM']
    keyword_list_optional = ['TCOMM', 'TUNIT', 'TUCD']

    # keyword_list_all = keyword_list_mandatory.append(keyword_list_optional)
    keyword_list_all = keyword_list_mandatory + keyword_list_optional

    print('keywords:', keyword_list_mandatory)
    print('keywords:', keyword_list_mandatory + keyword_list_optional)

    newheader = header.copy()

    nfields = header['TFIELDS']
    for ifield in range (1, nfields + 1):

        print(ifield)

        keyword = 'TTYPE' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]
        print(ifield, itest, keyword, value)

        keyword_next = 'TFORM' + str(ifield)
        itest = header.index(keyword_next)
        print(itest, type(header[itest]), header[itest])
        #print(itest, header.keys(itest))
        print(itest, header.comments[itest])
        newheader.set(keyword_next, header[itest], after=keyword)

        keyword = keyword_next
        keyword_next = 'TUNIT' + str(ifield)
        # locate keyword in original header and copy it
        print(itest, type(header[itest]), header[itest])
        itest = header.index(keyword_next)
        newheader.set(keyword_next, header[itest], after=keyword)


        keyword = keyword_next
        keyword_next = 'TUCD' + str(ifield)
        # locate keyword in original header and copy it
        print(itest, type(header[itest]), header[itest])
        itest = header.index(keyword_next)
        newheader.set(keyword_next, header[itest], after=keyword)

        keyword = keyword_next
        keyword_next = 'TCOMM' + str(ifield)
        # locate keyword in original header and copy it
        print(itest, type(header[itest]), header[itest])
        itest = header.index(keyword_next)
        print(keyword_next, header[itest])
        # look for mag in the string
        itest_mag = header[itest].find(' mag ')
        if itest_mag > -1:
            print('mag test:', header[itest])
            print(itest_mag)
            raw_input("Press ENTER to continue: ")


        itest_colour = header[itest].find(' colour')
        if itest_colour > -1:
            print('colour test:', header[itest])
            print(itest_colour)
            raw_input("Press ENTER to continue: ")

        newheader.set(keyword_next, header[itest], after=keyword)


    print(newheader)

    return newheader


def fits_header_fix_keyword_order(header=None):
    """



    """

    # look through by column number and copy the cards sequentially
    # create a list of unique keyword prefixes by striping off the field
    # numbers.
    # i.e.
    #    TTYPE1 -> TTYPE
    #    TTYPE2 -> TTYPE
    #    TFORM1 -> TFORM
    #
    # order within a column is:
    #    TTYPE
    #    TFORM


    for ifield in range(1, nfields + 1):
        print(ifield)
        keyword = 'TTYPE' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]



def fits_header_fix_units(header=None):
    """


    """
    keyword_list_mandatory = ['TTYPE', 'TFORM']
    keyword_list_optional = ['TCOMM', 'TUNIT', 'TUCD']

    # keyword_list_all = keyword_list_mandatory.append(keyword_list_optional)
    keyword_list_all = keyword_list_mandatory + keyword_list_optional

    print('keywords:', keyword_list_mandatory)
    print('keywords:', keyword_list_mandatory + keyword_list_optional)


    for ifield in range(1, nfields + 1):
        print(ifield)
        keyword = 'TTYPE' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]

        print(ifield, itest, keyword, value)




    # galact longitude and latitude
    if TTYPE == 'L' and TUNITS == '':
         TUNITS = 'deg'


    result = header

    return result


def fits_column_stats(data=None, ifield=None, debug=True):
    """

    see also table_stats

    """

    # ifield is 1-indexed; icolumn is 0-indexed
    icolumn = ifield - 1

    # try to compute stats for numeric columns and then strings
    # help(data)
    print()
    print(ifield, type(data))
    print(ifield, type(data.field(icolumn)))
    print(ifield, data.field(icolumn).shape, data.field(icolumn).size)
    print(ifield, type(data.field(icolumn)[0]))

    data_min = None
    data_max = None

    n_unique = np.unique(data.field(icolumn))

    if isinstance(data.field(icolumn)[0], basestring):
        print(ifield, 'This column is a character array')

    try:
        data_min = np.nanmin(data.field(icolumn))
    except:
        data_min= np.min(np.array(data.field(icolumn), dtype=object))

    try:
        data_max = np.nanmax(data.field(icolumn))
    except:
        data_max = np.max(np.array(data.field(icolumn), dtype=object))

    data_range = None
    try:
        data_range = data_max - data_min
    except:
        pass

    try:
        print(ifield, data.field(column).shape,
              data.ifield(column).size, len(data.ifield(icolumn)))
        print(ifield, data_min, data_max,
              len(data.field(icolumn)[np.isnan(data.field(icolumn))]))
        print('Range:', data_range)
        print(ifield, 'Unique values:', len(n_unique))
    except:
        # deal with the strings
        # http://stackoverflow.com/questions/12654093/arrays-of-strings-into-numpy-amax
        # data_dtype = data[ifield].dtype
        # print(ifield, data[ifield].shape, data[ifield].size, data_type)
        print(ifield, 'Range:', data_min, data_max, data_range)
        print(ifield, 'Unique values:', len(n_unique))

    result = None

    if ifield < 10 and debug:
        raw_input("Press ENTER to continue: ")

    return result




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


    keyword_list_mandatory = ['TTYPE', 'TFORM']
    keyword_list_optional = ['TUCD', 'TCOMM', 'TUNIT']

    # keyword_list_all = keyword_list_mandatory.append(keyword_list_optional)
    keyword_list_all = keyword_list_mandatory + keyword_list_optional

    print('keywords:', keyword_list_mandatory)
    print('keywords:', keyword_list_mandatory + keyword_list_optional)

    hdulist.info()
    print('type(hdulist):', type(hdulist))
    print('Number of HDUs:', len(hdulist))
    print('hdulist.filename:', hdulist.filename())

    header = hdulist[1].header
    print('type(header):', type(header))
    print('type(header[0]):', type(header[0]), len(header[0]))
    print('Number of bytes per row:', header['NAXIS1'])
    print('Number of table rows:', header['NAXIS2'])
    print('Number of table fields/columns:', header['TFIELDS'])
    print()
    help(header)
    print('Header items:', header.items())
    help(header.items)
    print()
    print('Header keywords:', header.keys())
    help(header.keys)
    print()
    print('Header values:', header.values())
    help(header.values)
    print()
    # print('Header comments:', header.comments())
    for key in header.keys():
        print(key)

    raw_input("Press ENTER to continue: ")


    tbdata = hdulist[1].data
    print('type (tbdata):', type(tbdata))
    print('len(tbdata):', len(tbdata))

    columns = hdulist[1].columns
    columns.info()

    if debug: raw_input("Press ENTER to continue: ")

    # copy the header
    header_copy = header
    nfields = header['TFIELDS']
    for ifield in range (1, nfields + 1):
        print(ifield)
        keyword = 'TTYPE' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]

        print(ifield, itest, keyword, value)


        keyword = 'TFORM' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]

        print(ifield, itest, keyword, value)

        keyword = 'TCOMM' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]

        print(ifield, itest, keyword, value)



        keyword = 'TUNIT' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]

        print(ifield, itest, keyword, value)

        keyword = 'TUCD' + str(ifield)
        itest = -1
        value = ''
        try:
            itest = header.index(keyword)
        except:
            pass
        if itest  > -1:
            value = header[itest]

        print(ifield, itest, keyword, value)

        # compute column/field stats
        fits_column_stats(data=tbdata, ifield=ifield)


    # determine the list of unique keywords with the prefix T

    if debug: raw_input("Press ENTER to continue: ")

    help(header)
    # find the keywords for column1
    itest = -1
    try:
        itest = header.index('TTYPE')
    except:
        pass

    print(itest)
    itest = header.index('TTYPE1')
    print(itest)


    if debug: raw_input("Press ENTER to continue: ")
    help(fits.Header)

    if debug: raw_input("Press ENTER to continue: ")

    # Header.index
    # Returns the index if the first instance of the given keyword in the
    # header, similar to `list.index` if the Header object is treated as a
    # list of keywords.
    help(fits.Header.index)

    print(header)

    print('type(header):', type(header), len(header))
    print(type(header[0]), len(header[0]))
    print(header[0], header.comments)

    if debug: raw_input("Press ENTER to continue: ")

    # print(header[0].comments)

    help(header)
    # list all the header cards
    for (icard, card) in enumerate(header):
        print(icard, icard + 1, card, header[icard])


    itest = header

    help(header)

    # print(header)


    if debug: raw_input("Press ENTER to continue: ")

    return



if __name__ == "__main__":

    import os
    import sys
    import time

    import traceback
    import inspect
    import logging

    # format = '%(asctime)s.%(msecs)02d %(levelname)s %(name)s' \
    #         '%(module)s - %(funcName)s: %(message)s'

    format = '%(asctime)s %(levelname)s %(name)s' \
               '%(module)s - %(funcName)s: %(message)s'

    logging.basicConfig(
        level=logging.INFO,
        format=format,
        datefmt="%Y-%m-%d %H:%M:%S")

    logger = logging.getLogger(__name__)

    inpath = '/data/desardata/MachineLearning/VHS_DR4_ESO/'
    filename = 'fs472446409191_v20110814_00914_586174.fits'

    infile = inpath + filename

    hdulist = fits.open(infile)
    hdulist.info()
    header = hdulist[1].header
    data = hdulist[1].data


    print()
    logger.info('Writing out some info')

    print('hdulist.filename():', hdulist.filename())
    # print('header.filename():', header.filename())
    # print('data.filename():', data.filename())
    print('hdulist.fileinfo(0):', hdulist.fileinfo(0))
    print('hdulist.fileinfo(1):', hdulist.fileinfo(1))
    print('hdulist[0].header[0]:', hdulist[0].header[0])
    print('hdulist[0].header[1]:', hdulist[0].header[1])
    print('hdulist[0].header.cards[0]:', hdulist[0].header.cards[0])
    print('hdulist[0].header.cards[0][0]:', hdulist[0].header.cards[0][0])
    print('hdulist[0].header.cards[0][1]:', hdulist[0].header.cards[0][1])
    print('hdulist[0].header.cards[0][2]:', hdulist[0].header.cards[0][2])
    # print('header.fileinfo():', header.fileinfo(0))
    print('CHECKSUM (original value):', header['CHECKSUM'])
    print('DATASUM (original value):', header['DATASUM'])

    # fix phase3 header
    newheader = mk_phase3_newheader(header=header, debug=True)

    print()
    logger.info('Writing out results')
    print('hdulist.filename():', hdulist.filename())
    print('hdulist[0].header[0]:', hdulist[0].header[0])
    print('hdulist[0].header[1]:', hdulist[0].header[1])
    print('hdulist[0].header.cards[0]:', hdulist[0].header.cards[0])
    print('hdulist[0].header.cards[0][0]:', hdulist[0].header.cards[0][0])
    print('hdulist[0].header.cards[0][1]:', hdulist[0].header.cards[0][1])
    print('hdulist[0].header.cards[0][2]:', hdulist[0].header.cards[0][2])
    # print('header.fileinfo():', header.fileinfo(0))
    # print('header.filename():', header.filename())
    # print('data.filename():', data.filename())
    print('hdulist.fileinfo(0):', hdulist.fileinfo(0))
    print('hdulist.fileinfo(1):', hdulist.fileinfo(1))
    print('CHECKSUM (original value):', header['CHECKSUM'])
    print('DATASUM (original value):', header['DATASUM'])
    hdulist[1].header = newheader

    hdulist.writeto('tmp.fits', overwrite=True, checksum=True)

    # read back check
    hdulist = fits.open('tmp.fits')
    header = hdulist[1].header
    print('hdulist.filename():', hdulist.filename())
    print('CHECKSUM (new value):', header['CHECKSUM'])
    print('DATASUM (new value):', header['DATASUM'])
    raw_input("Press ENTER to continue: ")

    # read astropy.Table
    table = Table.read('tmp.fits')
    # read astropy.Table
    table.meta['filename'] = 'tmp.fits'
    print("table.meta['filename']:", table.meta['filename'])

    explore_fits_header(infile=infile, header=None)

    explore_table_header(infile=infile, header=None)

    # read astropy.Table
    table = Table.read(infile)
