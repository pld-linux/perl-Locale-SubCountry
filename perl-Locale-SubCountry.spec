#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Locale
%define		pnam	SubCountry
Summary:	Locale::SubCountry - convert state, province, county etc. names to/from code
Summary(pl.UTF-8):   Locale::SubCountry - zamiana nazw stanu, prowincji, kraju itp. na i z kodu
Name:		perl-Locale-SubCountry
Version:	1.34
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	13ab2eeb06fac3f229ec55a7820abfe4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to convert the full name for a countries
administrative region to the code commonly used for postal addressing.
The reverse lookup can also be done. Sub country codes are defined in
"ISO 3166-2:1998, Codes for the representation of names of countries
and their subdivisions".

%description -l pl.UTF-8
Ten moduł pozwala zamieniać pełne nazwy obszarów administracyjnych
krajów na kody pocztowe. Możliwa jest także odwrotna zamiana. Kody
wewnętrzne krajów są zdefiniowane w "ISO 3166-2:1998, Codes for the
representation of names of countries and their subdivisions".

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
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
