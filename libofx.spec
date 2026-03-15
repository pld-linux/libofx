#
# Conditional build:
%bcond_without	apidocs	# Doxygen API documentation

Summary:	LibOFX library that allows applications to support OFX command responses
Summary(pl.UTF-8):	Biblioteka LibOFX pozwalająca aplikacjom obsługiwać odpowiedzi na polecenia OFX
Name:		libofx
Version:	0.10.9
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/libofx/libofx/releases
# TODO: use release tarballs
#Source0:	https://github.com/libofx/libofx/releases/download/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/libofx/libofx/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d53518ec2b5e12573add5477eaeb81c1
Patch0:		%{name}-system-wide-treehh.patch
Patch1:		%{name}-flags.patch
URL:		https://github.com/libofx/libofx
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.9.7
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	help2man
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml++2-devel >= 2.6
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
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

%package apidocs
Summary:	API documentation for LibOFX library
Summary(pl.UTF-8):	Dokumentacja API biblioteki LibOFX
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for LibOFX library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki LibOFX.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%{__rm} lib/tree.hh

%build
install -d config
touch INSTALL
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# C++ 11 is required by tree.hh 3+ and libxml++ 2.40+
CXXFLAGS="%{rpmcxxflags} -std=c++11"
%configure \
	--with-opensp-libs=%{_libdir}

%{__make} -j1

%if %{with apidocs}
%{__make} doc
%endif

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
%{_libdir}/libofx.so.*.*.*
%ghost %{_libdir}/libofx.so.7
%{_datadir}/libofx
%{_mandir}/man1/ofxconnect.1*
%{_mandir}/man1/ofxdump.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libofx.so
%{_includedir}/libofx
%{_pkgconfigdir}/libofx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libofx.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,js,png}
%endif
