%define name	d2x-xl
%define version 1.13.53
%define	Summary	An OpenGL Port of Desccent 1 and 2 Version 1.2, the famous 3D game for PC
%define release %mkrel 1
Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.descent2.de/resources/%{name}-%{version}.tar.bz2
# Source1:	http://www.descent2.de/resources/%{name}-makefiles.zip
# Patch0:		configure.patch
# Patch1:		d2x-xl-oof.patch
# Patch2:		d2x-xl-ogl.patch
# Patch3:		d2x-xl-vecmat.patch
Patch4:		d2x-xl-font-oden.patch
Patch5:		d2x-xl-alsadigi.patch
URL:		http://D2X-XL-engine.com/
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake 
Requires:	TiMidity++

%description
This is the port of Descent 2 Version 1.2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need the datafiles from the Retail version
of Descent 2 Version 1.2 installed in /usr/share/games/d2x-xl


%prep 
%setup -q %{name}-%{version}
# Remove a few files that are also contained in the second source
# archive
rm -f d2x-w32.ico d2x-xl-ico-32x32.gif d2x-xl-ico-64x64.gif d2x-xl.ico \
       d2x.w32.rc descent.ico texmerge.frag texmerge.vert
# %setup -T -D -a 1
# %patch0 -p0 -b .configure
# Strip some DOS line endings from the configure script
# %patch1 -p0 -b .oof
# %patch2 -p0 -b .ogl
# %patch3 -p0 -b .vecmat
# %patch4 -p0 -b .textdata
%patch5 -p0 -b .alsadigi
%patch4 -p0 -b .font
%build
dos2unix -U -b *
aclocal
autoheader
autoconf
automake --add-missing
chmod +x configure
chmod +x config.sub
chmod +x missing
export LDFLAGS=-L%_prefix/X11R6/%_lib
CFLAGS="-O0 -g3 -ggdb" %configure --bindir=/usr/games --enable-release=yes --disable-kalinix
make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
install -d %{buildroot}%{_menudir}
cat << EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}): needs="x11" \
		   section="More Applications/Games/Arcade/D2X-XL" \ title="D2X-XL" \
		   longtitle="%{Summary}" \
		   command="%{_gamesbindir}/%{name}"
		   icon="d2x-xl-ico-32x32.png"
		   command="%{_gamesbindir}/d2x-xl
EOF


%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
# no %doc ?
%defattr (-,root,root)
# better use macro, in case something change
%{_menudir}/%{name}
%{_gamesbindir}/d2x-xl

%changelog
# missing changelog here, rpmlint warn against this

* Fri May 19 2006 Lenny Cartier <lenny@mandrakesoft.com> 1.6.54
- 1.6.54
