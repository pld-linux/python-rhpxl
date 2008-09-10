Summary:	Library of Python code for configuring and running X
Summary(pl.UTF-8):	Biblioteka kodu Pythona używana do konfiguracji i uruchamiania X
Name:		python-rhpxl
Version:	0.49
Release:	1
License:	GPL
Group:		Libraries
Source0:	https://fedorahosted.org/releases/r/h/rhpxl/rhpxl-%{version}.tar.gz
# Source0-md5:	ad8a3151b455d435c4928611f421fc0a
URL:		https://fedoraproject.org/wiki/Rhpxl
BuildRequires:	gettext-devel
BuildRequires:	python-devel
%pyrequires_eq	python-libs
Requires:	hwdata >= 0.169
Requires:	kudzu >= 1.2.34.3
Requires:	newt
Requires:	python-rhpl
%ifnarch s390 s390x
Requires:	python-xf86config >= 0.3.34
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rhxpl package contains Python code for configuring and running X.

%description -l pl.UTF-8
Pakiet rhpxl zawiera kod Pythona używany do konfiguracji i
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
install -d $RPM_BUILD_ROOT%{_datadir}/rhpxl

%find_lang rhpxl
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpxl.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/ddcprobe
%dir %{py_sitedir}/rhpxl
%{py_sitedir}/rhpxl/*.py[co]
%attr(755,root,root) %{py_sitedir}/rhpxl/*.so
%{_datadir}/rhpxl
