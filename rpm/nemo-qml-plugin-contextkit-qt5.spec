Summary: ContextKit QML bindings
Name: nemo-qml-plugin-contextkit-qt5
Version: 1.1
Release: 2
License: LGPLv2
Group: Applications/System
URL: https://github.com/nemomobile/nemo-qml-plugin-contextkit
Source0: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(contextkit-statefs) >= 0.2.34
BuildRequires: cmake >= 2.8
# qmlplugindump and its dependencies
BuildRequires: qt5-qtdeclarative-devel-tools
BuildRequires: qt5-plugin-platform-minimal
BuildRequires: qt5-qtdeclarative-import-qtquick2plugin

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DUSEQT=5
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%cmake -DUSEQT=5
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/freedesktop/contextkit/libcontextkit.so
%{_libdir}/qt5/qml/org/freedesktop/contextkit/qmldir
%{_libdir}/qt5/qml/org/freedesktop/contextkit/plugins.qmltypes
