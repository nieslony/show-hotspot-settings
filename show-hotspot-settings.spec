%global pypi_name showhotspotsettings

Name:           show-hotspot-settings
Version:        0.3
Release:        1%{?dist}
Summary:        Show current hotspot settings in web page

License:        GPL-3.0
URL:            http://www.nieslony.site/OpenVPN_Admin
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{pypi_name} = %{version}
Requires:       httpd mod_wsgi

%description
Show current hotspot settings in web page from NetworkManager ot hostapd

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
python package

%prep
echo %{name}-%{pypi_version}
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install
mkdir -pv $RPM_BUILD_ROOT/var/www/%{name}
install show-hotspot-settings.wsgi $RPM_BUILD_ROOT/var/www/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
install apache-config/show-hotspot-settings.conf $RPM_BUILD_ROOT/%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
/var/www/%{name}
%{_datadir}/%{name}

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Feb 26 2025 Claas Nieslony <claas@nieslony.at> 0.3-1
- Make spec work again (claas@nieslony.at)
- Make stand alone sercer work again (claas@nieslony.at)
- Rename app.py (claas@nieslony.at)
- Create python module (claas@nieslony.at)

* Fri Mar 15 2024 Claas Nieslony <github@nieslony.at>
- Fix: directory name (github@nieslony.at)

* Mon Mar 11 2024 Claas Nieslony <github@nieslony.at>
- Install apache config to /usr/share/... (github@nieslony.at)

* Mon Mar 11 2024 Claas Nieslony <github@nieslony.at>
- Add dependencies
