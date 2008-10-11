
%define module	IMDB-Film
%define name	perl-%{module}
%define version	0.34
%define rel	1

Summary:	OO Perl interface to the database of films IMDB
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/S/ST/STEPANOV/%{module}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
IMDB::Film is OO Perl interface to the database of films
IMDB (www.imdb.com). It allows to retrieve information
about movies by its IMDB code or title. Also, there is a 
possibility to get information about IMDB persons (actors,
actresses, directors etc) by their name of code.

%prep
%setup -q -n %{module}-%{version}

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
