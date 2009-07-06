%define upstream_name	 Data-UUID
%define upstream_version 1.202

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary: Perl extension for generating Globally/Universally Unique Identifiers
License: GPL+ or Artistic
Group:	 Development/Perl
Url:     http://search.cpan.org/dist/%{upstream_name}
Source0: http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl extension for generating Globally/Universally Unique Identifiers
(GUIDs/UUIDs).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


