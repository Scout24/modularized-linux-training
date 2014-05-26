TOPLEVEL = bash-essentials.1.markdown bash-essentials.spec

GITREV := HEAD

REVISION := "$(shell git rev-list $(GITREV) -- $(TOPLEVEL) 2>/dev/null| wc -l)$(EXTRAREV)"
VERSION := $(shell cat VERSION 2>/dev/null).$(REVISION)
PV = bash-essentials-$(VERSION)

.PHONY: all deb srpm clean rpm info debinfo rpminfo

all: deb rpm
	ls -l dist/*.deb dist/*.rpm

deb: clean
	mkdir -p dist build/tmp build/deb/DEBIAN build/deb/usr/share/man/man1 build/deb/usr/share/doc/bash-essentials build/deb/DEBIAN
	cp bash-essentials.1.markdown build/tmp/
	ronn build/tmp/bash-essentials.1.markdown
	sed -i "s/\\\'/\\\(aq/g" build/tmp/bash-essentials.1
	gzip --best build/tmp/bash-essentials.1
	install -m 0644 build/tmp/bash-essentials.1.gz build/deb/usr/share/man/man1/bash-essentials.1.gz
	install -m 0644 DEBIAN/control build/deb/DEBIAN
	install -m 0644 DEBIAN/copyright build/deb/usr/share/doc/bash-essentials
	sed -i -e s/VERSION/$(VERSION)/ build/deb/DEBIAN/control
	fakeroot dpkg -b build/deb dist

srpm: clean
	mkdir -p dist build/$(PV) build/BUILD
	cp -r $(TOPLEVEL) Makefile build/$(PV)
	mv build/$(PV)/*.spec build/
	sed -i -e s/VERSION/$(VERSION)/ build/*.spec
	tar -czf build/$(PV).tar.gz -C build $(PV)
	rpmbuild --define="_topdir $(CURDIR)/build" --define="_sourcedir $(CURDIR)/build" --define="_srcrpmdir $(CURDIR)/dist" --nodeps -bs build/*.spec

rpm: srpm
	ln -svf ../dist build/noarch
	rpmbuild --nodeps --define="_topdir $(CURDIR)/build" --define="_rpmdir %{_topdir}" --rebuild $(CURDIR)/dist/*.src.rpm


info: rpminfo debinfo

debinfo: deb
	dpkg-deb -I dist/*.deb

rpminfo: rpm
	rpm -qip dist/*.noarch.rpm

clean:
	rm -Rf dist/*.rpm dist/*.deb build
