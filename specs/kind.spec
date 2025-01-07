%global debug_package %{nil}

Name: kind
# renovate: datasource=github-releases depName=kubernetes-sigs/kind
Version: 0.26.0
Release: 1%{?dist}
Summary: Kubernetes IN Docker - local clusters for testing Kubernetes

License: Apache-2.0
URL: https://github.com/kubernetes-sigs/kind
Source: %{url}/releases/download/v%{version}/%{name}-linux-amd64

%description
kind is a tool for running local Kubernetes clusters using Docker container "nodes".
kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

%prep
# Do not use autosetup since kind is delivered as a binary (and not as a .tar.gz)
cp %{SOURCE0} .

%build

%install
install -p -D %{name}-linux-amd64 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
