%global debug_package %{nil}

Name: k9s
# renovate: datasource=github-releases depName=derailed/k9s
Version: 0.50.7
Release: 1%{?dist}
Summary: Kubernetes CLI To Manage Your Clusters In Style

License: Apache-2.0
URL: https://github.com/derailed/k9s
Source: %{url}/releases/download/v%{version}/%{name}_Linux_amd64.tar.gz

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%prep
%autosetup -c

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
