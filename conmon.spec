%global debug_package %{nil}

Name: conmon
Epoch: 100
Version: 2.1.1
Release: 1%{?dist}
Summary: OCI container runtime monitor
License: Apache-2.0
URL: https://github.com/containers/conmon/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: glibc-static
BuildRequires: libseccomp-devel
BuildRequires: libtool
BuildRequires: pkgconfig
Requires: libglib-2.0.so.0()(64bit)
Requires: libseccomp.so.2()(64bit)

%description
conmon is a monitoring program and communication tool between a
container manager (like podman or CRI-O) and an OCI runtime (like runc
or crun) for a single container.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
set -ex && \
    export GIT_COMMIT="65b6eaaf91ed8fd4ef0d5cd9038cff72667cc6be" && \
    export GIT_BRANCH="main" && \
    export GIT_BRANCH_CLEAN="main" && \
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
    export CFLAGS='-I /usr/include/libseccomp' && \
%endif
    make bin/conmon

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install.bin

%files
%license LICENSE
%{_bindir}/conmon

%changelog
