%global debug_package %{nil}

Name: scc
# renovate: datasource=github-releases depName=boyter/scc
Version: 3.6.0
Release: 1%{?dist}
Summary: scc is a very fast accurate code counter with complexity calculations and COCOMO estimates
License: MIT
URL: https://github.com/boyter/scc
Source: %{url}/releases/download/v%{version}/%{name}_Linux_x86_64.tar.gz

%description
A tool similar to cloc, sloccount and tokei.
For counting the lines of code, blank lines, comment lines, and physical lines of source code in many programming languages.
Goal is to be the fastest code counter possible, but also perform COCOMO calculation like sloccount, estimate code complexity similar to cyclomatic complexity calculators and produce unique lines of code or DRYness metrics.
In short one tool to rule them all.

%prep
%autosetup -c

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
