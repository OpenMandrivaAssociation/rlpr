Summary:	Remote printing utilities
Name:		rlpr
Version:	2.06
Release:	%mkrel 5
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
