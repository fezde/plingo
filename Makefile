doc: build
	python3 src/generate_doc.py > docs/api.md
	python3 src/plingo docs/example_graffiti.jpg

build:
	pip3 install -e .

test:
	tox
