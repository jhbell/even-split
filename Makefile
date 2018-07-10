.PHONY: test

install:
	pip3 install -r requirements.txt

test: 
	coverage run -m unittest -v -b
	coverage report

clean:
	rm -f test/*.pyc
	rm -f src/*.pyc

scrub: clean
	rm -rf test/__pycache__/
	rm -rf src/__pycache__/
