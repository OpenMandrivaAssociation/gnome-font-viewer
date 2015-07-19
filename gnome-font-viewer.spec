%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME Font viewer
Name:		gnome-font-viewer
Version:	 3.16.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(freetype2)
Conflicts:	gnome-utils < 1:3.3.1

%description
Font viewer for Gnome desktop.

%prep
%setup -q

%build
%configure \
	--disable-schemas-compile
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
%{_datadir}/appdata/org.gnome.font-viewer.appdata.xml
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service


