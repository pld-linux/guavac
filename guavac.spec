Summary:	A Java compiler written in C++ for high performance
Summary(de):	Java-JVM-Compiler in C++
Summary(es):	Compilador java -> JVM escrito en C++ para optimizar desempeño
Summary(fr):	Compilateur Java -> JVM ecrit en C++ pour de grandes performances
Summary(pl):	Kompilator Javy napisany w C++
Summary(pt_BR):	Compilador java -> JVM escrito em C++ para otimizar performance
Summary(tr):	Java derleyicisi
Name:		guavac
Version:	1.2
Release:	6
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.yggdrasil.com/pub/dist/devel/compilers/guavac/%{name}-%{version}.tar.gz
# Source0-md5:	06b7391584fc6b22db7f16fc0a2f9b3e
Patch0:		%{name}-DESTDIR.patch
URL:		http://HTTP.CS.Berkeley.EDU/~engberg/guavac/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The guavac package includes guavac and guavad. Guavac is a stand-alone
compiler for the Java programming language. Guavac was written
entirely in C++ and it should be portable to any platform supporting
GNU's C++ (gcc) or a similar compiler. Guavad is guavac's
disassembler.

%description -l es
Guavac es un compilador para el lenguaje de programación Java. Fue
escrito enteramente en C++, y debe ser portátil para cualquier
plataforma que tiene un compilador C++ Gnu o un similar.

%description -l de
Guavac ist ein selbständiger Compiler für die Java-Programmiersprache.
Komplett in C++ geschrieben, läßt er sich auf jede Plattform
übernehmen, die den C++-Compiler von GNU oder ein ähnliches System
unterstützt.

%description -l fr
Guavac est un compilateur autonome du langage de programmation Java.
Il a été entièrement écrit en C++ et peut être porté sur toutes les
plates-formes qui disposent du compilateur C++ de GNU, ou d'un système
équivalent

%description -l pl
Pakiet guavac zawiera guavac i guavad. Guavac jest samodzielnym
kompilatorem Javy; zosta³ w ca³o¶ci napisany w C++ i powinien daæ siê
skompilowaæ na ka¿dej platformie, na której dzia³a GNU C++ (ggc) lub
podobny kompilator. Guavad to deasembler guavac. Nale¿y zainstalowaæ
guavac je¶li potzrebuje siê kompilatora Javy.

%description -l pt_BR
Guavac é um compilador para a linguagem de programação Java. Ele foi
escrito inteiramente em C++, e deve ser portátil para qualquer
plataforma que tem um compilador C++ Gnu ou um similar.

%description -l tr
Guavac tek baþýna çalýþan bir Java dili derleyicisidir. Tamamen C++
ile yazýlmýþtýr.

%prep
%setup -q
%patch -p1

%build
CFLAGS="%{rpmcflags} -fno-exceptions"
%configure2_13
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/guav*
%{_datadir}/guavac
%{_mandir}/man*/*
