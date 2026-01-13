# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: conmon
Epoch: 100
Version: 2.1.13
Release: 1%{?dist}
Summary: OCI container runtime monitor
License: Apache-2.0
URL: https://github.com/containers/conmon/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?rhel} == 7
BuildRequires: devtoolset-11
BuildRequires: devtoolset-11-gcc
BuildRequires: devtoolset-11-gcc-c++
BuildRequires: devtoolset-11-libatomic-devel
%endif
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: glibc-static
BuildRequires: libseccomp-devel
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: systemd-devel
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
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-11/enable
%endif
set -ex && \
    export GIT_COMMIT="e21e7c85b7637e622f21c57675bf1154fc8b1866" && \
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
