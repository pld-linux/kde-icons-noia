%define		_ver		090
%define		_name		noia

Summary:	KDE Icons Theme - Noia
Summary(pl):	Motyw ikon dla KDE - Noia
Name:		kde-icons-noia
Version:	0.90
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	%{_name}%{_ver}.tar.gz
# Source0-md5:	e86b9911335bf8f85b337c39b1598dc9
URL:		http://www.kdelook.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_icondir	/usr/share/icons

%description
KDE Icons Theme - Noia

%description -l pl
Motyw ikon dla KDE - Noia

%prep
%setup -q -n noia

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_icondir}/noia
cp -r 16x16/* $RPM_BUILD_ROOT/%{_icondir}/noia/
cp -r 22x22/* $RPM_BUILD_ROOT/%{_icondir}/noia/
cp -r 32x32/* $RPM_BUILD_ROOT/%{_icondir}/noia/
cp -r 48x48/* $RPM_BUILD_ROOT/%{_icondir}/noia/
cp -r 64x64/* $RPM_BUILD_ROOT/%{_icondir}/noia/
install index.desktop $RPM_BUILD_ROOT/%{_icondir}/noia/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog readme
%{_icondir}/noia
