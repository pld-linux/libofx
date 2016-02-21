Summary:	LibOFX library that allows applications to support OFX command responses
Summary(pl.UTF-8):	Biblioteka LibOFX pozwalająca aplikacjom obsługiwać odpowiedzi na polecenia OFX
Name:		libofx
Version:	0.9.10
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libofx/%{name}-%{version}.tar.gz
# Source0-md5:	adfa83a08d76b047f89a82d5b484f79b
Patch0:		%{name}-system-wide-treehh.patch
Patch1:		stdc++.patch
Patch2:		%{name}-flags.patch
URL:		http://libofx.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.9.7
BuildRequires:	help2man
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml++2-devel >= 2.6
BuildRequires:	opensp-devel
BuildRequires:	tree.hh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the LibOFX library. It is a API designed to allow applications
to very easily support OFX command responses, usually provided by
financial institutions. See http://www.ofx.net/ofx/default.asp for
details and specification. LibOFX is based on the excellent OpenSP
library written by James Clark, and now part of the OpenJADE project
(http://openjade.sourceforge.net/). LibOFX is written in C++, but
provides a C style interface usable transparently from both C and C++
using a single include file.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę LibOFX. Jest to API zaprojektowane aby
umożliwić aplikacjom w prosty sposób obsługiwać odpowiedzi na
polecenia OFX, zwykle udostępniane przez instytucje finansowe.
Szczegóły oraz specyfikację można znaleźć na stronie
http://www.ofx.net/ofx/default.asp. LibOFX jest oparta na świetnej
bibliotece OpenSP napisanej przez Jamesa Clarka, będącej teraz częścią
projektu OpenJADE (http://openjade.sourceforge.net/). LibOFX jest
napisana w C++, ale udostępnia interfejs w C, którego można używać w
sposób przezroczysty z poziomu C i C++ przy użyciu tego samego pliku
nagłówkowego.

%package devel
Summary:	Header files for LibOFX library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibOFX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	opensp-devel

%description devel
Header files for developing programs using LibOFX.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów z użyciem LibOFX.

%package static
Summary:	Static version LibOFX library
Summary(pl.UTF-8):	Biblioteka statyczna LibOFX
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibOFX library.

%description static -l pl.UTF-8
Statyczna biblioteka LibOFX.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{__rm} lib/tree.hh

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# C++ 11 is required by tree.hh 3+ and libxml++ 2.40+
CXXFLAGS="%{rpmcxxflags} -std=c++0x"
%configure \
	--with-opensp-libs=%{_libdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libofx.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libofx

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ofx2qif
%attr(755,root,root) %{_bindir}/ofxconnect
%attr(755,root,root) %{_bindir}/ofxdump
%attr(755,root,root) %{_libdir}/libofx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libofx.so.6
%{_datadir}/libofx
%{_mandir}/man1/ofxconnect.1*
%{_mandir}/man1/ofxdump.1*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libofx.so
%{_includedir}/libofx
%{_pkgconfigdir}/libofx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libofx.a
