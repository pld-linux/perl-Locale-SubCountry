#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	SubCountry
Summary:	Locale::SubCountry - convert state, province, county etc. names to/from code
Summary(pl):	Locale::SubCountry - zamiana nazw stanu, prowincji, kraju itp. na i z kodu
Name:		perl-Locale-SubCountry
Version:	1.23
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c11d9382ba9ae13ea3f37ec8ac884b0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to convert the full name for a countries
administrative region to the code commonly used for postal addressing.
The reverse lookup can also be done. Sub country codes are defined in
"ISO 3166-2:1998, Codes for the representation of names of countries
and their subdivisions".

%description -l pl
Ten modu� pozwala zamienia� pe�ne nazwy obszar�w administracyjnych
kraj�w na kody pocztowe. Mo�liwa jest tak�e odwrotna zamiana. Kody
wewn�trzne kraj�w s� zdefiniowane w "ISO 3166-2:1998, Codes for the
representation of names of countries and their subdivisions".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
