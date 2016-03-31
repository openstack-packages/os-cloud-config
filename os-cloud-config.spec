%global commit fd26d9d7e1211d6a795cbd678599dbc0975fc176
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:			os-cloud-config
Version:		0.4.1
Release:		2%{alphatag}%{?dist}
Summary:		Configuration for OpenStack clouds

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:                https://github.com/openstack/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildArch:		noarch
BuildRequires:		python-setuptools
BuildRequires:		python2-devel
BuildRequires:		python-pbr
BuildRequires:          git

Requires:		python-setuptools
Requires:		python-argparse
Requires:		python-oslo-config
Requires:		python-babel
Requires:		python-keystoneclient
Requires:		python-novaclient
Requires:		python-pbr
# Add Back Requires on python-ironicclient once it's actually available
# Requires:		python-ironicclient
Requires:		pyOpenSSL

%description
os-cloud-config offers a suite of tools and libraries used to do the initial
configuration of OpenStack clouds.

%prep
%autosetup -n %{name}-%{commit} -S git

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/os_cloud_config*
%{_bindir}/generate-keystone-pki
%{_bindir}/init-keystone
%{_bindir}/init-keystone-heat-domain
%{_bindir}/register-nodes
%{_bindir}/setup-endpoints
%{_bindir}/setup-flavors
%{_bindir}/setup-neutron
%{_bindir}/upload-kernel-ramdisk

%changelog
* Fri Apr  1 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4.1-2.fd26d9dgit
- Include keystone bugfix

* Thu Mar 31 2016 RDO <rdo-list@redhat.com> 0.4.1-1
- RC1 Rebuild for Mitaka RC1 0.4.1
