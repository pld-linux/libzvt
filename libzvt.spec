%define gtk2_version 1.3.13
%define glib2_version 1.3.13
%define libart_lgpl_version 2.3.8

Summary:	Zvt terminal widget library
Summary(pl):	Biblioteka z widgetem terminala zvt
Name:		libzvt
Version:	1.110.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/����������
Group(uk):	X11/��̦�����
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libzvt/%{name}-%{version}.tar.bz2
URL:		ftp://www.gnome.org/
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:	libart_lgpl-devel >= %{libart_lgpl_version}
# Added to avoid the warning messages about utmp group, bug #24171
PreReq:		utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The libzvt package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

%description -l pl
Ten pakiet zawiera widget terminala dla GTK+. Jest u�ywany przez
gnome-terminal oraz inne programy.

%package devel
Summary:	Headers for libzvt
Summary(pl):	Pliki nag��wkowe libzvt
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}
Requires:	glib2-devel >= %{glib2_version}
Requires:	gtk2-devel >= %{gtk2_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
The libzvt package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

You should install the libzvt-devel package if you would like to
compile applications that use the zvt terminal widget. You do not need
to install libzvt-devel if you just want to use precompiled
applications.

%description devel -l pl
Pliki nag��wkowe potrzebne do kompilowania program�w u�ywaj�cych
libzvt.

%package static
Summary:	Static libzvt library
Summary(pl):	Statyczna biblioteka libzvt
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of libzvt libraries.

%description static -l pl
Statyczna wersja bibliotek libzvt.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(2755,root,utmp) %{_sbindir}/gnome-pty-helper-2

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
