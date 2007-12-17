%define	Summary	This is the port of Descent 2 Version 1.2, the famous 3D game for PC

Summary:	%{Summary}
Name:		d2x-xl
Version:	1.9.9
Release:	%mkrel 3
Source0:	http://www.descent2.de/resources/%{name}-%{version}.tar.bz2
Patch2:		d2x-xl-ogl.patch
URL:		http://www.descent2.de/
Group:		Games/Arcade
License:	GPL
BuildRequires:	automake SDL-devel dos2unix desktop-file-utils ImageMagick
BuildRequires:	SDL_mixer-devel	mesagl-devel mesaglu-devel
Requires:	TiMidity++

%description
This is the port of Descent 2 Version 1.2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need the datafiles from the Retail version
of Descent 2 Version 1.2 installed in %{_gamesdatadir}/%{name}

%prep 
%setup -q
%patch2 -p0 -b .ogl
dos2unix -b `find -type f`

%build
aclocal
autoheader
autoconf
automake --add-missing
chmod +x configure
chmod +x config.sub
chmod +x missing
%configure --bindir=%{_gamesbindir} --enable-release --with-opengl
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

install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -resize 16x16 d2x-xl-ico-32x32.gif %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 d2x-xl-ico-32x32.gif %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 d2x-xl-ico-64x64.gif %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


