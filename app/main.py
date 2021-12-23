import pdfkit
from config import options
from markdown import markdown

input_filename = '../tests/Sample.md'
style = 'css/sonar.css'


def main():
    with open(input_filename, 'r') as f:
        html_text = markdown(f.read(), output_format="html")
        pdfkit.from_string(html_text, '../tests/Result.pdf', options=options, css=style)


if __name__ == "__main__":
    main()
