init:
	pip install -r requirements.txt
	export PYTHONPATH="$PYTHONPATH:$HOME/.python"

test:	
	nosetests tests

