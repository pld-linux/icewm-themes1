Summary:        Pack of themes for icewm
Summary(pl):	Zestaw tematów dla icewm
Name:		icewm-themes-pack1
Version:	1.0
Release:	1
License:	GPL (?)
Group:		Themes
Group(pl):	Tematy
Source0:	%{name}.tar.gz

Requires:	icewm
Buildroot:      %{tmpdir}/%{name}-root-%(id -u -n)

%define		_themesdir	/usr/X11R6/lib/X11/icewm/themes

%description 
This is a set of 25 themes for icewm.

%description -l pl
Jest to zestaw 25 tematów do uprzyjemnienia wygl±du twojego icewm'a.

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
