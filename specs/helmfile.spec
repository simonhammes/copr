%global debug_package %{nil}

Name: helmfile
Version: 0.169.2
Release: 1%{?dist}
Summary: Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases

License: MIT
URL: https://github.com/helmfile/helmfile
# https://github.com/helmfile/helmfile/releases/download/v0.169.2/helmfile_0.169.2_linux_amd64.tar.gz
Source: %{url}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
# TODO: Source1 = Documentation

%description
Helmfile is a declarative spec for deploying helm charts. It lets you...

- Keep a directory of chart value files and maintain changes in version control.
- Apply CI/CD to configuration changes.
- Periodically sync to avoid skew in environments.

To avoid upgrades for each iteration of helm, the helmfile executable delegates to helm - as a result, helm must be installed.

%prep
%autosetup -c
# TODO: Documentation/Shell completions

%build
# TODO: Shell completions

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}
# TODO: Shell completions

%files
# TODO: Documentation/Shell completions
%{_bindir}/%{name}
