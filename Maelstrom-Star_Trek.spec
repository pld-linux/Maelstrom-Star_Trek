Summary:	Rockin' asteroids game - Star Trek theme
Summary(pl):	Gra, w kt�rej strzelasz do asteroid�w - motyw Star Trek
Name:		Maelstrom-Star_Trek
Version:	1
Release:	1
License:	dunno
Group:		X11/Application/Games
Source0:	http://www.devolution.com/~slouken/Maelstrom/add-ons/Star_Trek.tar.gz
URL:		http://www.devolution.com/~slouken/Maelstrom/add-ons/
Requires:	Maelstrom
Obsoletes:	Maelstrom-1980
Obsoletes:	Maelstrom-Star_Wars
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom
%description
Star Trek theme for Maelstrom.

%description -l pl
Motyw Star Trek dla Maelstroma.

%prep
%setup -q -n Star_Trek

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install %* $RPM_BUILD_ROOT%{_gamedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_gamedir}/*
