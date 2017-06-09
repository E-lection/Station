from flask import Flask, Response
import jinja2
import os
from jinja2 import Template

import pexpect

PDFLATEX_COMMAND = "pdflatex -interaction=nonstopmode -output-directory=tex {}"
TEMPLATE_TEX = 'tex/voterpincard.tex'
FILENAME = 'pin'
VOTERPIN_TEX = 'tex/' + FILENAME + '.tex'
VOTERPIN_PDF = 'tex/' + FILENAME + '.pdf'

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def create_pdf(voterpin):
	# Get the latex template
	template = latex_jinja_env.get_template(TEMPLATE_TEX)

	# Render this with the correct voter pin
	pin_tex = template.render(voterpin=voterpin)

	# Write pin_tex to a file
	file = open(VOTERPIN_TEX,'w')
	file.write(pin_tex)
	file.close()

	# Render it as a pdf
	tex_render = pexpect.spawn(PDFLATEX_COMMAND.format(VOTERPIN_TEX))
	try:
		tex_render.expect("Output written on", timeout=30)
	except pexpect.TIMEOUT:
		return "Rendering the PDF took too long, please try again!"

    # Load PDF into memory
	pdf_file = open(VOTERPIN_PDF)

    # Remove files from filesystem
	os.remove(VOTERPIN_TEX)
	os.remove(VOTERPIN_PDF)
	os.remove('tex/' + FILENAME + '.aux')
	os.remove('tex/' + FILENAME + '.log')

	return Response(pdf_file, mimetype='application/pdf')
