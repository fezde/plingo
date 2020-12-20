doc:
	#Generate API doc
	python3 src/generate_doc.py > docs/api.md

doc-images:
	#Generate static examples
	python3 src/plingo docs/example_graffiti.jpg
	python3 src/plingo docs/example_ghavatar.png

	#Generate iterative example
	python3 src/plingo -i 200 docs/example_ghavatar.png
	convert -loop 0 -delay 200 docs/example_ghavatar.png -delay 33 docs/example_ghavatar.png_out_*.png docs/example_ghavatar_200.gif
	rm docs/example_ghavatar.png_out_*.png

doc-long-animation:
	#Generate a long iterative example animation
	python3 src/plingo -i 2000 docs/example_ghavatar.png
	convert -loop 0 -delay 200 docs/example_ghavatar.png -delay 5 docs/example_ghavatar.png_out_*.png docs/example_ghavatar_2000.gif
	rm docs/example_ghavatar.png_out_*.png

build:
	pip3 install -e .

test:
	tox
