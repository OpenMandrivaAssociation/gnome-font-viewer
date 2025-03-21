%define url_ver	%(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Summary:	GNOME Font viewer
Name:		gnome-font-viewer
Version:	48.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-4)
BuildRequires:	pkgconfig(gio-2.0) 
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  cmake
BuildRequires:	meson
Conflicts:	gnome-utils < 1:3.3.1

%description
Font viewer for Gnome desktop.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

#fix .desktop file
desktop-file-edit %{buildroot}%{_datadir}/applications/org.gnome.font-viewer.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
%{_datadir}/metainfo/org.gnome.font-viewer.appdata.xml
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%{_iconsdir}/hicolor/scalable/apps/org.gnome.font-viewer.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.font-viewer-symbolic.svg
