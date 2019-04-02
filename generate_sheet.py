##############################################################################
#
# An example of inserting images into a worksheet using the XlsxWriter
# Python module.
#
# Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
#
import os
import xlsxwriter


# Create an new Excel file and add a worksheet.
normal = xlsxwriter.Workbook('images.xlsx')
siili = xlsxwriter.Workbook('images_siili.xlsx')

normalsheet = normal.add_worksheet()
siilisheet = siili.add_worksheet()

# Widen the first column to make the text clearer.

perLine = 6
ncount = 0
scount = 0

w = 11
h = 64
normalsheet.set_column(0, perLine-1, width = w)
normalsheet.set_row(0, height=h)
siilisheet.set_column(0, perLine-1, width = w)
siilisheet.set_row(0, height=h)


for filename in os.listdir("codes"):
    if filename.endswith('png'):
        if "BOI" in filename:
            siilisheet.set_row(scount // perLine, height=h)
            siilisheet.insert_image( scount // perLine, scount % perLine, os.path.join('codes', filename),
            {'x_scale': 2, 'y_scale': 2})
            scount += 1
        else:
            normalsheet.set_row(ncount // perLine, height=h)
            normalsheet.insert_image( ncount // perLine, ncount % perLine, os.path.join('codes', filename),
            {'x_scale': 2, 'y_scale': 2})
            ncount += 1
normal.close()
siili.close()