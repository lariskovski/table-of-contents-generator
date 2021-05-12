all:
	@python3 main.py $(file)

test:
	@flake8
	