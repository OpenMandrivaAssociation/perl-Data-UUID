%define module	Data-UUID
%define name	perl-%{module}
%define version 1.14.8
%define up_version 0.148
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl extension for generating Globally/Universally Unique Identifiers
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Data/%{module}-%{up_version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl extension for generating Globally/Universally Unique Identifiers
(GUIDs/UUIDs).

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README 
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/man3/*


