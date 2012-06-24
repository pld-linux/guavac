Summary:	A Java compiler written in C++ for high performance.
Summary(pl):	Kompiler Javy napisany w C++ 
Name:		guavac
Version:	1.2
Release:	4
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Source0:	ftp://ftp.yggdrasil.com/pub/dist/devel/compilers/guavac/%{name}-%{version}.tar.gz
Patch0:		guavac-DESTDIR.patch
Url:		http://HTTP.CS.Berkeley.EDU/~engberg/guavac/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The guavac package includes guavac and guavad. Guavac is a stand-alone
compiler for the Java programming language. Guavac was written
entirely in C++ and it should be portable to any platform supporting
GNU's C++ (gcc) or a similar compiler. Guavad is guavac's
disassembler.

Install guavac if you need a Java compiler on your system.

%description -l pl
Pakiet guavac zawiera guavac i guavad. Guavac jest samodzielnym
kompilatorem Javy; zosta� w ca�o�ci napisany w C++ i powinien da� si�
skompilowa� na ka�dej platformie, na kt�rej dzia�a GNU C++ (ggc) lub
podobny kompilator. Guavad to deasembler guavac. Nale�y zainstalowa�
guavac je�li potzrebuje si� kompilatora Javy.

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
