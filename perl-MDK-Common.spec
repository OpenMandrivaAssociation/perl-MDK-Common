%define version 1.2.27
%define release %mkrel 3

Summary: Various simple functions
Name: perl-MDK-Common
Version: %{version}
Release: %{release}
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/perl-MDK-Common/
Source0: MDK-Common-%version.tar.bz2
License: GPLv2+
Group: Development/Perl
Conflicts: drakxtools-newt < 9.1-30mdk, drakconf < 9.1-14mdk
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
Various simple functions created for DrakX

%prep
%setup -q -n MDK-Common-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING tutorial.html 
%{perl_vendorlib}/MDK
%{_mandir}/man*/*
