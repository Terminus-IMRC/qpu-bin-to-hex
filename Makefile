CFLAGS := -Wall -Wextra -O2

CC := gcc
RM := rm -f

all: qbin2hex

qbin2hex: qbin2hex.o

.PHONY: clean
clean:
	$(RM) qbin2hex qbin2hex.o
