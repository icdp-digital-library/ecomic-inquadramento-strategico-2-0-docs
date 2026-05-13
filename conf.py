# Configuration file for the Sphinx documentation builder.
# Docs Italia – Read the Docs compatible configuration.

project = 'Ecomic – Ecosistema digitale per la cultura'
author = 'Istituto centrale per la digitalizzazione del patrimonio culturale – Digital Library'
release = '2.0'
version = '2.0'
copyright = '2025, Istituto centrale per la digitalizzazione del patrimonio culturale – Digital Library'

language = 'it'

extensions = []

# Source
source_suffix = '.rst'
master_doc = 'index'
root_doc = 'index'

# HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 2,
    'collapse_navigation': False,
    'sticky_navigation': True,
}
html_css_files = ['custom.css']
html_static_path = ['_static']

# Disable epub cover (avoids warnings on Read the Docs)
epub_show_urls = 'footnote'

# LaTeX / PDF output
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'inputenc': '\\usepackage[utf8]{inputenc}',
    'babel': '\\usepackage[italian]{babel}',
}
latex_documents = [
    (master_doc,
     'ecomic-report-2.0.tex',
     'Ecomic – Ecosistema digitale per la cultura. Report 2.0',
     'Istituto centrale per la digitalizzazione del patrimonio culturale – Digital Library',
     'manual'),
]
