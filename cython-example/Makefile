CYTHON=cython
CC=gcc
PYINC=/usr/include/python2.7
CFLAGS=-shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I$(PYINC)

compute_typed.so: compute_typed.c
	$(CC) $(CFLAGS) $^ -o $@

compute_typed.c: compute_typed.pyx
	$(CYTHON) $^

.PHONY: clean

clean:
	\rm *.so *.c
