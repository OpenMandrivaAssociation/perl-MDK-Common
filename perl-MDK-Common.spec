%define module MDK-Common

Summary:	Various simple functions
Name:		perl-%{module}
Version:	1.2.31.1
Release:	1
License:	GPLv2+
Group:		Development/Perl
Url:		https://abf.io/software/perl-MDK-Common
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

