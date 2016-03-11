Summary: Fortran 2003 bindings for OpenGL
Name: f03gl
Version: 2.0
Release: 1%{dist}
License: GPLv3
Group: System Environment/Libraries
URL: http://www-stone.ch.cam.ac.uk/pub/f03gl/index.xhtml
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: mesa-libGL-devel, mesa-libGLU-devel, freeglut-devel

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
%configure --disable-examples
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
%{_libdir}/*.la
%{_libdir}/*.so*
##%{_docdir}/%{name}-%{version}/*
%doc README

%files devel
%{_fmoddir}/GL/*.mod
%{_libdir}/*.a

%changelog
* Fri Mar 11 2016 Davide Cesari <dcesari@malina.metarpa> - 2.0-1
- New version with clear license

* Fri Sep 18 2009 root <root@spider.metarpa> - 1.0-1
- First rpm build
