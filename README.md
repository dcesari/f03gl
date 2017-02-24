
# F03gl #
> Modules for using the OpenGL graphics library from Fortran

This project is derived from the pioneering work of [Anthony Stone and
Aleksandar Donev](http://www-stone.ch.cam.ac.uk/pub/f03gl/index.xhtml)
for creating a complete Fortran interface to the OpenGL library along
with GLU and GLUT libraries using the F2003 `ISO_C_BINDING` intrinsic
module.

With respect to the original project, this version adds support
for building the package with autoconf/automake/libtool creating
shared libraries and it provides a spec file for building a .rpm
package on a Fedora Linux distribution, thus enhancing the
portability.

You should thus build the package following the usual GNU procedure:

```
# autoreconf -if # only necessary if you download the raw git sources
# ./configure
# make
# make install
```
The package is also available for some versions of Fedora and CentOS distros
as a personal copr repository 
![https://copr.fedorainfracloud.org/coprs/dcesari69/interfortran/package/f03gl/](https://copr.fedorainfracloud.org/coprs/dcesari69/interfortran/package/f03gl/status_image/last_build.png)
Instructions for enabling the repository can be found in the
[interfortran copr project page](https://copr.fedorainfracloud.org/coprs/dcesari69/interfortran/).

The text of the original README is reported here:

```
F03GL -- modules for using the OpenGL graphics library from Fortran

  Copyright 2009 Anthony Stone and Aleksandar Donev

  This file is part of f03gl.

  f03gl is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  any later version.

  f03gl is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with f03gl (see file COPYING). If not, see
  <http://www.gnu.org/licenses/>.


To use this package you need a Fortran 2003 compiler. 

Unpack the files:
  tar xzvf f03gl.tgz
or
  unzip f03gl.zip
The files will be extracted into a new f03gl directory. Change to this
directory. Check that the Makefile is set up to use the correct
compiler and the appropriate libraries. Also set the GLUT variable for
the version of GLUT that you intend to use. Then just run make. This
should compile the OpenGL_gl, OpenGL_glu and OpenGL_glut object and
module files, and then compile and run the test files, one after the
other. You will need to quit from each test before the next one will
run. The first three tests are rather boring, but in the last three
you can bring up a menu with a right mouse click and change some of
the properties of the display. From the f90 code you can see how to do
similar things in your own code. These examples are slightly-modified
versions of the examples provided with Bill Mitchell's f90gl package 
http://math.nist.gov/f90gl/They should run on 64-bit architectures as
well as 32-bit.

Anthony Stone      ajs1 at cam dot ac dot uk
Aleksandar Donev   aleks dot donev at gmail dot com
```
