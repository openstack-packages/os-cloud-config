Name:			os-cloud-config
Version:		XXX
Release:		1%{?dist}
Summary:		os-cloud-config

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:		noarch
BuildRequires:		python-setuptools
BuildRequires:		python2-devel

Requires:		python-setuptools
Requires:		python-argparse
Requires:		python-oslo-config
Requires:       python-babel
Requires:       python-keystoneclient
Requires:       python-novaclient
Requires:       python-ironicclient
Requires:       pyOpenSSL

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Configuration for OpenStack clouds.

%prep

%setup -q -n %{name}-%{upstream_version}

sed -i '/setuptools_git/d' setup.py
sed -i 's/__version__.*/__version__="%{version}"/'  os_cloud_config/__init__.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{python_sitelib}/os_cloud_config*
%{_bindir}/generate-keystone-pki
%{_bindir}/init-keystone
%{_bindir}/register-nodes
%{_bindir}/setup-endpoints
%{_bindir}/setup-neutron


%changelog
* Mon Aug 25 2014 Derek Higgins <derekh@redhat.com> - XXX
- Add setup-endpoints and setup-neutron

* Fri Aug 01 2014 Derek Higgins <derekh@redhat.com> - XXX
- initial package

