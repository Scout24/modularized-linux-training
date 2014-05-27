Summary: Bash essentials man page
Name: bash-essentials
# Automated build process will fill in Version and Release
Version: VERSION
Release: 3
License: Creative Commons (CC BY-SA 3.0)
Vendor: Immobilien Scout GmbH
Packager: $Id: bash-essentials.spec 88759 2014-05-21 14:29:55Z sneben $
Group: Documentation/Man
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/ImmobilienScout24/modularized-linux-training
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: gzip, rubygem-ronn

%description
Essential tricks for using Bash. Part of ImmobilienScout24 Linux Training.

This man page should help with the daily work to improve and fasten your
ability to write clean and compact bash scripts.

%prep
%setup

%build
ronn %{_builddir}/%{name}-%{version}/bash-essentials.1.markdown
# BUGFIXING the display of '
sed -i "s/\\\'/\\\(aq/g" %{_builddir}/%{name}-%{version}/bash-essentials.1
gzip %{_builddir}/%{name}-%{version}/bash-essentials.1

%install
rm -rf  %{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 0644 bash-essentials.1.gz %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root,-)
%{_mandir}/man1/bash-essentials.1.gz

