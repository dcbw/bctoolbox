Name:           bctoolbox
Version:        5.4.21
Release:        2.dcbw%{?dist}
Summary:        Utilities library used by Belledonne Communications

License:        GPL-3.0-or-later
URL:            https://github.com/BelledonneCommunications/bctoolbox

BuildRequires:  git cmake gcc-c++ doxygen
BuildRequires:  openssl-devel

Source0: %{name}-%{version}.tar.gz

%undefine _hardened_build
%undefine _annotated_build

%description
Utilities library used by Belledonne Communications softwares
like belle-sip, mediastreamer2 and liblinphone.

%package        devel
Summary:        Development libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Libraries and headers required to develop software with %{name}.


%prep
%autosetup -p1
# epel
sed -i 's|cmake_minimum_required(VERSION.*|cmake_minimum_required(VERSION 3.20)|g' CMakeLists.txt


%build
%global optflags %(echo %optflags | sed 's|-Wp,-D_GLIBCXX_ASSERTIONS||g')
%cmake -Wno-dev \
       -DCMAKE_SKIP_RPATH=YES \
       -DCMAKE_VERBOSE_MAKEFILE=NO \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DENABLE_STRICT=YES \
       -DENABLE_MBEDTLS=NO \
       -DENABLE_OPENSSL=YES \
       -DENABLE_TESTS_COMPONENT=NO
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE.txt
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_datadir}/*/cmake/*


%changelog
* Wed Jun 11 2025 Dan Williams <dan@ioncontrol.co> - 5.4.21-2.dcbw
- Clean up specfile

* Sun Jun  8 2025 Dan Williams <dan@ioncontrol.co> - 5.4.21-1.dcbw
- Update to 5.4.21

* Mon Apr 11 2022 Cristian Balint <cristian.balint@gmail.com>
- github upstream releases
