.PHONY: test

install:
	pip3 install -r requirements.txt

test: 
	coverage run -m unittest -v -b
	coverage report
