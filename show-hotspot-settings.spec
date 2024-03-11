Name:       show-hotspot-settings
Version:    0.2.2
Release:    1%{?dist}
Summary:    Show current hotspot settings in web page

License:    GPL-3.0
URL:        http://www.nieslony.site/OpenVPN_Admin
Source0:    %{name}-%{version}.tar.gz

Requires: %{py3_dist Flask qrcode mod_wsgi}
Requires: httpd

%description
Show current hotspot settings in web page from NetworkManager ot hostapd

%prep
%setup

%install
mkdir -pv %{buildroot}/%{_datadir}/%{name}
install -D -m 644 -t %{buildroot}/%{_licensedir}/%{name} LICENSE
install -D -m 644 -t %{buildroot}/%{_datadir}/%{name} apache-config/*
install -D -m 644 -t %{buildroot}/%{_localstatedir}/www/%{name} web/*{py,wsgi}
install -D -m 644 -t %{buildroot}/%{_localstatedir}/www/%{name}/templates web/templates/*
install -D -m 644 -t %{buildroot}/%{_localstatedir}/www/%{name}/static  web/static/*

%files
%{_datadir}/%{name}/*
%{_localstatedir}/www/%{name}
%license LICENSE

%changelog
* Mon Mar 11 2024 Claas Nieslony <github@nieslony.at>
- Install apache config to /usr/share/... (github@nieslony.at)

* Mon Mar 11 2024 Claas Nieslony <github@nieslony.at>
- Add dependencies
