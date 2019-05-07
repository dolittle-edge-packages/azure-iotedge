%define iotedge_user iotedge
%define iotedge_group %{iotedge_user}
%define iotedge_home %{_localstatedir}/lib/iotedge
%define iotedge_logdir %{_localstatedir}/log/iotedge
%define iotedge_confdir %{_sysconfdir}/iotedge
%define iotedge_datadir %{_datadir}/iotedge

Name     : azure-iotedge
Version  : 1.0.6
Release  : 1
License  : MIT
Summary  : Azure IoT Edge Security Daemon
URL      : https://github.com/azure/iotedge
Source0  : https://github.com/dolittle-edge/azure-iotedge-clearlinux-build/releases/download/build-v1.0.6-29200/iotedge-1.0.6-29200.x86_64.tar.gz
Source1  : https://github.com/dolittle-edge/azure-iotedge-clearlinux-build/releases/download/build-v1.0.6-29200/libiothsm-std-1.0.6-29200.x86_64.tar.gz
Requires : docker

%description
Azure IoT Edge Security Daemon
Azure IoT Edge is a fully managed service that delivers cloud intelligence
locally by deploying and running artificial intelligence (AI), Azure services,
and custom logic directly on cross-platform IoT devices. Run your IoT solution
securely and at scale—whether in the cloud or offline.

This package contains the IoT Edge daemon and CLI tool.

%prep
%setup -c -a 1

%build

%install
rm -r /builddir/build/BUILDROOT/azure-iotedge-1.0.6-1.x86_64
cp -r /builddir/build/BUILD/azure-iotedge-1.0.6 /builddir/build/BUILDROOT/azure-iotedge-1.0.6-1.x86_64

%post
%systemd_post iotedge.service
%systemd_post iotedge-install.service

%preun
%systemd_preun iotedge.service
%systemd_preun iotedge-install.service

%postun
%systemd_postun_with_restart iotedge.service
%systemd_postun_with_restart iotedge-install.service

%files
%defattr(-, root, root, -)

# libs
/usr/lib64/libiothsm.so
/usr/lib64/libiothsm.so.1
/usr/lib64/libiothsm.so.1.0.6

# bins
/usr/bin/iotedge
/usr/bin/iotedged
/usr/bin/iotedge-install

# config
/usr/share/defaults/iotedge/config.yaml
/usr/share/defaults/iotedge/logrotate.d/iotedge

# man
/usr/share/man/man1/iotedge.1.gz
/usr/share/man/man8/iotedged.8.gz

# systemd
/usr/lib/systemd/system/iotedge.service
/usr/lib/systemd/system/iotedge-install.service

%doc /usr/share/doc/iotedge/LICENSE.gz
%doc /usr/share/doc/iotedge/ThirdPartyNotices.gz
%doc /usr/share/doc/iotedge/trademark

%changelog

