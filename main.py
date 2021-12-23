from markdown import markdown
import pdfkit

input_filename = 'Sample.md'
# output_filename = 'README.pdf'
#
with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format="html")

pdfkit.from_string(html_text, 'sample.pdf')

# with open('Sample.md', 'r+') as f:
#     text = f.read()
#     html = markdown(text)

# with open('README.html', 'w') as f:
#     f.write(html)

# pdfkit.from_string(html_text, output_filename)