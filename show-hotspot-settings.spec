Name:       show-hotspot-settings
Version:    0.2.1
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
install -D -m 644 -t %{buildroot}/%{_licensedir}/%{name} LICENSE
install -D -m 644 -t %{buildroot}/%{_sysconfdir}/httpd/conf.d apache-config/*
install -D -m 644 -t %{buildroot}/%{_localstatedir}/www/%{name} web/*{py,wsgi}
install -D -m 644 -t %{buildroot}/%{_localstatedir}/www/%{name}/templates web/templates/*
install -D -m 644 -t %{buildroot}/%{_localstatedir}/www/%{name}/static  web/static/*

%files
%{_sysconfdir}/httpd/conf.d/*
%{_localstatedir}/www/%{name}
%license LICENSE
