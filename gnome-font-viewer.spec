%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME Font viewer
Name:		gnome-font-viewer
Version:	3.6.2
Release:	4
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
%configure2_5x \
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
%{_datadir}/applications/%{name}.desktop

