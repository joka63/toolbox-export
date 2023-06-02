# Toolbox-export provides just one shell script, and does not require any special
# installation procedures or libraries. There is no need to run the
# "all" build target if you don't want to build the man pages (see
# doc/Makefile).

BINS        = toolbox-export
DOCS        = ChangeLog \
              README.md

PN          = toolbox-export
PREFIX     ?= /usr/local
BINDIR      = $(PREFIX)/bin
DOCDIR      = $(PREFIX)/share/doc/$(PN)
BASHCOMPDIR = $(PREFIX)/share/bash-completion/completions
MAN1DIR     = $(PREFIX)/share/man/man1

ifeq ($(COMPRESS), yes)
  DOCS := $(addsuffix .gz,$(DOCS))
endif

replace_vars = sed \
	-e "s|@PN@|$(PN)|g" \
	-e "s|@BINDIR@|$(BINDIR)|g" \
	-e "s|@DOCDIR@|$(DOCDIR)|g" \
	-e "s|@BASHCOMPDIR@|$(BASHCOMPDIR)|g" \
	-e "s|@MAN1DIR@|$(MAN1DIR)|g" 

all: man

install: install-bin install-man 

install-bin:
	@echo 'installing binary...'
	install -d -m 755 "$(DESTDIR)$(BINDIR)"
	install -p -m 755 $(BINS) "$(DESTDIR)$(BINDIR)"

install-man: man
	@echo 'installing man pages...'
	@$(MAKE) -C doc install-man

install-doc: $(DOCS)
	@echo 'installing documentation...'
	install -d -m 755 "$(DESTDIR)$(DOCDIR)"
	install -p -m 644 $(DOCS) "$(DESTDIR)$(DOCDIR)"
	@$(MAKE) -C doc install-doc

man:
	@echo 'generating manpages...'
	@$(MAKE) -C doc man

clean:
	rm -f *.gz
	@$(MAKE) -C doc clean

%.gz : %
	gzip -9 -n -c $< > $@
