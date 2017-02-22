dnl Process this file with autoconf to produce a configure script.

AC_INIT(f03gl, 2.1,)
dnl AC_CONFIG_HEADERS([config.h])
AC_CONFIG_SRCDIR([configure.ac])
AM_INIT_AUTOMAKE([foreign])
AC_CONFIG_MACRO_DIR([m4])

AC_LANG([C])

dnl Detect X Window system
AC_PATH_XTRA
LIBS="$LIBS $X_LIBS"
CFLAGS="$CFLAGS $X_CFLAGS"
CXXFLAGS="$CXXFLAGS $X_CFLAGS"

dnl Check for OpenGL headers and library
dnl AC_CHECK_HEADERS([GL/gl.h OpenGL/gl.h])
AC_CHECK_LIB([GL],[glBegin],, AC_MSG_ERROR([OpenGL library not found]),)

dnl AC_CHECK_HEADERS([GL/glu.h OpenGL/glu.h])
AC_CHECK_LIB([GLU], [gluPerspective],, AC_MSG_ERROR([GLU library not found]),)
dnl AC_CHECK_LIB([GLU], [gluPerspective],
dnl  glu=yes
dnl  GLU_LIBS="-lGLU"
dnl  AC_SUBST(GLU_LIBS)
dnl  AC_DEFINE(HAVE_LIBGLU, 1, [Enable GLU]),
dnl  AC_MSG_RESULT([GLU library not found]), )

AC_CHECK_HEADERS([GL/glut.h OpenGL/glut.h])
AC_CHECK_LIB([glut], [glutInit],, AC_MSG_ERROR([glut/freeglut/openglut library not found]),)
dnl AC_CHECK_LIB([glut], [glutInit],
dnl  glut=yes
dnl  GLUT_LIBS="-lglut"
dnl  AC_SUBST(GLUT_LIBS)
dnl  AC_DEFINE(HAVE_LIBGLU, 1, [Enable GLUT]),
dnl  AC_MSG_RESULT([GLUT library not found]), )
dnl #define  FREEGLUT             1
dnl  __OPENGLUT_H__
dnl #define OPENGLUT

AC_ARG_ENABLE(glut_type, AC_HELP_STRING([--glut-type],
[select glut type: glut, openglut, freeglut, openglut.nullfunc, freeglut.nullfunc, default autodetected]),,[enableval=])dnl default empty

GLUT_TYPE=$enableval
if  test "x$GLUT_TYPE" = "x"; then
dnl autodetect

AC_CHECK_DECL(FREEGLUT,
GLUT_TYPE=freeglut
AC_MSG_RESULT([Using Freeglut]),,
[#include <GL/glut.h>])

AC_CHECK_DECL(OPENGLUT,
GLUT_TYPE=openglut
AC_MSG_RESULT([Using Openglut]),,
[#include <GL/glut.h>])

fi

AM_CONDITIONAL(GLUT_glut, test "x$GLUT_TYPE" = "xglut")
AM_CONDITIONAL(GLUT_openglut, test "x$GLUT_TYPE" = "xopenglut")
AM_CONDITIONAL(GLUT_freeglut, test "x$GLUT_TYPE" = "xfreeglut")
AM_CONDITIONAL(GLUT_glut_nullfunc, test "x$GLUT_TYPE" = "xglut.nullfunc")
AM_CONDITIONAL(GLUT_openglut_nullfunc, test "x$GLUT_TYPE" = "xopenglut.nullfunc")
AM_CONDITIONAL(GLUT_freeglut_nullfunc, test "x$GLUT_TYPE" = "xfreeglut.nullfunc")
AM_CONDITIONAL(GLUT_sgiglut, test "x$GLUT_TYPE" = "xglut" -o "x$GLUT_TYPE" = "xglut.nullfunc")

AC_ARG_ENABLE(examples, AC_HELP_STRING([--disable-examples],
[disable build of examples]),,
[enableval=yes])dnl default enable
AM_CONDITIONAL(DO_EXAMPLES, test "x$enableval" = "xyes")

dnl Locate Fortran 90 compiler among these if not specified
AC_PROG_FC([gfortran g95 pgf90 pgf95 ifort xlf90 xlf95 f90 f95])
dnl add any compiler-specific option here
if test "x$FC" = "xgfortran"; then
 FCFLAGS="$FCFLAGS -fno-range-check"
fi

AC_LANG_PUSH(Fortran)dnl Do the following checks in Fortran
AC_FC_SRCEXT(f90)dnl and use .f90 extension

AC_COMPILE_IFELSE(
  [AC_LANG_PROGRAM(,[[      USE, INTRINSIC :: ISO_C_BINDING]])],
  [AC_MSG_RESULT([ISO_C_BINDING f03 module available!])],
  [AC_MSG_ERROR([Your compiler seems not to support the F2003 ISO_C_BINDING module for interfacing to C, please add any compiler flag that can enable this feature or upgrade your compiler!])])

dnl F77=$FC
dnl FFLAGS=$FCFLAGS


AC_PROG_LIBTOOL

pkgdocdir='${datadir}/doc/${PACKAGE}-${VERSION}'
AC_SUBST(pkgdocdir)

AC_CONFIG_FILES([
Makefile
])

AC_OUTPUT
