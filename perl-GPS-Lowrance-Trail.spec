%define upstream_name    GPS-Lowrance-Trail
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Convert between GDM16 Trails and other formats
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/GPS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Assert)
BuildRequires: perl(Geo::Coordinates::DecimalDegrees)
BuildRequires: perl(Geo::Coordinates::UTM)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(XML::Generator)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

