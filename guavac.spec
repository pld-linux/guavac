Summary:	A Java compiler written in C++ for high performance.
Name:		guavac
Version:	1.2
Release:	4
Copyright:	GPL
Group:		Development/Languages
Source:		ftp://ftp.yggdrasil.com/pub/dist/devel/compilers/guavac/guavac-1.2.tar.gz
Patch:		guavac-DESTDIR.patch
Url:		http://HTTP.CS.Berkeley.EDU/~engberg/guavac/
Buildroot:	/tmp/%{name}-%{version}-root

%description
The guavac package includes guavac and guavad. Guavac is a
stand-alone compiler for the Java programming language.
Guavac was written entirely in C++ and it should be portable
to any platform supporting GNU's C++ (gcc) or a similar
compiler. Guavad is guavac's disassembler.

Install guavac if you need a Java compiler on your system.

%prep
%setup -q
%patch -p1

%build
%configure
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/guav* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/guav*
%{_datadir}/guavac
%{_mandir}/man*/*
