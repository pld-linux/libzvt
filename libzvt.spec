%define		gtk2_version		2.0.3
%define		glib2_version		2.0.3
%define		libart_lgpl_version	2.3.8

Summary:	Zvt terminal widget library
Summary(pl):	Biblioteka z widgetem terminala zvt
Name:		libzvt
Version:	2.0.1
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libzvt/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am15.patch
Patch1:		%{name}-i18n-branch.patch
URL:		ftp://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gtk+2-devel >= %{gtk2_version}
BuildRequires:	libart_lgpl-devel >= %{libart_lgpl_version}
BuildRequires:	libtool
BuildRequires:	gnome-common
PreReq:		utempter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
The libzvt package contains a terminal widget for GTK+. It's used by
gnome-terminal among other programs.

%description -l pl
Ten pakiet zawiera widget terminala dla GTK+. Jest u¿ywany przez
gnome-terminal oraz inne programy.

%package devel
Summary:	Headers for libzvt
Summary(pl):	Pliki nag³ówkowe libzvt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= %{glib2_version}
Requires:	gtk+2-devel >= %{gtk2_version}
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
Pliki nag³ówkowe potrzebne do kompilowania programów u¿ywaj±cych
libzvt.

%package static
Summary:	Static libzvt library
Summary(pl):	Statyczna biblioteka libzvt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of libzvt libraries.

%description static -l pl
Statyczna wersja bibliotek libzvt.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
rm -f missing
%{__libtoolize}
aclocal -I %{_aclocaldir}/gnome2-macros
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
