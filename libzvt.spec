
%define _snap	20031020

Summary:	Zvt terminal widget library
Summary(es.UTF-8):	Biblioteca de widget de terminal zvt
Summary(pl.UTF-8):	Biblioteka z widgetem terminala zvt
Name:		libzvt
Version:	2.0.2
Release:	0.%{_snap}.4
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{_snap}.tar.bz2
# Source0-md5:	9c06f2e4ff429616284a0b1f62fe8c9b
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pangox.patch
Patch2:		%{name}-link.patch
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

%description -l es.UTF-8
El paquere libzvt contiene un widget de terminal para GTK+.

%description -l pl.UTF-8
Ten pakiet zawiera widget terminala dla GTK+.

%package devel
Summary:	Headers for libzvt
Summary(es.UTF-8):	Cabeceras para libzvt
Summary(pl.UTF-8):	Pliki nagłówkowe libzvt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel
Requires:	libart_lgpl-devel

%description devel
The libzvt package contains a terminal widget for GTK+.

You should install the libzvt-devel package if you would like to
compile applications that use the zvt terminal widget. You do not need
to install libzvt-devel if you just want to use precompiled
applications.

%description devel -l es.UTF-8
El paquere libzvt contiene un widget de terminal para GTK+.

Debe instalar el paquete libzvt-devel si quiere compilar aplicaciones
que usan el widget de terminal zvt. No tiene por qué instalarlo si
sólo quiere usar aplicaciones precompiladas.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilowania programów używających
libzvt.

Powinieneś zainstalować pakiet libzvt-devel jeśli chcesz kompilować
aplikacje które używają widgeta terminala zvt. Nie potrzebujesz
instalować libzvt-devel jeśli jedynie chcesz używać aplikacji już
skompilowanych.

%package static
Summary:	Static libzvt library
Summary(es.UTF-8):	Biblioteca libzvt estática
Summary(pl.UTF-8):	Statyczna biblioteka libzvt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libzvt libraries.

%description static -l es.UTF-8
La versión estática de bibliotecas libzvt.

%description static -l pl.UTF-8
Statyczna wersja bibliotek libzvt.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libzvt-*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
