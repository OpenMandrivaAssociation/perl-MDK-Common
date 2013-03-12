%define module MDK-Common

Summary:	Various simple functions
Name:		perl-%{module}
Version:	1.2.29
Release:	3
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/perl-MDK-Common/
Source0:	%{module}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Perl
BuildRequires:	perl-JSON-PP
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Various simple functions created for DrakX.

%prep
%setup -q -n %{module}-%{version}

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
%{_mandir}/man*/*

