%global debug_package %{nil}

# Turn off strip'ng of binaries
%global __strip /bin/true

Name:           grpc_php_plugin
Version:        1.70.1
Release:        1%{?dist}
Summary:        A PHP plugin for the C based gRPC protoc command
License:        Apache-2.0
URL:            https://github.com/grpc/grpc
BuildRequires:  git cmake

%description
%{summary}.

%prep
git clone -b v%{version} --depth 1 https://github.com/grpc/grpc grpc
cd grpc
git submodule update --init

%build
mkdir -p grpc/cmake/build
cd grpc/cmake/build
cmake ../..

make protoc grpc_php_plugin

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp grpc/cmake/build/%{name} %{buildroot}/usr/bin/
chmod +x %{buildroot}/usr/bin/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Mon Feb 24 2025 Jamie Curnow <jc@jc21.com> - 1.70.1-1
- v1.70.1
