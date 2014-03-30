Name:		nagios-plugins-openstack
Version:	0.2
Release:	3%{?dist}
Summary:	Nagios Openstack Plugins

Group:		System Environment/Base
License:	UNKNOWN
URL:		http://www.example.com
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	/usr/bin/ceph, /usr/bin/cinder, /usr/bin/glance, /usr/bin/keystone, /usr/bin/heat, /usr/bin/neutron, /usr/bin/nova, /usr/bin/openstack-status

%description
some nagios checks that calls user programs to see if things are working

%prep
%setup -q


%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}%{_libdir}/nagios/plugins
install -m 755 plugins/* %{buildroot}%{_libdir}/nagios/plugins/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_libdir}/nagios/plugins/*


%changelog

