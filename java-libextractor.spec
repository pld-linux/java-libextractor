#
# Conditional build:
%bcond_with	javac	# use java/javac instead of gij/gcj
#
Summary:	Java support for libextractor
Summary(pl.UTF-8):	Wiązania Javy dla biblioteki libextractor
Name:		java-libextractor
Version:	0.5.18
Release:	1
License:	GPL v2+
Group:		Libraries/Java
Source0:	http://gnunet.org/libextractor/download/libextractor-java-%{version}.tar.gz
# Source0-md5:	e04e9984f0fa09188bab31410a6b3106
Patch0:		libextractor-java-destdir.patch
URL:		http://gnunet.org/libextractor/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libextractor-devel >= %{version}
%if %{with javac}
BuildRequires:	jdk
%else
BuildRequires:	gcc-java
%endif
Requires:	jre
Requires:	libextractor >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java support for libextractor.

%description -l pl.UTF-8
Wiązania Javy dla biblioteki libextractor.

%prep
%setup -q -n libextractor-java-%{version}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
# . in CLASSPATH required for configure test
export CLASSPATH=.
%configure \
	%{!?with_javac:JAVA=gij}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libextractor_java.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libextractor_java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libextractor_java.so.0
%attr(755,root,root) %{_libdir}/libextractor_java.so
%{_javadir}/libextractor.jar
