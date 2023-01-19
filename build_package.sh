#!/bin/sh
python3 -m build
python3 -m twine upload --repository mistapi-testpypi dist/*     

#python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps mistapi
