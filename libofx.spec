
Summary:	The LibOFX library is designed to allow applications to support OFX command responses
Name:		libofx
Version:	0.6.5
Release:	0.1
Source0:	http://download.sourceforge.net/libofx/%{name}-%{version}.tar.gz
BuildRequires:	opensp-devel
Group:		Libraries
License:	GPL
URL:		http://libofx.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the LibOFX library. It is a API designed to allow applications
to very easily support OFX command responses, usually provided by
financial institutions. See http://www.ofx.net/ofx/default.asp for
details and specification. LibOFX is based on the excellent OpenSP
library written by James Clark, and now part of the OpenJADE
http://openjade.sourceforge.net/ project. OpenSP by itself is not
widely distributed. OpenJADE 1.3.1 includes a version on OpenSP that
will link, however, it has some major problems with LibOFX and isn't
recommended. Since LibOFX uses the generic interface to OpenSP, it
should be compatible with all recent versions of OpenSP (It has been
developed with OpenSP-1.5pre5). LibOFX is written in C++, but provides
a C style interface usable transparently from both C and C++ using a
single include file.


%package devel
Summary:        Header files for libofx
Group:          Development/Tools
Requires:       %{name} = %{version}

%description devel
Header files for developing programs using libofx

%package static
Summary:        Static version libofx library
Summary(pl):    Biblioteka statyczna libofx
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}

%description static
Static libofx library.


%prep
%setup -q

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
#LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} make prefix=$RPM_BUILD_ROOT%{_prefix} \#
#    libdir=$RPM_BUILD_ROOT%{_libdir} \
#    datadir=$RPM_BUILD_ROOT%{_datadir} \
#    includedir=$RPM_BUILD_ROOT%{_includedir} install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so.*.*
%{_datadir}/libofx/dtd/*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
