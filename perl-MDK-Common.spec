%define version 1.2.29
%define release %mkrel 1

Summary:	Various simple functions
%define	module	MDK-Common
Name:		perl-%{module}
Version:	1.2.29
Release:	1
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/perl-MDK-Common/
Source0:	%{module}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Perl
Conflicts:	drakxtools-newt < 9.1-30mdk drakconf < 9.1-14mdk
BuildArch:	noarch

%description
Various simple functions created for DrakX

%prep
%setup -q -n %{module}-%{version}

%build
Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc COPYING tutorial.html 
%{perl_vendorlib}/MDK
%{_mandir}/man*/*
