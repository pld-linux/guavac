Summary:	A Java compiler written in C++ for high performance
Summary(de.UTF-8):	Java-JVM-Compiler in C++
Summary(es.UTF-8):	Compilador java -> JVM escrito en C++ para optimizar desempeño
Summary(fr.UTF-8):	Compilateur Java -> JVM ecrit en C++ pour de grandes performances
Summary(pl.UTF-8):	Kompilator Javy napisany w C++
Summary(pt_BR.UTF-8):	Compilador java -> JVM escrito em C++ para otimizar performance
Summary(tr.UTF-8):	Java derleyicisi
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

%description -l es.UTF-8
Guavac es un compilador para el lenguaje de programación Java. Fue
escrito enteramente en C++, y debe ser portátil para cualquier
plataforma que tiene un compilador C++ Gnu o un similar.

%description -l de.UTF-8
Guavac ist ein selbständiger Compiler für die Java-Programmiersprache.
Komplett in C++ geschrieben, läßt er sich auf jede Plattform
übernehmen, die den C++-Compiler von GNU oder ein ähnliches System
unterstützt.

%description -l fr.UTF-8
Guavac est un compilateur autonome du langage de programmation Java.
Il a été entièrement écrit en C++ et peut être porté sur toutes les
plates-formes qui disposent du compilateur C++ de GNU, ou d'un système
équivalent

%description -l pl.UTF-8
Pakiet guavac zawiera guavac i guavad. Guavac jest samodzielnym
kompilatorem Javy; został w całości napisany w C++ i powinien dać się
skompilować na każdej platformie, na której działa GNU C++ (ggc) lub
podobny kompilator. Guavad to deasembler guavac. Należy zainstalować
guavac jeśli potrzebuje się kompilatora Javy.

%description -l pt_BR.UTF-8
Guavac é um compilador para a linguagem de programação Java. Ele foi
escrito inteiramente em C++, e deve ser portátil para qualquer
plataforma que tem um compilador C++ Gnu ou um similar.

%description -l tr.UTF-8
Guavac tek başına çalışan bir Java dili derleyicisidir. Tamamen C++
ile yazılmıştır.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -fno-exceptions"
%configure2_13
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/guav*
%{_datadir}/%{name}
%{_mandir}/man*/*
