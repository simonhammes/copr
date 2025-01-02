%global debug_package %{nil}

Name: k3sup
# renovate: datasource=github-releases depName=alexellis/k3sup
Version: 0.13.6
Release: 1%{?dist}
Summary: Bootstrap K3s over SSH in < 60s

License: MIT
URL: https://github.com/alexellis/k3sup
Source: %{url}/releases/download/%{version}/%{name}

%description
k3sup is a light-weight utility to get from zero to KUBECONFIG with k3s on any local or remote VM.
All you need is ssh access and the k3sup binary to get kubectl access immediately.

%prep
# Do not use autosetup since k3sup is delivered as a binary (and not as a .tar.gz)
cp %{SOURCE0} .

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
