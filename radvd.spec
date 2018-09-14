#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x411FA8C112D91A31 (reubenhwk@gmail.com)
#
Name     : radvd
Version  : 2.17
Release  : 1
URL      : http://www.litech.org/radvd/dist/radvd-2.17.tar.xz
Source0  : http://www.litech.org/radvd/dist/radvd-2.17.tar.xz
Source99 : http://www.litech.org/radvd/dist/radvd-2.17.tar.xz.asc
Summary  : A Router Advertisement daemon
Group    : Development/Tools
License  : BSD-4-Clause
Requires: radvd-bin
Requires: radvd-config
Requires: radvd-license
Requires: radvd-man
BuildRequires : bison
BuildRequires : flex
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev

%description
radvd is the router advertisement daemon for IPv6.  It listens to router
solicitations and sends router advertisements as described in "Neighbor
Discovery for IP Version 6 (IPv6)" (RFC 2461).  With these advertisements
hosts can automatically configure their addresses and some other
parameters.  They also can choose a default router based on these
advertisements.

Install radvd if you are setting up IPv6 network and/or Mobile IPv6
services.

%package bin
Summary: bin components for the radvd package.
Group: Binaries
Requires: radvd-config
Requires: radvd-license
Requires: radvd-man

%description bin
bin components for the radvd package.


%package config
Summary: config components for the radvd package.
Group: Default

%description config
config components for the radvd package.


%package license
Summary: license components for the radvd package.
Group: Default

%description license
license components for the radvd package.


%package man
Summary: man components for the radvd package.
Group: Default

%description man
man components for the radvd package.


%prep
%setup -q -n radvd-2.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536931873
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1536931873
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/radvd
cp COPYRIGHT %{buildroot}/usr/share/doc/radvd/COPYRIGHT
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/radvd
/usr/bin/radvdump

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/radvd.service

%files license
%defattr(-,root,root,-)
/usr/share/doc/radvd/COPYRIGHT

%files man
%defattr(-,root,root,-)
/usr/share/man/man5/radvd.conf.5
/usr/share/man/man8/radvd.8
/usr/share/man/man8/radvdump.8
