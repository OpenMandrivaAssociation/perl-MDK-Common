%define module MDK-Common

Summary:	Various simple functions
Name:		perl-%{module}
Version:	1.2.29
Release:	14
License:	GPLv2+
Group:		Development/Perl
Url:		https://abf.io/omv_software/perl-MDK-Common
Source0:	%{module}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	perl-JSON-PP
BuildRequires:	perl-devel

%description
Various simple functions created for DrakX.

%prep
%setup -qn %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc tutorial.html 
%{perl_vendorlib}/MDK
%{_mandir}/man3/*

