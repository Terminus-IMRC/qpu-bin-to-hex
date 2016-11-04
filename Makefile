CFLAGS := -Wall -Wextra -O2

CC := gcc
INSTALL := install
RM := rm -f

PREFIX ?= /usr/local

all: qbin2hex

qbin2hex: qbin2hex.o

.PHONY: install
install: qbin2hex
	$(INSTALL) -D -t "$(DESTDIR)/$(PREFIX)/bin/" qbin2hex

.PHONY: clean
clean:
	$(RM) qbin2hex qbin2hex.o
