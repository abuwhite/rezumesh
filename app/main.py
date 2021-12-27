import pdfkit

from config import options, g
from markdown import markdown

style = 'css/pandoc.css'

USERNAME = 'znhv'

repo = g.get_repo("{user}/{user}".format(user=USERNAME))
contents = repo.get_contents("")
while contents:
    content = contents.pop(0)
    if content.name.endswith('md'):
        with open('../tests/{name}.md'.format(name=USERNAME), 'wb') as f:
            f.write(content.decoded_content)
    else:
        print('Sorry, Markdown file not find :(')


def main():
    input_filename = '../tests/{user}.md'.format(user=USERNAME)

    with open(input_filename, 'r') as f:
        html_text = markdown(
            f.read(),
            output_format="xhtml"
        )
        pdfkit.from_string(
            html_text,
            '../tests/Result.pdf',
            options=options,
            css=style
        )


if __name__ == "__main__":
    main()
