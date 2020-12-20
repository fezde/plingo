doc-api:
	#Generate API doc
	python3 src/generate_doc.py > docs/api.md

doc-images:
	#Generate static examples
	plingo docs/example_graffiti.jpg
	plingo docs/example_ghavatar.png

	#Generate iterative example
	plingo -i 200 docs/example_ghavatar.png
	convert -loop 0 -delay 200 docs/example_ghavatar.png -delay 33 docs/example_ghavatar.png_out_*.png docs/example_ghavatar_200.gif
	ffmpeg -i docs/example_ghavatar_200.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*24:trunc(ih/2)*24" -sws_flags neighbor docs/example_ghavatar_200.mp4
	rm docs/example_ghavatar.png_out_*.png

doc-long-animation:
	#Generate a long iterative example animation
	plingo -i 2000 docs/example_ghavatar.png
	convert -loop 0 -delay 200 docs/example_ghavatar.png -delay 5 docs/example_ghavatar.png_out_*.png docs/example_ghavatar_2000.gif
	ffmpeg -i docs/example_ghavatar_2000.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*24:trunc(ih/2)*24" -sws_flags neighbor docs/example_ghavatar_2000.mp4
	rm docs/example_ghavatar.png_out_*.png

doc-all: doc-long-animation doc-images doc

build-dist:
	#pip3 install -e .
	python3 setup.py bdist_wheel

install: build-dist
	pip3 install --upgrade dist/Plingo-0.0.1.dev4-py3-none-any.whl

publish-test: build-dist
	twine upload --repository testpypi dist/*

publish: build-dist
	twine upload --repository pypi dist/*

test:
	tox
