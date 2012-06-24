Summary:	Multiple-precision floating-point computations library
Summary(pl):	Biblioteka oblicze� zmiennoprzecinkowych wielokrotnej precyzji
Name:		mpfr
Version:	2.2.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.mpfr.org/mpfr-current/%{name}-%{version}.tar.bz2
# Source0-md5:	40bf06f8081461d8db7d6f4ad5b9f6bd
Patch0:		%{name}-info.patch
URL:		http://www.mpfr.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	gmp-devel >= 4.1.0
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library. The main goal of MPFR is
to provide a library for multiple-precision floating-point computation
which is both efficient and has a well-defined semantics. It copies
the good ideas from the ANSI/IEEE-754 standard for double-precision
floating-point arithmetic (53-bit mantissa).

%description -l pl
Biblioteka MPFR to biblioteka C do oblicze� zmiennoprzecinkowych z
wielokrotn� precyzj� i dok�adnym zaokr�glaniem (zwanym tak�e poprawnym
zaokr�glaniem). Jest oparta na bibliotece GMP wielokrotnej precyzji.
G��wnym celem MPFR jest dostarczenie biblioteki do oblicze�
zmiennoprzecinkowych wielokrotnej precyzji, kt�ra jest wydajna i ma
dobrze zdefiniowan� semantyk�. Powiela dobre idee ze standardu
ANSI/IEEE-754 dla arytmetyki zmiennoprzecinkowej podw�jnej precyzji (z
53-bitow� mantys�).

%package devel
Summary:	Header files for MPFR library
Summary(pl):	Pliki nag��wkowe biblioteki MPFR
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 4.1.0
Obsoletes:	libmpfr-devel

%description devel
Header files for MPFR library.

%description devel -l pl
Pliki nag��wkowe biblioteki MPFR.

%package static
Summary:	Static MPFR library
Summary(pl):	Statyczna biblioteka MPFR
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPFR library.

%description static -l pl
Statyczna biblioteka MPFR.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared

# make -j4 creates truncated .lo files
%{__make} -j1 all
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog FAQ.html NEWS README TODO
%attr(755,root,root) %{_libdir}/libmpfr.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpfr.so
%{_libdir}/libmpfr.la
%{_includedir}/mpfr.h
%{_includedir}/mpf2mpfr.h
%{_infodir}/mpfr.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpfr.a
