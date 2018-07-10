.PHONY: test

install:
	pip3 install -r requirements.txt

coverage: 
	coverage run -m unittest -v -b
	coverage report

style:
	pylint src
	pylint test

format:
	autopep8 -i src/*.py
	autopep8 -i test/*.py

test: style coverage

clean:
	rm -f test/*.pyc
	rm -f src/*.pyc

scrub: clean
	rm -rf test/__pycache__/
	rm -rf src/__pycache__/
