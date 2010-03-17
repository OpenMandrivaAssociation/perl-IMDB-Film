%define upstream_name	 IMDB-Film
%define upstream_version 0.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	OO Perl interface to the database of films IMDB
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/ST/STEPANOV/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
IMDB::Film is OO Perl interface to the database of films
IMDB (www.imdb.com). It allows to retrieve information
about movies by its IMDB code or title. Also, there is a 
possibility to get information about IMDB persons (actors,
actresses, directors etc) by their name of code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog Todo
%{perl_vendorlib}/IMDB
%{_mandir}/man3/*
