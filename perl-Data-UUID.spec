%define	modname	Data-UUID
%define modver 1.219

Summary:	Perl extension for generating Globally/Universally Unique Identifiers
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-UUID-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Perl extension for generating Globally/Universally Unique Identifiers
(GUIDs/UUIDs).

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README 
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/man3/*


