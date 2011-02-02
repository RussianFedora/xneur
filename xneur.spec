Summary:	X Neural Switcher
Name:		xneur
Version:	0.12.0
Release:	1%{?dist}

License:	GPLv2
Group:		User Interface/Desktops
URL:		http://www.xneur.ru
Source:		http://dists.xneur.ru/release-%{version}/tgz/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	pcre-devel
BuildRequires:	libX11-devel
BuildRequires:	gstreamer-devel
BuildRequires:	freealut-devel >= 1.0.1
BuildRequires:	aspell-devel
BuildRequires:	libXpm-devel
BuildRequires:	imlib2-devel
BuildRequires:	xosd-devel
BuildRequires:	gettext-devel
BuildRequires:	libnotify-devel
BuildRequires:	enchant-devel
BuildRequires:	autoconf, automake, libtool


%description
X Neural Switcher is a program for automatic (intelligent) keyboard layout
changing in the X Window System. It is mainly used to change between Russian
and English, but also supports Armenian, Belorussian, Bolgarian, Czech,
Georgian, German, Greek, Estonian, French, Kazakh, Lithuanian, Latvian, Polish,
Moldovan (Romanian), Spanish, Ukrainian and Uzbek.


%description -l ru
X Neural Switcher это программа для автоматического (интеллектуального)
переключения раскладок клавиатуры в X Window. Прежде всего он предназначен
для смены русской и английской раскладок, но также поддерживаются армянский,
белорусский, болгарский, чешский, грузинский, немецкий, греческий, эстонский,
французский, казахский, литовский, латвийский (латышский), польский, молдавский
(румынский), испанский, украинский и узбекский языки.


%package devel
Summary:	Static library and header files for the xneur
Group:		Development/Libraries
Requires:	%{name} = %{version}


%description devel
The %{name}-devel package contains API documentation for
developing %{name}.


%prep
%setup -q


%build
%configure LIBNOTIFY_CFLAGS="%( pkg-config --cflags "libnotify >= 0.4.0" gtk+-2.0 )" LIBNOTIFY_LIBS="%( pkg-config --libs "libnotify >= 0.4.0" gtk+-2.0 )"

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# remove static
rm %{buildroot}/%{_libdir}/{,%{name}}/*.{a,la}

%find_lang %{name}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/%{name}/xneurrc*
%{_bindir}/%{name}
%{_libdir}/*.so.*
%{_libdir}/%{name}/*.so.*
%{_mandir}/man?/*
%{_datadir}/%{name}/*


%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_libdir}/%{name}/*.so
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*


%changelog
* Wed Feb  2 2011 Arkady L. Shane <ashejn@yandex-team.ru> 0.12.0-1
- update to 0.12.0

* Sun Nov 28 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.11.1-1
- update to 0.11.1

* Thu Oct  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.10.0-1
- update to 0.10.0
- some merges from hubbitus spec

* Mon Aug 16 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.9-2
- rebuilt for Fedra 14

* Fri May 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.9-1
- update to 0.9.9

* Sun Mar 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.8-1
- update to 0.9.8

* Thu Oct 15 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.7-1
- update to 0.9.7

* Wed Sep 16 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.6-1
- update to 0.9.6

* Wed Aug  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.5-1
- update to 0.9.5

* Wed Apr 22 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.4-1
- 0.9.4

* Fri Apr 17 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.4-0.1.20090416svn344
- last snapshot

* Fri Jan  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.3-1
- 0.9.3

* Mon Nov  3 2008 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.2-1
- 0.9.2

* Fri Jul 25 2008 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.1-1
- 0.9.1

* Tue Jun 24 2008 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.0-1
- 0.9.0

* Fri Oct 12 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.8.0-1
- 0.8.0
- add missing BR gstreamer-devel, freealut-devel, aspell-devel

* Tue Jul 17 2007  Arkady L. Shane <ashejn@yandex-team.ru> 0.6.2-1
- 0.6.2

* Fri May 18 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.6.1-1
- 0.6.1

* Mon Apr 23 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.6-1
- 0.6

* Sat Mar 10 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.5-1
- 0.5.0
- add devel package

* Tue Jan 23 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.4-1
- rebuilt for FC6
- cleanup spec

* Wed Jan 03 2007 Nik <niktr@mail.ru>
- rebuild for FC6
- updated to svn version dated 03012007
- minor changes in spec file

* Wed Mar 02 2005 Andy Shevchenko <andriy@asplinux.ru>
- rebuild for ASPLinux
- update to 0.0.3

* Mon Feb 14 2005 myLinux, Ltd <info@mylinux.com.ua>
- build for myLinux

* Wed Jan 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt0.1
- first build for Sisyphus
