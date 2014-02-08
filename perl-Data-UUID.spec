%define	modname	Data-UUID
%define	modver	1.218

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	3

Summary:	Perl extension for generating Globally/Universally Unique Identifiers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Data/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel

%description
Perl extension for generating Globally/Universally Unique Identifiers
(GUIDs/UUIDs).

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README 
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
%{_mandir}/man3/*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.218.0-1
- cleanups
- new version

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.217.0-5mdv2012.0
+ Revision: 765147
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.217.0-4
+ Revision: 763661
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.217.0-3
+ Revision: 762981
- force it
- rebuilt for new perl

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.217.0-2
+ Revision: 667086
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.217.0-1mdv2011.0
+ Revision: 587622
- new version

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.216.0-1mdv2011.0
+ Revision: 576294
- update to 1.216

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.215.0-3mdv2011.0
+ Revision: 564427
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.215.0-2mdv2011.0
+ Revision: 555784
- rebuild for perl 5.12

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.215.0-1mdv2011.0
+ Revision: 553093
- update to 1.215

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.203.0-1mdv2010.1
+ Revision: 461269
- update to 1.203

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.202.0-1mdv2010.0
+ Revision: 392720
- update to 1.202
- using %%perl_convert_version
- fixed license field

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.202-1mdv2010.0
+ Revision: 387002
- update to new version 1.202

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.201-1mdv2010.0
+ Revision: 370048
- update to new version 1.201

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.149-1mdv2009.1
+ Revision: 299376
- update to new version 1.149

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.14.8-4mdv2009.0
+ Revision: 256485
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.14.8-2mdv2008.1
+ Revision: 151442
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14.8-1mdv2008.0
+ Revision: 69247
- revert wrong previous commit
- update to new version 1.148

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.8-1mdv2008.0
+ Revision: 56004
- revert to previous versioning scheme

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.148-1mdv2008.0
+ Revision: 55647
- update to new version 1.148


* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.8-1mdv2007.0
+ Revision: 86554
- new version
- Import perl-Data-UUID

* Fri Sep 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.5-1mdv2007.0
- New version (upstream version 0.145)

* Sat Sep 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.2-1mdv2007.0
- New version (upstream version 0.142)

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-2mdv2007.0
- Rebuild

* Mon Mar 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdk
- New release 0.14

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- New release 0.13
- spec cleanup
- drop patch0 (merged upstream)
- fix directory ownership

* Sat Jan 21 2006 Michael Scherer <misc@mandriva.org> 0.11-4mdk
- fix build on amd64 ( patch0 )

* Fri Nov 18 2005 Michael Scherer <misc@mandriva.org> 0.11-3mdk
- Rebuild
- use %%mkrel and %%check
- fix rpmlint error ( dot in summary )
- fix doc

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.11-2mdk
- Rebuild for new perl

* Thu Apr 29 2004 Michael Scherer <misc@mandrake.org> 0.11-1mdk
- First MandrakeSoft Package
