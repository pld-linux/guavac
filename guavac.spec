Summary:	A Java compiler written in C++ for high performance
Summary(de):	Java-JVM-Compiler in C++
Summary(es):	Compilador java -> JVM escrito en C++ para optimizar desempe�o
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
Guavac es un compilador para el lenguaje de programaci�n Java. Fue
escrito enteramente en C++, y debe ser port�til para cualquier
plataforma que tiene un compilador C++ Gnu o un similar.

%description -l de
Guavac ist ein selbst�ndiger Compiler f�r die Java-Programmiersprache.
Komplett in C++ geschrieben, l��t er sich auf jede Plattform
�bernehmen, die den C++-Compiler von GNU oder ein �hnliches System
unterst�tzt.

%description -l fr
Guavac est un compilateur autonome du langage de programmation Java.
Il a �t� enti�rement �crit en C++ et peut �tre port� sur toutes les
plates-formes qui disposent du compilateur C++ de GNU, ou d'un syst�me
�quivalent

%description -l pl
Pakiet guavac zawiera guavac i guavad. Guavac jest samodzielnym
kompilatorem Javy; zosta� w ca�o�ci napisany w C++ i powinien da� si�
skompilowa� na ka�dej platformie, na kt�rej dzia�a GNU C++ (ggc) lub
podobny kompilator. Guavad to deasembler guavac. Nale�y zainstalowa�
guavac je�li potzrebuje si� kompilatora Javy.

%description -l pt_BR
Guavac � um compilador para a linguagem de programa��o Java. Ele foi
escrito inteiramente em C++, e deve ser port�til para qualquer
plataforma que tem um compilador C++ Gnu ou um similar.

%description -l tr
Guavac tek ba��na �al��an bir Java dili derleyicisidir. Tamamen C++
ile yaz�lm��t�r.

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
