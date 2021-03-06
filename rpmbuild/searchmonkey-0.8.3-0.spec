Summary: Graphical equivalent of find + grep
Name: searchmonkey
Version: 0.8.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
Source0: http://searchmonkey.embeddediq.com/repo/searchmonkey-%{version}.tar.gz
URL: http://searchmonkey.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: pkgconfig, gettext, gtk2-devel

%description
searchmonkey is a powerful, but fast GTK+ text search utility that allows
files and content to be searched using regular expressions.  It aims
to be the graphical equivalent of find + grep, but with the simplicity
of the Beagle search engine.

%prep
%setup -q

%build
%configure
make

%install
rm -fr %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -fr %{buildroot}

%files
%doc README INSTALL COPYING.LESSER
%{_bindir}/searchmonkey
%{_datadir}/icons/hicolor/16x16/apps/searchmonkey.png
%{_datadir}/icons/hicolor/22x22/apps/searchmonkey.png
%{_datadir}/icons/hicolor/24x24/apps/searchmonkey.png
%{_datadir}/icons/hicolor/32x32/apps/searchmonkey.png
%{_datadir}/icons/hicolor/48x48/apps/searchmonkey.png
%{_datadir}/pixmaps/searchmonkey/*.png
# Only required for GNOME
%{_datadir}/applications/searchmonkey.desktop
%{_datadir}/locale/*/LC_MESSAGES/*.mo
