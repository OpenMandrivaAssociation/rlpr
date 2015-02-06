Summary:	Remote printing utilities
Name:		rlpr
Version:	2.06
Release:	6
License:	GPL
Group:		Networking/Remote access
# Site of original author is dead, and project, too. As several other
# orphaned printing packages this is re-hosted on linuxprinting.org
Source0:	http://www.linuxprinting.org/download/printing/%{name}-%{version}.tar.bz2
URL:		http://www.linuxprinting.org/download/printing/README.txt
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
Rlpr is a package that makes it possible (or at the very least,
easier), to print files on remote sites to your local printer. The
rlpr package includes BSD-compatible replacements for `lpr', `lpq',
and `lprm', whose functionality is a superset of their BSD
counterparts. In other words, with the rlpr package, you can do
everything you can do with the BSD printing commands, and more. The
programs contained within the rlpr package are all GPL'd, and are more
lightweight, cleaner and more secure than their BSD counterparts.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -fr %buildroot


%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(4755,root,root) %{_bindir}/*
%{_mandir}/man*/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.06-5mdv2010.0
+ Revision: 433350
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.06-4mdv2009.0
+ Revision: 260242
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.06-3mdv2009.0
+ Revision: 251323
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 27 2007 Jérôme Soyer <saispo@mandriva.org> 2.06-1mdv2008.1
+ Revision: 138402
- New release

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.04-4mdv2008.0
+ Revision: 70370
- use %%mkrel

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Import rlpr




* Fri Sep  2 2005 Till Kamppeter <till@mandriva.com> 2.04-3mdk
- Removed the dust of 1 year not rebuilding.

* Fri Aug 13 2004 Till Kamppeter <till@mandrakesoft.com> 2.04-2mdk
- Rebuilt.
- Some clean-up in the spec file.

* Sun Jul 27 2003 Till Kamppeter <till@mandrakesoft.com> 2.04-1mdk
- Finally updated to version 2.04.
- Removed the patch, it was already applied upstream.

* Fri Mar 22 2002 David BAUDENS <baudens@mandrakesoft.com> 2.02-3mdk
- Clean after build
- Remove pl description and summary

* Tue Aug  7 2001 Till Kamppeter <till@mandrakesoft.com> 2.02-2mdk
- Executables must be SUID root to work

* Tue Aug  7 2001 Till Kamppeter <till@mandrakesoft.com> 2.02-1mdk
- Initial release
