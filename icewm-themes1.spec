Summary:	Pack of themes for icewm
Summary(pl):	Zestaw tematów dla icewm
Name:		icewm-themes-pack1
Version:	1.0
Release:	2
License:	GPL (?)
Group:		Themes
Group(de):	Themen
Group(pl):	Motywy
Source0:	%{name}.tar.gz

Requires:	icewm
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/X11R6/lib/X11/icewm/themes

%description 
This is a set of 25 themes for icewm.
4Dwm Theme v.2		Jeremiah Cornelius <jcorneli@rocketmail.com>
Absolute_I		Taner Tas <terranigma@pmail.net>
The Alien race		Mike Wynn <Mike.Wynn@alien-race.freeserve.co.uk>
AltOS			MarkJ <h089@mth.uea.ac.uk>
Amiga Theme		Bhaak <bhaak@gmx.net>
Area51 (MJ-7)		RudeSka
ASUKA			Josef 'Jupp' Schugt <jupp@gmx.de>
Athens Theme		Oleastre <osamyn@ulb.ac.be>
Batman			RudeSka
BB.T.O			Pal Palocz <palocz.pal@mail.deltav.hu>
Beamer - The BMW Theme	Chris Phelps <chicane@reninet.com>
CoolTech		William Wieboldt <waw@gopenguin.com>
MicroGUI-2		Tal Danzig <tdanzig@home.com>
DarkBlue		Fl0
Deathray		Daniel W. Lemon  <dwl@wolsi.com>
Dogmatic		Xerithane <xerithane@nerdfarm.org>
Dominanz Haus		<Mathias.Hasselmann@gmx.de>
Dot			Roland Buehlmann <roli.buehlmann@trash.net>
E15			?
Easy			Daniel W. Lemon  <dwl@wolsi.com>
Eazel			Arlo Rose, adapted to IceWM by Oleastre
fake95			Josef 'Jupp' Schugt <jupp@gmx.de>
FrostyAgain		<mathias.hasselmann@gmx.de>
Helix			RudeSka
REI			Josef 'Jupp' Schugt <jupp@gmx.de>

%description -l pl
Jest to zestaw 25 tematów do uprzyjemnienia wygl±du twojego icewm'a.
4Dwm Theme v.2          Jeremiah Cornelius <jcorneli@rocketmail.com>
Absolute_I              Taner Tas <terranigma@pmail.net>
The Alien race          Mike Wynn <Mike.Wynn@alien-race.freeserve.co.uk>
AltOS                   MarkJ <h089@mth.uea.ac.uk>
Amiga Theme             Bhaak <bhaak@gmx.net>
Area51 (MJ-7)           RudeSka
ASUKA                   Josef 'Jupp' Schugt <jupp@gmx.de>
Athens Theme            Oleastre <osamyn@ulb.ac.be>
Batman                  RudeSka
BB.T.O                  Pal Palocz <palocz.pal@mail.deltav.hu>
Beamer - The BMW Theme  Chris Phelps <chicane@reninet.com>
CoolTech                William Wieboldt <waw@gopenguin.com>
MicroGUI-2              Tal Danzig <tdanzig@home.com>
DarkBlue                Fl0
Deathray                Daniel W. Lemon  <dwl@wolsi.com>
Dogmatic                Xerithane <xerithane@nerdfarm.org>
Dominanz Haus           <Mathias.Hasselmann@gmx.de>
Dot                     Roland Buehlmann <roli.buehlmann@trash.net>
E15                     ?
Easy                    Daniel W. Lemon  <dwl@wolsi.com>
Eazel                   Arlo Rose, adapted to IceWM by Oleastre
fake95                  Josef 'Jupp' Schugt <jupp@gmx.de>
FrostyAgain             <mathias.hasselmann@gmx.de>
Helix                   RudeSka
REI                     Josef 'Jupp' Schugt <jupp@gmx.de>

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
%dir %{_themesdir}
%{_themesdir}/*
