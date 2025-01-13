%global debug_package %{nil}

Name: watchexec
# renovate: datasource=github-releases depName=watchexec/watchexec
Version: 2.2.1
Release: 1%{?dist}
Summary: Executes commands in response to file modifications
License: Apache-2.0
URL: https://github.com/watchexec/watchexec
Source: %{url}/releases/download/v%{version}/%{name}-%{version}-x86_64-unknown-linux-gnu.tar.xz

%description
Software development often involves running the same commands over and over. Boring!
watchexec is a simple, standalone tool that watches a path and runs a command whenever it detects modifications.
Example use cases:
- Automatically run unit tests
- Run linters/syntax checkers
- Rebuild artifacts

%prep
%autosetup -c

%build

%install
install -p -D %{name}-%{version}-x86_64-unknown-linux-gnu/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
