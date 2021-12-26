%define		kdeplasmaver	5.23.4
%define		kf_ver		5.78
%define		qt_ver		5.15.0
%define		kpname		wrapland
#
Summary:	Qt/C++ library wrapping libwayland
Name:		%{kpname}
Version:	0.523.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://gitlab.com/kwinft/%{kpname}/-/archive/%{kpname}@%{version}/%{name}-%{name}@%{version}.tar.bz2
# Source0-md5:	2f9c21645be7a8e968afd00abf25f92e
URL:		http://www.kde.org/
BuildRequires:	EGL-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.66.0
BuildRequires:	wayland-devel >= 1.18
BuildRequires:	wayland-protocols >= 1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Wrapland is a Qt/C++ library that wraps and mediates the libwayland
client and server API for its consumers. Wrapland is an independent
part of the [KWinFT project][kwinft-project] with the KWinFT window
manager being Wrapland's first and most prominent user.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{name}-%{name}@%{version}

%build
install -d build

cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_libdir}/libWraplandServer.so.0.*.*
%ghost %{_libdir}/libWraplandServer.so.0
%{_libdir}/libWraplandClient.so.0.*.*
%ghost %{_libdir}/libWraplandClient.so.0
%attr(755,root,root) %{_prefix}/libexec/org-kde-kf5-wrapland-testserver
%{_datadir}/qlogging-categories5/org_kde_wrapland.categories

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/Wrapland
%{_includedir}/wrapland_version.h
%{_libdir}/libWraplandServer.so
%{_libdir}/libWraplandClient.so
%{_includedir}/Wrapland
