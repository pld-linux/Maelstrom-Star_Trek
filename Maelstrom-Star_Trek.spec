Summary:	Rockin' asteroids game - Star Trek theme
Summary(pl.UTF-8):   Gra, w której strzelasz do asteroidów - motyw Star Trek
Name:		Maelstrom-Star_Trek
Version:	1
Release:	3
License:	unknown
Group:		X11/Applications/Games
# Source0-md5:	ea23f9eaa96a27c14affe3196611c918
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/add-ons/Star_Trek.zip
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/add-ons.html
Requires:	Maelstrom
Obsoletes:	Maelstrom-1980
Obsoletes:	Maelstrom-Star_Wars
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom
%description
Star Trek theme for Maelstrom.

%description -l pl.UTF-8
Motyw Star Trek dla Maelstroma.

%prep
%setup -q -n Star_Trek

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install "%Maelstrom Sounds" $RPM_BUILD_ROOT%{_gamedir}/Maelstrom_Sounds.bin
install "%Maelstrom Sprites" $RPM_BUILD_ROOT%{_gamedir}/Maelstrom_Sprites.bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_gamedir}/*
