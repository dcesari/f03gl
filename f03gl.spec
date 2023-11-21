Summary: Fortran 2003 bindings for OpenGL
Name: f03gl
Version: 2.1
Release: 5%{dist}
License: GPLv3
Group: System Environment/Libraries
URL: http://www-stone.ch.cam.ac.uk/pub/f03gl/index.xhtml
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-gfortran, mesa-libGL-devel, mesa-libGLU-devel, freeglut-devel, libtool

%package devel

Group: Deelopment/Libraries
Summary: Static libraries and modules for f03gl.

%description

A Fortran 2003 interface to the OpenGL library,
along with the GLU and GLUT toolkits.

%description devel

A Fortran 2003 interface to the OpenGL library,
along with the GLU and GLUT toolkits, devel package.

%prep
%setup -q

%build
autoreconf -ifv
%configure --disable-examples --disable-static
make

%install
make DESTDIR=%{buildroot} install
mkdir -p ${RPM_BUILD_ROOT}%{_fmoddir}/GL
/bin/mv ${RPM_BUILD_ROOT}%{_includedir}/GL/*.mod  \
  ${RPM_BUILD_ROOT}%{_fmoddir}/GL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
#doc   COPYING README.md
%{_docdir}/%{name}-%{version}/*

%files devel
%{_fmoddir}/GL/*.mod
#{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so*

%changelog
* Wed Feb 22 2017 dcesari <dcesari@arpae.it> 2.1-4
- add dep on libtool (dcesari@arpae.it)

* Wed Feb 22 2017 Davide Cesari <dcesari@arpae.it> 2.1-3
- tito update release (dcesari@arpae.it)

* Wed Feb 22 2017 Davide Cesari <dcesari@arpae.it> 2.1-2
- update version by hand for tito build (dcesari@arpae.it)
- add autoreconf for git/tito build (dcesari@arpae.it)

* Wed Feb 22 2017 Davide Cesari <dcesari@arpae.it>
- new package built with tito

* Fri Mar 11 2016 Davide Cesari <dcesari@malina.metarpa> - 2.0-1
- New version with clear license

* Fri Sep 18 2009 root <root@spider.metarpa> - 1.0-1
- First rpm build

