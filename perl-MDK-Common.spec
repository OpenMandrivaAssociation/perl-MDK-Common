Summary:	Various simple functions
%define	module	MDK-Common
Name:		perl-%{module}
Version:	1.2.29
Release:	1
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/perl-MDK-Common/
Source0:	%{module}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Perl
BuildArch:	noarch

%description
Various simple functions created for DrakX

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

%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.29-1
- drop 'COPYING' as it's shipped with common-licenses
- drop ancient conflicts
- cleanups
- new version:
        o fix namespace in doc
        o substInFile: fix writing to zero-sized or nonexistent files (#460),
          eof does not seem to return true anymore for filehandles vivified
          through select  (behavior change seems introduced by upstream perl
          commit 32e653230c7ccc7fa595b1ab68502c6eb66ff980)

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.27-6mdv2012.0
+ Revision: 765478
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.27-5
+ Revision: 763972
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.27-4
+ Revision: 763088
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.27-3
+ Revision: 667226
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 1.2.27-2
+ Revision: 650046
- rebuild

* Wed Feb 02 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.27-1
+ Revision: 635301
- 1.2.27:
- add cp_afx command to copy files without crossing file systems

* Sun Oct 24 2010 Thierry Vignaud <tv@mandriva.org> 1.2.26.1-1mdv2011.0
+ Revision: 587837
- fix URL
- fix license tag
- append_to_file: better error message making easier to pinpoint actual place
  of error

* Thu Sep 09 2010 Funda Wang <fwang@mandriva.org> 1.2.26-3mdv2011.0
+ Revision: 576980
- rebuild for new perl

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 1.2.26-2mdv2011.0
+ Revision: 556961
- rebuild

* Tue Jul 20 2010 Thierry Vignaud <tv@mandriva.org> 1.2.26-1mdv2011.0
+ Revision: 555137
- if_, if__: make easier to debug (#60153)

* Wed Jun 02 2010 Pascal Terjan <pterjan@mandriva.org> 1.2.25-1mdv2010.1
+ Revision: 546928
- preserve sockets and pipes in cp_af

* Tue Jan 12 2010 Pascal Terjan <pterjan@mandriva.org> 1.2.24-1mdv2010.1
+ Revision: 490236
- fix whereis_binary to work on absolute symlinks inside chroot

* Mon Dec 14 2009 Pascal Terjan <pterjan@mandriva.org> 1.2.23-1mdv2010.1
+ Revision: 478550
- get available size of requested partition not / in df

* Tue Dec 01 2009 Thierry Vignaud <tv@mandriva.org> 1.2.22-1mdv2010.1
+ Revision: 472293
- use a more portable df()
- substInFile:
  o do not unlink the symlink to recreate it later to the same target

* Wed Oct 07 2009 Thierry Vignaud <tv@mandriva.org> 1.2.21-1mdv2010.0
+ Revision: 455651
- substInFile:
  o ensure we keep old file as file.bak until we wrote new file
  o call fsync() when editing a non empty file

* Wed Oct 07 2009 Thierry Vignaud <tv@mandriva.org> 1.2.20-1mdv2010.0
+ Revision: 455637
- Call fsync after writing to ensure that files are written
- fix df on mips, statfs structure is different from x86

* Tue Jun 09 2009 Eugeni Dodonov <eugeni@mandriva.com> 1.2.19-1mdv2010.0
+ Revision: 384410
- 1.2.19:
- Correctly handling '#' when loading shell variables (#50670, #51457).

* Tue Apr 14 2009 Pascal Terjan <pterjan@mandriva.org> 1.2.18-1mdv2009.1
+ Revision: 367145
- decode ' inside '' properly in getVarsFromSh

* Wed Mar 11 2009 Pascal Terjan <pterjan@mandriva.org> 1.2.17-1mdv2009.1
+ Revision: 353717
- quote correctly ' inside ''
- protect various chars in setExportedVarsInSh and setExportedVarsInCsh

* Mon Feb 02 2009 Pascal Terjan <pterjan@mandriva.org> 1.2.16-1mdv2009.1
+ Revision: 336379
- Protect more things in setVarsInSh

* Mon Jan 26 2009 Pascal Terjan <pterjan@mandriva.org> 1.2.15-1mdv2009.1
+ Revision: 333652
- protect parenthesis in setVarsInSh (#47298)

* Wed Oct 01 2008 Pixel <pixel@mandriva.com> 1.2.14-1mdv2009.0
+ Revision: 290314
- 1.2.14:
- round_up(), round_down(): workaround "Illegal modulus zero" (#43165)

* Tue Sep 09 2008 Pixel <pixel@mandriva.com> 1.2.13-1mdv2009.0
+ Revision: 283136
- 1.2.13: export cat_utf8() and cat_utf8_or_die()

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.12-2mdv2009.0
+ Revision: 223817
- rebuild

* Thu Apr 03 2008 Olivier Blin <blino@mandriva.org> 1.2.12-1mdv2008.1
+ Revision: 192186
- 1.2.12
- fix crash introduced in previous release

* Thu Apr 03 2008 Olivier Blin <blino@mandriva.org> 1.2.11-1mdv2008.1
+ Revision: 192038
- 1.2.11
- workaround glibc misconfiguration that make users listed twice
  (#34279)

* Fri Jan 18 2008 Pixel <pixel@mandriva.com> 1.2.10-1mdv2008.1
+ Revision: 154681
- 1.2.10: modify before_leaving() to be compatible with perl 5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 11 2007 Thierry Vignaud <tv@mandriva.org> 1.2.9-1mdv2008.0
+ Revision: 84348
- fix including the doc of sub-modules

* Tue Sep 04 2007 Thierry Vignaud <tv@mandriva.org> 1.2.8-1mdv2008.0
+ Revision: 79343
- make formatError() work with any modules (fixing installer bug #33131)

* Thu Aug 09 2007 Thierry Vignaud <tv@mandriva.org> 1.2.7-1mdv2008.0
+ Revision: 60753
- fix installer breakage

* Mon Aug 06 2007 Thierry Vignaud <tv@mandriva.org> 1.2.6-1mdv2008.0
+ Revision: 59370
- make find_index() pinpoint the actual bug (ie the caller)
- make formatError() safer (managing exceptions containing " at ")

* Wed May 30 2007 Pixel <pixel@mandriva.com> 1.2.5-1mdv2008.0
+ Revision: 32767
- new release, 1.2.5
- enhance fuzzy_pidofs() to handle kernel processes


* Mon Sep 04 2006 Pixel <pixel@mandriva.com> 1.2.3-1mdv2007.0
- setVarsInSh: fix writing "|" in sh config files

* Tue Jan 03 2006 Pixel <pixel@mandriva.com> 1.2.2-1mdk
- better fix for syscall.ph used somewhere else

* Thu Dec 22 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.2.1-1mdk
- fix syscall()

* Fri Nov 25 2005 Pixel <pixel@mandriva.com> 1.2-1mdk
- MDK::Common::Globals removed
- simplified version number
- perl-MDK-Common-devel replaced by package perl_checker,
  => perl-MDK-Common is a simple perl package, no more requiring ocaml
  => noarch

* Mon May 30 2005 Pixel <pixel@mandriva.com> 1.1.24-1mdk
- fix openFileMaybeCompressed() catMaybeCompressed() when file names contain spaces (bugzilla #16172)

* Thu May 19 2005 Pixel <pixel@mandriva.com> 1.1.23-1mdk
- use "our" instead of "use vars"
- add addVarsInSh() and addVarsInShMode()

* Wed Feb 16 2005 Pixel <pixel@mandrakesoft.com> 1.1.22-2mdk
- no need to call "make test", "make" is doing all what's needed
  (and otherwise MDK/Common.pm is not generated when needed due to missing dependencies)

* Tue Feb 15 2005 Pixel <pixel@mandrakesoft.com> 1.1.22-1mdk
- fix building doc without buildrequiring perl-MDK-Common (thanks to Gary L. Greene)

* Thu Dec 23 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.21-1mdk
- MDK::Common::File: add secured_output() (secured version of output())
- MDK::System: make setVarsInShMode be paranoid for all files in /home
  (anthill #1226)

* Fri Nov 26 2004 Pixel <pixel@mandrakesoft.com> 1.1.20-2mdk
- new checks in perl_checker

* Tue Nov 16 2004 Pixel <pixel@mandrakesoft.com> 1.1.20-1mdk
- MDK::Common::File : add all_files_rec()

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.1.19-2mdk
- rebuild for new perl

* Wed Nov 10 2004 Pixel <pixel@mandrakesoft.com> 1.1.19-1mdk
- MDK::System: fix cp_with_option() which called cp_af() recursively, loosing the specific options
- MDK::System: add distrib() to get company, system (e.g. Mandrakelinux) and product (e.g. 10.1)
- various perl_checker enhancements/fixes

* Mon Sep 06 2004 Pixel <pixel@mandrakesoft.com> 1.1.18-1mdk
- more flexible typeFromMagic

* Wed Aug 18 2004 Pixel <pixel@mandrakesoft.com> 1.1.17-3mdk
- use DESTDIR
- add perl_checker-vim
- add Ctrl-return in perl and cperl emacs mode
- fake Getopt::Long

* Wed Aug 11 2004 Pixel <pixel@mandrakesoft.com> 1.1.17-2mdk
- various perl_checker enhancements/fixes

* Wed Aug 04 2004 Pixel <pixel@mandrakesoft.com> 1.1.17-1mdk
- setVarsInSh() now tries to use quoting only when really needed,
  otherwise it breaks program parsing the generated file (eg: /usr/sbin/autologin)

* Mon Aug 02 2004 Pixel <pixel@mandrakesoft.com> 1.1.16-1mdk
- MDK::Common::System: whereis_binary() can now handle prefix

* Fri Jul 23 2004 Pixel <pixel@mandrakesoft.com> 1.1.15-2mdk
- workaround bug in ocaml on ultrasparc 
  (can't catch exception "Fatal error: out-of-bound access in array or string" in native code)

* Thu Jul 22 2004 Pixel <pixel@mandrakesoft.com> 1.1.15-1mdk
- add begins_with in MDK::Common::String

* Mon Jul 05 2004 Pixel <pixel@mandrakesoft.com> 1.1.14-1mdk
- more perlish behaviour for to_int() and to_float()
  (skipping leading spaces)

* Mon Jun 28 2004 Pixel <pixel@mandrakesoft.com> 1.1.13-1mdk
- fix single/quote handling in getVarsFromSh()
- setVarsInSh() now handles characters $, ', \" and spaces in the value
- fix cp_af() for symlinks to directories

* Mon May 10 2004 Pixel <pixel@mandrakesoft.com> 1.1.12-1mdk
- many perl_checker enhancements and cleanup

* Wed Apr 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.11-4mdk
- pixel:
  o add perl_checker.html
  o add testsuite
  o cp_af() now handles devices (block and character)
  o fix detecting of boolean context vs scalar context
  o fix some warning
  o in "$a ? $a : xxx", "xxx" can need short circuit
  o recognize "-c" function
  o turn some errors to warnings
- perl_checker's faked packages:
  o sync with glib/gtk+ 2.4.0
  o support Gnome2 and Gnome2::Vte too

* Thu Mar 11 2004 Pixel <pixel@mandrakesoft.com> 1.1.11-3mdk
- cp_af() now handles devices (mknod)

* Fri Feb 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.10-2mdk
- update gtk2-perl binding fake package

* Tue Jan 13 2004 Pixel <pixel@mandrakesoft.com> 1.1.11-1mdk
- sync perl_checker_fake_packages/{Glib,Gtk2}.pm
- perl_checker: fix build time overflow in cache

* Fri Jan 09 2004 Pixel <pixel@mandrakesoft.com> 1.1.10-2mdk
- perl_checker: entries in generated pot file are sorted by files

* Wed Jan 07 2004 Pixel <pixel@mandrakesoft.com> 1.1.10-1mdk
- add whereis_binary()

* Mon Jan 05 2004 Pixel <pixel@mandrakesoft.com> 1.1.9-1mdk
- many perl_checker enhancements

* Tue Dec 16 2003 Pixel <pixel@mandrakesoft.com> 1.1.8-4mdk
- MDK::Common::File::cp_f() added

* Tue Nov 18 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.8-3mdk
- perl_checker --generate-pot: unescape "$" & "@" caracters
- substInFile: if file is a symlink, make sure it stays a symlink

* Mon Nov 10 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.8-2mdk
- fix path in po generated from sources

* Wed Oct 15 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.8-1mdk
- add uniq_ (uniq but according to some code results on each value)

* Fri Sep 19 2003 Pixel <pixel@mandrakesoft.com> 1.1.7-1mdk
- read_gnomekderc() & update_gnomekderc() will now handle key=value where key
can contain spaces
- export cat_or_die()

