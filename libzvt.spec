%define gtk2_version 1.3.13
%define glib2_version 1.3.13
%define libart_lgpl_version 2.3.8

Summary: Zvt terminal widget library
Name: libzvt
Version: 1.110.0
Release: 1
URL: ftp://ftp.gnome.org
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:  libart_lgpl-devel >= %{libart_lgpl_version}

# Added to avoid the warning messages about utmp group, bug #24171
PreReq:                utempter

%description

The libzvt package contains a terminal widget for GTK+.
It's used by gnome-terminal among other programs.

%package devel
Summary: Libraries and headers for libzvt
Group: Development/Libraries
Requires:	%name = %{version}

Requires:	glib2-devel >= %{glib2_version}
Requires:	gtk2-devel >= %{gtk2_version}
Requires:  libart_lgpl-devel >= %{libart_lgpl_version}

Conflicts: gnome-libs-devel < 1.4.1.2

%description devel

The libzvt package contains a terminal widget for GTK+.
It's used by gnome-terminal among other programs.

You should install the libzvt-devel package if you would like to
compile applications that use the zvt terminal widget. You do not need
to install libzvt-devel if you just want to use precompiled
applications.

%prep
%setup -q -n %{name}-%{version}

%build

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*
%attr(2755, root, utmp) %{_sbindir}/gnome-pty-helper-2

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jan  5 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 snap

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- 1.105.0.90 snap

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- CVS snap, rebuild for glib 1.3.10

* Tue Oct  9 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new CVS snap, rebuild in 7.2-gnome

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- Initial build.
