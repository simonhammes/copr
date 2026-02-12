%global debug_package %{nil}

Name: skaffold
# renovate: datasource=github-releases depName=GoogleContainerTools/skaffold
Version: 2.17.2
Release: 1%{?dist}
Summary: Easy and Repeatable Kubernetes Development

License: Apache-2.0
URL: https://github.com/GoogleContainerTools/skaffold
Source: %{url}/releases/download/v%{version}/%{name}-linux-amd64

%description
Skaffold is a command line tool that facilitates continuous development for Kubernetes applications.
You can iterate on your application source code locally then deploy to local or remote Kubernetes clusters.
Skaffold handles the workflow for building, pushing and deploying your application.
It also provides building blocks and describe customizations for a CI/CD pipeline.

%prep
# Do not use autosetup since skaffold is delivered as a binary (and not as a .tar.gz)
cp %{SOURCE0} .

%build

%install
install -p -D skaffold-linux-amd64 %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
