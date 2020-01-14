all: test

test:
	python3 -m doctest fskv.py

clean:
	rm -rf __pycache__
	rm -f data/*
	touch data/.gitignore
	