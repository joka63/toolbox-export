%global srcname toolbox-export

Name:    toolbox-export
Version: 0.2.2
Release: 4%{?dist}
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
sed 's/^version=.*$/'$(cat VERSION.txt)'/' toolbox-export


%build
make 


%install
DESTDIR=%{buildroot}/%{_prefix} make install


%files
%doc README.md
%doc README.de.md
%doc ACKNOWLEDGMENTS.md
%doc AUTHORS.md
%license COPYING.md
%{_bindir}/%{name}
%{_datadir}/man/man*/%{name}*


%changelog
* Sat Oct 25 2025 joka63 <JoKatzer@gmx.de> 0.2.2-4
- bump version to 0.2.3 (JoKatzer@gmx.de)
- fix: check and refuse -a -d combo (JoKatzer@gmx.de)
- fix: toolbox-export --purge may not clean-up db (JoKatzer@gmx.de)

* Wed Jul 03 2024 joka63 <JoKatzer@gmx.de> 0.2.2-3
- Fixed webhook's URL and Content type 

* Wed Jul 03 2024 joka63 <JoKatzer@gmx.de> 0.2.2-2
- test: autobuild after changing release nr (JoKatzer@gmx.de)

* Wed Jul 03 2024 joka63 <JoKatzer@gmx.de> 0.2.2-1
- docs: Updated READMEs (JoKatzer@gmx.de)
- chore: added version template for tito (JoKatzer@gmx.de)

* Mon Jul 01 2024 joka63 <JoKatzer@gmx.de> 0.2.1-1
- first package built with tito for toolbox-export version 0.2.1

