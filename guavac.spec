Name: guavac
Version: 1.2
Release: 4
Copyright: GPL
Source: ftp://ftp.yggdrasil.com/pub/dist/devel/compilers/guavac/guavac-1.2.tar.gz
Url: http://HTTP.CS.Berkeley.EDU/~engberg/guavac/
Group: Development/Languages
Summary: A Java compiler written in C++ for high performance.
Buildroot: /var/tmp/guavac-root

%description
The guavac package includes guavac and guavad. Guavac is a
stand-alone compiler for the Java programming language.
Guavac was written entirely in C++ and it should be portable
to any platform supporting GNU's C++ (gcc) or a similar
compiler. Guavad is guavac's disassembler.

Install guavac if you need a Java compiler on your system.

%prep
%setup 

%build
%ifarch alpha
CCC=egcs CFLAGS=" " ./configure --prefix=/usr 
%else
CCC=egcs CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
%endif
make CCC=egcs

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
strip $RPM_BUILD_ROOT/usr/bin/guav* || :

%files
/usr/bin/guav*
/usr/man/man*/*
/usr/share/guavac
