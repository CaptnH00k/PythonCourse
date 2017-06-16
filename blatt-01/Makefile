COMPILE_CMD = python3 -m py_compile
TEST_CMD = python3 -m doctest
CHECKSTYLE_CMD = flake8
PLOTFILE = mergesort.py

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
	python3 $(PLOTFILE) | tee times.txt
	gnuplot -e 'plot "times.txt"; pause mouse;'
