%define Werror_cflags %nil
%define	Summary	This is the port of Descent 2 Version 1.2, the famous 3D game for PC

Summary:	%{Summary}
Name:		d2x-xl
Version:	1.15.341
Release:	3
Source0:	http://www.descent2.de/resources/%{name}-%{version}.tar.xz
Patch0:		d2x-xl-1.15.130-link.patch
# Patch2:		d2x-xl-ogl.patch
URL:		http://www.descent2.de/
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake SDL-devel dos2unix desktop-file-utils imagemagick
BuildRequires:	SDL_mixer-devel	GL-devel glew-devel lesstif-devel SDL_net-devel
BuildRequires:  mesaglu-devel
BuildRequires:	libgomp-devel SDL_image-devel curl-devel glibc-devel
Requires:	TiMidity++

%description
This is the port of Descent 2 Version 1.2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need the datafiles from the Retail version
of Descent 2 Version 1.2 installed in %{_gamesdatadir}/%{name}

%prep 
%setup -q
%patch0 -p0

%build
autoreconf
chmod +x configure
%configure2_5x --bindir=%{_gamesbindir} --enable-release --with-opengl
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_gamesdatadir}/%{name}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=D2X-XL
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

# install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
# convert -resize 16x16 d2x-xl-ico-32x32.gif %{buildroot}%{_miconsdir}/%{name}.png
# convert -resize 32x32 d2x-xl-ico-32x32.gif %{buildroot}%{_iconsdir}/%{name}.png
# convert -resize 48x48 d2x-xl-ico-64x64.gif %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
# %{_miconsdir}/%{name}.png
# %{_iconsdir}/%{name}.png
# %{_liconsdir}/%{name}.png






%changelog
* Wed Apr 04 2012 Zombie Ryushu <ryushu@mandriva.org> 1.15.341-1mdv2011.0
+ Revision: 789179
- Update to 1.15.341

* Tue Feb 28 2012 Zombie Ryushu <ryushu@mandriva.org> 1.15.303-1
+ Revision: 781344
- Upgrade to 303

* Sat Feb 18 2012 Zombie Ryushu <ryushu@mandriva.org> 1.15.293-1
+ Revision: 776857
- Upgrade to 1.15.293

* Fri Nov 04 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.270-1
+ Revision: 716928
- Upgrade to 1.15.270
- Upgrade to 1.15.270

* Wed Oct 26 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.269-1
+ Revision: 707382
- Upgrade to 1.15.269

* Thu Oct 13 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.268-1
+ Revision: 704552
- Upgrade to 1.15.268

* Sat Sep 10 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.261-1
+ Revision: 699271
- Upgrade to 1.15.261
- fix build requires
- Upgrade to 1.15.253
- Upgrade to 1.15.252

* Tue Jun 21 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.233-1
+ Revision: 686420
- Upgrade to 1.15.233

* Wed Jun 08 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.230-1
+ Revision: 683229
- Update to 230

* Wed Jun 08 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.229-1
+ Revision: 683162
- Update to 229

* Tue Jun 07 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.228-1
+ Revision: 683020
- Upgrade to 1.15.228

* Mon Jun 06 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.227-1
+ Revision: 682922
- Upgrade to 1.15.227

* Sat May 14 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.210-1
+ Revision: 674574
- Upgrade to 1.15.210
- Upgrade to 1.15.209

* Sat Apr 23 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.184-1
+ Revision: 657757
- Upgrade to 1.15.184

* Fri Apr 22 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.183-1
+ Revision: 656646
- Upgrade to 1.15.183
- Re-get SVN
- Upgrade to 1.15.179
- Upgrade to 1.15.178

* Sat Apr 09 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.177-1
+ Revision: 652134
- Upgrade to 1.15.177
- Update to 1.15.174

* Thu Apr 07 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.173-1
+ Revision: 651823
- Update to 1.15.173 svn
- Update to 1.15.173 svn
- Upgrade to 1.15.172
- Upgrade to 1.15.171
- Upgrade to 1.15.170
- Upgrade to 1.15.169
- Upgrade to 1.15.168
- Upgrade to 1.15.167
- Upgrade to 1.15.166
- Upgrade to 1.15.164

* Sat Mar 26 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.160-1
+ Revision: 648562
- Upgrade to 1.15.160

* Mon Mar 21 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.155-1
+ Revision: 647230
- Upgrade to version 1.15.155
- Upgrade to 1.15.141

* Tue Mar 01 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.139-1
+ Revision: 641102
- Update to 1.15.139

* Mon Feb 28 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.137-1
+ Revision: 640913
- Update to 1.15.137 and use xz now
- Fix SDL_net dependency
- Upgrade to 1.15.136

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.15.130-2
+ Revision: 640541
- fix linkage
- rebuild to obsolete old packages

* Wed Feb 23 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.130-1
+ Revision: 639451
+ rebuild (emptylog)

* Tue Feb 22 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.128-1
+ Revision: 639270
- Update to 1.15.128

* Mon Feb 21 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.127-1
+ Revision: 639131
- Version 1.15.127

* Wed Feb 16 2011 Zombie Ryushu <ryushu@mandriva.org> 1.15.125-1
+ Revision: 638000
- Upgrade to 1.15.125

* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 1.15.103-1mdv2011.0
+ Revision: 599362
- add more BRs
- add more BRs

  + Zombie Ryushu <ryushu@mandriva.org>
    - Upgrade to 1.15.103
    - Upgrade to 1.15.103
    - Upgrade to 1.15.103
    - Upgrade to 1.15.87
    - Upgrade to 1.15.87
    - Upgrade to 1.15.79
    - Upgrade to 1.15.79
    - Upgrade to 1.15.63
    - Upgrade to 1.15.63
    - Upgrade to 1.15.63

* Sun Mar 21 2010 Zombie Ryushu <ryushu@mandriva.org> 1.14.202-1mdv2010.1
+ Revision: 526271
- Fix lesstif dependency
- Add openmotif dependency
- Add curl dependency
- Add SDL_image dependency
- Add libgomp dependency
- Upgrade to 1.14.202
- Upgrade to 1.14.202
- Upgrade to 1.14.202
- Much needed version bump to 1.13.53
- Much needed version bump to 1.13.53

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Funda Wang <fwang@mandriva.org>
    - New version 1.13.53
    - integrate Zombie Ryushu's work

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.9.9-5mdv2009.0
+ Revision: 243885
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.9.9-3mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sun May 27 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 1.9.9-3mdv2008.0
+ Revision: 31718
- fixed TiMidity++ dep name


* Sun Mar 04 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.9.9-2mdv2007.0
+ Revision: 132329
- bump
- use dos2unix on files only
- fix buildrequires
- fix buildrequires
-new package from Zombie
- Import d2x-xl

