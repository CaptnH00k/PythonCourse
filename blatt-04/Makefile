COMPILE_CMD = python3 -m py_compile
TEST_CMD = python3 -m doctest
CHECKSTYLE_CMD = flake8
PLOTFILE = WordCount.py

all: compile test checkstyle

compile:
	$(COMPILE_CMD) *.py

test:
	$(TEST_CMD) *.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
	rm -f times.txt

plot:
	python3 $(PLOTFILE)
	gnuplot -e 'plot "words.txt"; pause mouse;'
