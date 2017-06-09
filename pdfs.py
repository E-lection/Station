from StringIO import StringIO
from flask import render_template

def create_pdf(filename, voter_pin):
    # open output file for writing (truncated binary)
    #resultFile = open(outputFilename, "w+b")

    # # convert HTML to PDF
    # pisaStatus = pisa.CreatePDF(
    #         sourceHtml,                # the HTML to convert
    #         dest=resultFile)           # file handle to recieve result
    #
    # # close output file
    # resultFile.close()                 # close output file
    # pdf = pisa.CreatePDF(
    #     render_template('voterpincard.html'),
    #     file(filename, "wb")
    #     )
    # return True on success and False on errors
    return pdf
