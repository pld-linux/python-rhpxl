Summary:	Library of Python code for configuring and running X
Summary(pl):	Biblioteka kodu Pythona u¿ywana do konfiguracji i uruchamiania X
Name:		python-rhpxl
Version:	0.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	rhpxl-%{version}.tar.gz
# Source0-md5:	c6dc279b3f77b68951af5c0a4a7124da
BuildRequires:	gettext-devel
BuildRequires:	python-devel
%pyrequires_eq	python-libs
%ifnarch s390 s390x
Requires:	python-xf86config >= 0.3.2
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhxpl package contains Python code for configuring and running X.

%description -l pl
Pakiet rhpxl zawiera kod Pythona u¿ywany do konfiguracji i
uruchamiania X.

%prep
%setup -q -n rhpxl-%{version}

rm -f po/no.po

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang rhpxl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpxl.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(750,root,root) %{_sbindir}/ddcprobe
%dir %{py_sitescriptdir}/rhpxl
%{py_sitescriptdir}/rhpxl/*.py*
%{_datadir}/rhpxl
