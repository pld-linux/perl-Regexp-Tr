#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Tr
Summary:	Regexp::Tr - run-time-compiled tr/// objects
Summary(pl):	Regexp::Tr - obiekty tr/// kompilowane w czasie wykonywania
Name:		perl-Regexp-Tr
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c01cb427ae8cfeba5d92fb392336510
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One very useful ability of Perl is to do relatively cheap
transliteration via the tr/// regex operator. Unfortunately, Perl
requires tr/// to be known at compile-time. The common solution has
been to put an eval around any dynamic tr/// operations, but that is
very expensive to be used often (for instance, within a loop). This
module solves that problem by compiling the tr/// a single time and
allowing the user to use it repeatedly and delete it when it it no
longer useful.

%description -l pl
Jedna z bardzo przydatnych mo¿liwo¶ci Perla to w miarê tania zamiana
znaków przez operator tr///. Niestety Perl wymaga, aby tr/// by³o
znane w czasie kompilacji. Popularne rozwi±zanie to otoczenie przez
eval wszystkich dynamicznych operacji tr///, ale ma to bardzo du¿y
narzut czasowy, je¶li jest u¿ywane czêsto (na przyk³ad w pêtli). Ten
modu³ rozwi±zuje problem poprzez kompilowanie wyra¿enia tr/// jeden
raz, a nastêpnie pozwolenie u¿ytkownikowi na wielokrotne u¿ywanie go
i usuniêcie, kiedy przestaje byæ potrzebne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Regexp/Tr.pm
%{_mandir}/man3/*
