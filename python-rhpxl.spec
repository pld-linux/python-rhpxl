Summary:	Library of Python code for configuring and running X
Summary(pl):	Biblioteka kodu Pythona u¿ywana do konfiguracji i uruchamiania X
Name:		python-rhpxl
Version:	0.18
Release:	0.9
License:	GPL
Group:		Libraries
Source0:	rhpxl-%{version}.tar.gz
# Source0-md5:	60088c7d19309600375f16ef1dbdb952
Source1:	vesamodes
Source2:	extramodes
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-xorg.patch
BuildRequires:	gettext-devel
BuildRequires:	python-devel
%pyrequires_eq	python-libs
Requires:	hwdata >= 0.169
Requires:	kudzu >= 1.2.34.3
Requires:	newt
Requires:	python-rhpl
%ifnarch s390 s390x
Requires:	python-xf86config >= 0.3.24
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhxpl package contains Python code for configuring and running X.

%description -l pl
Pakiet rhpxl zawiera kod Pythona u¿ywany do konfiguracji i
uruchamiania X.

%prep
%setup -q -n rhpxl-%{version}
%patch0 -p1
%patch1 -p1

rm -f po/no.po

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/rhpxl
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/rhpxl
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/rhpxl

%find_lang rhpxl
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpxl.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_sbindir}/ddcprobe
%dir %{py_sitescriptdir}/rhpxl
%{py_sitescriptdir}/rhpxl/*.py[co]
%{_datadir}/rhpxl
