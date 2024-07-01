%global srcname toolbox-export
%
Name:    toolbox-export
Version: 0.0.0
Release: 0%{?dist}
License: GPLv3
Summary: Export starters and binaries from podman toolboxes
Url:     https://github.com/joka63/%{srcname}
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  rubygem-asciidoctor
BuildRequires:  make
Requires:       sqlite3

%description
Toolbox-export is a small project that aims to fill a small gap in Fedora's toolbox.

A frequently requested toolbox feature is the 
export of application starters. This mini-project aims to provide the missing feature.

Toolbox-export is basically an adaptation of the distrobox shell script distrobox-export to toolbox. It adopts its options and call syntax as much as possible.

%prep
%autosetup

%build
make 

%install
DESTDIR=%{buildroot} make install


%files
%doc README.md
%doc README.de.md
%doc ACKNOWLEDGEMENTS.md
%doc AUTHORS.md
%license COPYING.md
%{_bindir}/%{name}
%{_datadir}/man/man*/%{name}*


%changelog