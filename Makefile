doc:
	python3 src/generate_doc.py > docs/api.md
	python3 src/main.py docs/example_graffiti.jpg

test:
	pytest