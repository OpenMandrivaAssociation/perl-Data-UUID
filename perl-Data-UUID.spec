# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname Data-UUID
%define modver 1.224

Summary:	Perl extension for generating Globally/Universally Unique Identifiers
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-UUID-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Perl extension for generating Globally/Universally Unique Identifiers
(GUIDs/UUIDs).

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make_build

%install
%make_install

%files
%doc Changes README 
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%doc %{_mandir}/man3/*
