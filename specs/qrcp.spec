%global debug_package %{nil}

Name: qrcp
# renovate: datasource=github-releases depName=claudiodangelis/qrcp
Version: 0.11.4
Release: 1%{?dist}
Summary: Transfer files over wifi from your computer to your mobile device by scanning a QR code without leaving the terminal

License: MIT
URL: https://github.com/claudiodangelis/qrcp
Source: %{url}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz

%description
Transfer files over Wi-Fi from your computer to a mobile device by scanning a QR code without leaving the terminal.

%prep
%autosetup -c

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
