.PHONY: docs
init:
	pip install -r requirements-dev.txt

publish-test:
	python3 -m build
	python3 -m twine upload --repository mistapi-testpypi dist/* 
	rm -fr build dist

publish:
	python3 -m build
	python3 -m twine upload --repository mistapi dist/* 
	rm -fr build dist 
