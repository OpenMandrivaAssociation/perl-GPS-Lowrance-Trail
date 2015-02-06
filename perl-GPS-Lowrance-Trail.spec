%define upstream_name    GPS-Lowrance-Trail
%define upstream_version 0.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Convert between GDM16 Trails and other formats
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GPS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Assert)
BuildRequires:	perl(Geo::Coordinates::DecimalDegrees)
BuildRequires:	perl(Geo::Coordinates::UTM)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(XML::Generator)
BuildArch:	noarch

%description
This module allows one to convert between Lowrance GPS trail files (handled
by their GDM16 application), Latitude/Longitude (or "Lat/Lon") files, UTM,
and GPX files which may be used by mapping applications.

Methods
    The following methods are implemented.
    * new

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.430.0-2mdv2011.0
+ Revision: 654966
- rebuild for updated spec-helper

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 381801
- adding missing buildrequires:
- import perl-GPS-Lowrance-Trail


* Sun May 31 2009 cpan2dist 0.43-1mdv
- initial mdv release, generated with cpan2dist

