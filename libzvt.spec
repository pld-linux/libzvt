
%define _snap	20031020

Summary:	Zvt terminal widget library
Summary(es):	Biblioteca de widget de terminal zvt
Summary(pl):	Biblioteka z widgetem terminala zvt
Name:		libzvt
Version:	2.0.2
Release:	0.%{_snap}.2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{_snap}.tar.bz2
# Source0-md5:	9c06f2e4ff429616284a0b1f62fe8c9b
Patch0:		%{name}-am15.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtk+2-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool >= 1.4.3
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	pkgconfig >= 1:0.14.0
Requires:	utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libzvt package contains a terminal widget for GTK+.

%description -l es
El paquere libzvt contiene un widget de terminal para GTK+.

%description -l pl
Ten pakiet zawiera widget terminala dla GTK+.

%package devel
Summary:	Headers for libzvt
Summary(es):	Cabeceras para libzvt
Summary(pl):	Pliki nag³ówkowe libzvt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel
Requires:	libart_lgpl-devel

%description devel
The libzvt package contains a terminal widget for GTK+.

You should install the libzvt-devel package if you would like to
compile applications that use the zvt terminal widget. You do not need
to install libzvt-devel if you just want to use precompiled
applications.

%description devel -l es
El paquere libzvt contiene un widget de terminal para GTK+.

Debe instalar el paquete libzvt-devel si quiere compilar aplicaciones
que usan el widget de terminal zvt. No tiene por qué instalarlo si
sólo quiere usar aplicaciones precompiladas.

%description devel -l pl
Pliki nag³ówkowe potrzebne do kompilowania programów u¿ywaj±cych
libzvt.

Powiniene¶ zainstalowaæ pakiet libzvt-devel je¶li chcesz kompilowaæ
aplikacje które u¿ywaj± widgeta terminala zvt. Nie potrzebujesz
instalowaæ libzvt-devel je¶li jedynie chcesz u¿ywaæ aplikacji ju¿
skompilowanych.

%package static
Summary:	Static libzvt library
Summary(es):	Biblioteca libzvt estática
Summary(pl):	Statyczna biblioteka libzvt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libzvt libraries.

%description static -l es
La versión estática de bibliotecas libzvt.

%description static -l pl
Statyczna wersja bibliotek libzvt.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# empty files
#%doc NEWS README AUTHORS
%doc libzvt/AUTHORS ChangeLog libzvt/README libzvt/TODO libzvt/BUGS
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/libzvt-2.0
%attr(2755,root,utmp) %{_libdir}/libzvt-2.0/gnome-pty-helper

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libzvt-*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
