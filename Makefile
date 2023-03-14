install:
	pip install -r requirements.txt

lint: 
	pylint src/

type-check:
	mypy src

test:
	coverage run -m unittest discover 

coverage:
	coverage report