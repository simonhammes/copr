%global debug_package %{nil}

Name: dops
# renovate: datasource=github-releases depName=Mikescher/better-docker-ps
Version: 1.16
Release: 1%{?dist}
Summary: better docker ps
License: MIT
URL: https://github.com/Mikescher/better-docker-ps
Source: %{url}/releases/download/v%{version}/%{name}_linux-amd64

%description
A replacement for the default docker-ps that tries really hard to fit within your terminal width.

%prep
# Do not use autosetup since skaffold is delivered as a binary (and not as a .tar.gz)
cp %{SOURCE0} .

%build

%install
install -p -D %{name}_linux-amd64 %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
