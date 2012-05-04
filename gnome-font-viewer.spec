%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-font-viewer
Version:	3.4.0
Release:	%mkrel 2
Summary:	GNOME Font viewer
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(freetype2)
Conflicts:	gnome-utils < 1:3.3.1
Conflicts:	gnome-control-center < 3.0.2

%description
Font viewer for Gnome desktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath \
	--disable-schemas-compile
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
%{_datadir}/applications/%{name}.desktop


