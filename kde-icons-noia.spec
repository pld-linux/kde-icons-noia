%define		_name		Noia_KDE

Summary:	KDE Icons Theme - Noia
Summary(pl):	Motyw ikon dla KDE - Noia
Name:		kde-icons-noia
Version:	0.95
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	ftp://distfiles.pld-linux.org/src/%{_name}_%{version}.tar.gz
# Source0-md5:	e86b9911335bf8f85b337c39b1598dc9
URL:		http://www.kdelook.org/
BuildRequires:	rpmbuild(macros) >= 1.123
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Icons Theme - Noia

%description -l pl
Motyw ikon dla KDE - Noia

%prep
%setup -q -n 'Noia\ KDE\ 0.95'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/noia

cp -r 16x16 $RPM_BUILD_ROOT%{_iconsdir}/noia
cp -r 22x22 $RPM_BUILD_ROOT%{_iconsdir}/noia
cp -r 32x32 $RPM_BUILD_ROOT%{_iconsdir}/noia
cp -r 48x48 $RPM_BUILD_ROOT%{_iconsdir}/noia
cp -r 64x64 $RPM_BUILD_ROOT%{_iconsdir}/noia
cp -r 128x128 $RPM_BUILD_ROOT%{_iconsdir}/noia
install index.desktop $RPM_BUILD_ROOT%{_iconsdir}/noia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog readme
%{_iconsdir}/noia
