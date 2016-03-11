ACLOCAL_AMFLAGS = -I m4

lib_LTLIBRARIES = libf03gl.la

libf03gl_la_SOURCES = OpenGL_gl.f90 OpenGL_glu.f90 GLUT_fonts.c
libf03gl_la_LIBADD = $(LIBS)

AM_FCFLAGS = -I.

# USE-depenencies
OpenGL_glu.$(OBJEXT): OpenGL_gl.$(OBJEXT)
OpenGL_glu.lo: OpenGL_gl.$(OBJEXT)

if GLUT_glut
libf03gl_la_SOURCES += OpenGL_glut.f90
OpenGL_glut.$(OBJEXT): OpenGL_gl.$(OBJEXT)
OpenGL_glut.lo: OpenGL_gl.$(OBJEXT)
endif
if GLUT_openglut
libf03gl_la_SOURCES += OpenGL_openglut.f90
OpenGL_openglut.$(OBJEXT): OpenGL_gl.$(OBJEXT)
OpenGL_openglut.lo: OpenGL_gl.$(OBJEXT)
endif
if GLUT_freeglut
libf03gl_la_SOURCES += OpenGL_freeglut.f90
OpenGL_freeglut.$(OBJEXT): OpenGL_gl.$(OBJEXT)
OpenGL_freeglut.lo: OpenGL_gl.$(OBJEXT)
endif
#if GLUT_glut_nullfunc
#libf03gl_la_SOURCES += OpenGL_glut.nullfunc.f90
#OpenGL_glut.nullfunc.$(OBJEXT): OpenGL_gl.$(OBJEXT)
#OpenGL_glut.nullfunc.lo: OpenGL_gl.$(OBJEXT)
#endif
if GLUT_openglut_nullfunc
libf03gl_la_SOURCES += OpenGL_openglut.nullfunc.f90
OpenGL_openglut.nullfunc.$(OBJEXT): OpenGL_gl.$(OBJEXT)
OpenGL_openglut.nullfunc.lo: OpenGL_gl.$(OBJEXT)
endif
if GLUT_freeglut_nullfunc
libf03gl_la_SOURCES += OpenGL_freeglut.nullfunc.f90
OpenGL_freeglut.nullfunc.$(OBJEXT): OpenGL_gl.$(OBJEXT)
OpenGL_freeglut.nullfunc.lo: OpenGL_gl.$(OBJEXT)
endif

OpenGL_glut.o: OpenGL_gl.o
OpenGL_openglut.o: OpenGL_gl.o
OpenGL_freeglut.o: OpenGL_gl.o
#OpenGL_glut.nullfunc.o: OpenGL_gl.o
OpenGL_openglut.nullfunc.o: OpenGL_gl.o
OpenGL_freeglut.nullfunc.o: OpenGL_gl.o

noinst_PROGRAMS =
if DO_EXAMPLES
noinst_PROGRAMS += sphere stars blender scube modview plotfunc

sphere_SOURCES = sphere.f90
sphere_LDADD = libf03gl.la

stars_SOURCES = stars.f90
stars_LDADD = libf03gl.la

blender_SOURCES = blender.f90
blender_LDADD = libf03gl.la

scube_SOURCES = scube.f90
scube_LDADD = libf03gl.la

modview_SOURCES = modview.f90
modview_LDADD = libf03gl.la

plotfunc_SOURCES = plotfunc.f90
plotfunc_LDADD = libf03gl.la

if GLUT_sgiglut
noinst_PROGRAMS += RandomSphere_GLUT
RandomSphere_GLUT_SOURCES = RandomSphere_GLUT.f90
RandomSphere_GLUT_LDADD = libf03gl.la
else
noinst_PROGRAMS += RandomSphere_OpenGLUT
RandomSphere_OpenGLUT_SOURCES = RandomSphere_OpenGLUT.f90
RandomSphere_OpenGLUT_LDADD = libf03gl.la
endif
endif

glincludedir = $(includedir)/GL
# should detect module extension in autoconf
nodist_glinclude_HEADERS = opengl_gl.mod opengl_glu.mod opengl_glut.mod \
 opengl_kinds.mod

# additional files to be packaged and installed
dist_pkgdoc_DATA = README.md COPYING
# additional files to be packaged but not installed
dist_noinst_DATA = FreeGLUT.h GL.h GLU.h GLUT.h OpenGLUT.h \
 enumglu.spec enum.spec gl.spec glu.spec f03gl.spec Script.sh \
 glut_interfaces.pl spec_interfaces.pl h_interfaces.glutnullfunc.pl h_interfaces.pl

mostlyclean-compile:
	-rm -f *.$(OBJEXT) *.mod
