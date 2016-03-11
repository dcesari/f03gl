#  Copyright 2009 Anthony Stone and Aleksandar Donev

#  This file is part of f03gl.
#
#  f03gl is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#  f03gl is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with f03gl (see file COPYING). If not, see
#  <http://www.gnu.org/licenses/>.



#  Comment out for 32-bit architecture
BITS      := 64

#  The directories containing the OpenGL libraries and GLUT libraries
OGLLIBDIR := -L/usr/lib${BITS}

#  The directory containing the X11 libraries
X11LIBDIR := -L/usr/X11R6/lib${BITS}

#  Libraries for OpenGL, including GLUT, GLU and OpenGL
F90GLUTLIB := -lglut -lGL -lGLU

#  The X11 libraries
X11LIB := -lXaw -lXt -lXmu -lXi -lXext -lX11 -lm -lXxf86vm

ifndef COMPILER
  COMPILER := nagfor
endif
FC=${COMPILER}
ifeq (${COMPILER},nagfor)
#  Nag nagfor compiler, version 5.2
  FFLAGS    := $(DEBUG) -f2003 -colour -gline -DNAGF95 -DF2003 -DOPENGL
  LIBRARIES := ${OGLLIBDIR} ${X11LIBDIR} -L/usr/local/lib${BITS}
  LIBS      := ${F90GLUTLIB} ${X11LIB} -lpthread -ldl
endif
ifeq (${COMPILER},gfortran)
#  Gfortran version 4.5.0
  FFLAGS    := $(DEBUG) -DOPENGL -fno-range-check
  LIBRARIES := ${OGLLIBDIR} ${X11LIBDIR} -L/usr/local/lib${BITS} -L/home/ajs1/gcc-20090906/lib${BITS}
  LIBS      := ${F90GLUTLIB} ${X11LIB} -lpthread -ldl -lgfortran
endif
ifeq (${COMPILER},ifort)
#  ifort compiler, version 11.1.059 or later.
  FFLAGS    := $(DEBUG) -DOPENGL
  LIBRARIES := ${OGLLIBDIR} ${X11LIBDIR} -L/usr/local/lib${BITS}
  LIBS      := ${F90GLUTLIB} ${X11LIB} -lpthread -ldl
endif

#  If you use OpenGLUT or FreeGlut, change this variable and adjust
#  the libraries appropriately.
# GLUT      := glut
# GLUT      := openglut
GLUT      := freeglut

LIBRARIES := ${OGLLIBDIR} ${X11LIBDIR} -L/usr/local/lib
MODULES    = GLUT_fonts.o OpenGL_${GLUT}.o OpenGL_glu.o OpenGL_gl.o 


all: sphere stars blender scube modview plotfunc

%.o: %.f90
	${FC} ${FFLAGS} -c $<

blender modview plotfunc scube sphere stars : %: %.f90 ${MODULES} force
	${FC} ${FFLAGS} -c $<
	${FC} $@.o ${MODULES} ${LIBRARIES} ${LIBS} -o $@
	./$@

OpenGL%.mod: OpenGL%.f90
	${FC} ${FFLAGS} -c $<

force:

OpenGL_${GLUT}.o OpenGL_glu.o: OpenGL_gl.o

clean:
	-rm -f *.mod *.o

