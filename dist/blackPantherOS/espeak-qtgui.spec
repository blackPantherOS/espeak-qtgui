%define debug_package  %nil
%define name 		espeak-qtgui
%define pypi_name 	espeak_qtgui
%define Summary		Qt5 Gui for Espeak
%define Summary_hu	Qt5 kezelőfelület az Espeak-hez
%define sourcetype      tar.xz
%define version         1.0

Name:         %name
Summary:       %Summary
Summary(hu):   %Summary_hu
Version:       %version
Release:       %mkrel 4
License:       GPL3
Distribution: blackPanther OS
Vendor:       blackPanther Europe
Group:        Sound/Utilities
URL:	      https://github.com/blackPantherOS/espeak-qtgui
Source0:      %name-%version.%sourcetype
Buildroot:    %_tmppath/%name-%version-%release-root
BuildArch:	noarch
Requires:     python3 >= 3.5.1
Requires:     python3-qt5 >= 5.6
Requires:     espeak-ng >= 1.50
Requires:     pydialog >= 0.6


%description
A simple Qt5 Gui for the Espeak.
Core developer is Miklos Horvath 

%files
%defattr(-,root,root)
%_bindir/%name
%python3_sitelib/%pypi_name/*
%python3_sitelib/%{pypi_name}*egg-info
%{_datadir}/applications/*.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%prep
%setup -q -n %{name}

%build
%py3_build

%install
%py3_install

%define  nameicon %name.png
mkdir -p -m755 %{buildroot}{%_liconsdir,%_iconsdir,%_miconsdir}
convert -scale 48x48 %{nameicon} %{buildroot}/%{_liconsdir}/%{name}.png
convert -scale 32x32 %{nameicon} %{buildroot}/%{_iconsdir}/%{name}.png
convert -scale 16x16 %{nameicon} %{buildroot}/%{_miconsdir}/%{name}.png

%clean
rm -rf %buildroot


%changelog
* Sat Jan 18 2020 Charles K. Barcza <info@blackpanther.hu> 1.0-4bP
- build package for blackPanther OS v17-19.x 32/64 bit or ARM
-------------------------------------------------------------------------

* Sat Jan 18 2020 Charles K. Barcza <info@blackpanther.hu> 1.0-3bP
- build package for blackPanther OS v17-19.x 32/64 bit or ARM
-------------------------------------------------------------------------

* Sat May 06 2017 Charles Barcza <info@blackpanther.hu> 1.0-2bP
- build for blackPanther OS v16.x
------------------------------------------------------------------
* Sat May 06 2017 Miklos Horvath <hmiki@blackpantheros.eu> 
- Initial version
