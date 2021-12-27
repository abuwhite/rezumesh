PDF := Boris_Zhenikhov_CV.pdf
README := Test.md

all: pdf open

.PHONY: pdf
pdf: $(README)
	pandoc $(README) -o $(PDF)

.PHONY: open
open: $(PDF)
	open $(PDF)