Summary:	Pack of themes for IceWM
Summary(pl):	Zestaw motywów dla IceWM-a
Name:		icewm-themes1
Version:	1.0
Release:	2
License:	GPL (?)
Group:		Themes
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	7c3c248b817b89f59fc584407c3cc5d6
Requires:	icewm
Obsoletes:	icewm-themes-pack1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/share/icewm/themes

%description
This is a set of 25 themes for IceWM. Themes authors:
- 4Dwm Theme v.2 - Jeremiah Cornelius <jcorneli@rocketmail.com>
- Absolute_I - Taner Tas <terranigma@pmail.net>
- The Alien race - Mike Wynn <Mike.Wynn@alien-race.freeserve.co.uk>
- AltOS - MarkJ <h089@mth.uea.ac.uk>
- Amiga Theme - Bhaak <bhaak@gmx.net>
- Area51 (MJ-7) - RudeSka
- ASUKA - Josef 'Jupp' Schugt <jupp@gmx.de>
- Athens Theme - Oleastre <osamyn@ulb.ac.be>
- Batman - RudeSka
- BB.T.O - Pal Palocz <palocz.pal@mail.deltav.hu>
- Beamer - The BMW Theme - Chris Phelps <chicane@reninet.com>
- CoolTech - William Wieboldt <waw@gopenguin.com>
- MicroGUI-2 - Tal Danzig <tdanzig@home.com>
- DarkBlue - Fl0
- Deathray - Daniel W. Lemon <dwl@wolsi.com>
- Dogmatic - Xerithane <xerithane@nerdfarm.org>
- Dominanz Haus - <Mathias.Hasselmann@gmx.de>
- Dot - Roland Buehlmann <roli.buehlmann@trash.net>
- E15 - ?
- Easy - Daniel W. Lemon <dwl@wolsi.com>
- Eazel - Arlo Rose, adapted to IceWM by Oleastre
- fake95 - Josef 'Jupp' Schugt <jupp@gmx.de>
- FrostyAgain - <mathias.hasselmann@gmx.de>
- Helix - RudeSka
- REI - Josef 'Jupp' Schugt <jupp@gmx.de>

%description -l pl
Jest to zestaw 25 motywów do uprzyjemnienia wygl±du twojego IceWM-a.
Autorzy poszczególnych motywów:
- 4Dwm Theme v.2 - Jeremiah Cornelius <jcorneli@rocketmail.com>
- Absolute_I - Taner Tas <terranigma@pmail.net>
- The Alien race - Mike Wynn <Mike.Wynn@alien-race.freeserve.co.uk>
- AltOS - MarkJ <h089@mth.uea.ac.uk>
- Amiga Theme - Bhaak <bhaak@gmx.net>
- Area51 (MJ-7) - RudeSka
- ASUKA - Josef 'Jupp' Schugt <jupp@gmx.de>
- Athens Theme - Oleastre <osamyn@ulb.ac.be>
- Batman - RudeSka
- BB.T.O - Pal Palocz <palocz.pal@mail.deltav.hu>
- Beamer - The BMW Theme - Chris Phelps <chicane@reninet.com>
- CoolTech - William Wieboldt <waw@gopenguin.com>
- MicroGUI-2 - Tal Danzig <tdanzig@home.com>
- DarkBlue - Fl0
- Deathray - Daniel W. Lemon <dwl@wolsi.com>
- Dogmatic - Xerithane <xerithane@nerdfarm.org>
- Dominanz Haus - <Mathias.Hasselmann@gmx.de>
- Dot - Roland Buehlmann <roli.buehlmann@trash.net>
- E15 - ?
- Easy - Daniel W. Lemon <dwl@wolsi.com>
- Eazel - Arlo Rose, adapted to IceWM by Oleastre
- fake95 - Josef 'Jupp' Schugt <jupp@gmx.de>
- FrostyAgain - <mathias.hasselmann@gmx.de>
- Helix - RudeSka
- REI - Josef 'Jupp' Schugt <jupp@gmx.de>

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
