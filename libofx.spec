Summary:	LibOFX library that allows applications to support OFX command responses
Summary(pl):	Biblioteka LibOFX pozwalaj±ca aplikacjom obs³ugiwaæ odpowiedzi na polecenia OFX
Name:		libofx
Version:	0.6.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libofx/%{name}-%{version}.tar.gz
# Source0-md5:	685749c235518af6e7ee3c01122a306d
URL:		http://libofx.sourceforge.net/
BuildRequires:	opensp-devel
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

%description -l pl
Ten pakiet zawiera bibliotekê LibOFX. Jest to API zaprojektowane aby
umo¿liwiæ aplikacjom w prosty sposób obs³ugiwaæ odpowiedzi na
polecenia OFX, zwykle udostêpniane przez instytucje finansowe.
Szczegó³y oraz specyfikacjê mo¿na znale¼æ na stronie
http://www.ofx.net/ofx/default.asp. LibOFX jest oparta na ¶wietnej
bibliotece OpenSP napisanej przez Jamesa Clarka, bêd±cej teraz czê¶ci±
projektu OpenJADE (http://openjade.sourceforge.net/). LibOFX jest
napisana w C++, ale udostêpnia interfejs w C, którego mo¿na u¿ywaæ w
sposób przezroczysty z poziomu C i C++ przy u¿yciu tego samego pliku
nag³ówkowego.

%package devel
Summary:        Header files for LibOFX library
Summary(pl):	Pliki nag³ówkowe biblioteki LibOFX
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:	opensp-devel

%description devel
Header files for developing programs using LibOFX.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów z u¿yciem LibOFX.

%package static
Summary:        Static version LibOFX library
Summary(pl):    Biblioteka statyczna LibOFX
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}

%description static
Static LibOFX library.

%description static -l pl
Statyczna biblioteka LibOFX.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_datadir}/libofx

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/libofx

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
