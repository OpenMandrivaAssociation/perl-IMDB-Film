%define upstream_name IMDB-Film
%define upstream_version 0.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.53
Release:	1

Summary:	OO Perl interface to the database of films IMDB
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/S/ST/STEPANOV/IMDB-Film-0.53.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::FileCache)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Error)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Pod::Checker)
BuildRequires:	perl(Text::Unidecode)
BuildArch:	noarch

%description
IMDB::Film is OO Perl interface to the database of films
IMDB (www.imdb.com). It allows to retrieve information
about movies by its IMDB code or title. Also, there is a 
possibility to get information about IMDB persons (actors,
actresses, directors etc) by their name of code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

%files
%doc README ChangeLog Todo
%{perl_vendorlib}/IMDB
%{_mandir}/man3/*


%changelog
* Sat Nov 06 2010 Anssi Hannula <anssi@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 594191
- new version (makes the module work again)

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2011.0
+ Revision: 526446
- update to 0.45

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.440.0-1mdv2010.1
+ Revision: 523954
- update to 0.44

* Tue Dec 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2010.1
+ Revision: 478792
- update to 0.43

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.1
+ Revision: 461292
- update to 0.42

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.0
+ Revision: 415006
- update to 0.41

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.40-1mdv2010.0
+ Revision: 396132
- new version

* Wed Jul 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2010.0
+ Revision: 393525
- update to new version 0.39

* Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2010.0
+ Revision: 390836
- update to new version 0.37

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.1
+ Revision: 292179
- update to new version 0.34

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2009.0
+ Revision: 220141
- update to new version 0.33

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.32-1mdv2008.1
+ Revision: 144816
- update to new version 0.32

* Thu Dec 27 2007 Anssi Hannula <anssi@mandriva.org> 0.31-1mdv2008.1
+ Revision: 138208
- update to new version 0.31

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2008.1
+ Revision: 97500
- update to new version 0.30

* Thu Jul 19 2007 Anssi Hannula <anssi@mandriva.org> 0.29-1mdv2008.0
+ Revision: 53679
- 0.29

* Fri May 11 2007 Anssi Hannula <anssi@mandriva.org> 0.28-1mdv2008.0
+ Revision: 26411
- 0.28

* Sun Apr 29 2007 Anssi Hannula <anssi@mandriva.org> 0.27-1mdv2008.0
+ Revision: 19142
- Import perl-IMDB-Film


