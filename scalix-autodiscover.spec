Name:       scalix-autodiscover
Version:    0.0.9
Release:    1%{?dist}
Summary:    Scalix Autodiscover service
License:    Copyright 2018 Scalix, Inc. (www.scalix.com)
Source: %{name}.tar.gz
BuildArch: noarch
Group:      Applications/Communications
Vendor:     Scalix Corporation
URL:        http://www.scalix.com
Packager:   Scalix Support <support@scalix.com>
Requires:   python /usr/bin/pip libxml2-devel gcc python-devel

%description
The Autodiscover service minimizes user configuration
and deployment steps by providing clients access to email
and groupware server features.

%prep
%setup -q -c %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -f --archive * %{buildroot}
mkdir -p %{buildroot}/etc/httpd/conf.d/
ln -s /opt/scalix-autodiscover/cgi/httpd_directory.conf %{buildroot}/etc/httpd/conf.d/scalix_autodiscover_directory.conf

%post
$(type -p pip) install -r /opt/scalix-autodiscover/requirements.txt

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/httpd/conf.d/scalix_autodiscover_directory.conf
%config %attr(0555, nobody, nobody) /etc/opt/scalix-autodiscover/autodiscover.ini
/opt/scalix-autodiscover/cgi/httpd_directory.conf
/opt/scalix-autodiscover/cgi/httpd_vhost.conf
/opt/scalix-autodiscover/requirements.txt
%attr(0755, nobody, nobody) /opt/scalix-autodiscover/cgi/autodiscover.py

%changelog
