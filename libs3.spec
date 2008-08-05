Summary: C Library for Amazon S3 Access
Name: libs3
Version: trunk
Release: 1
License: GPL
Group: Development/Tools
URL: http://sourceforge.net/projects/reallibs3
Source0: libs3-trunk.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires: curl-devel
Buildrequires: libxml2-devel
Buildrequires: make
Requires: curl
Requires: libxml2

%define debug_package %{nil}

%description
This library provides an API for using Amazon's S3 service (see
http://s3.amazonaws.com).  Its design goals are:

- To provide a simple and straightforward API for accessing all of S3's
  functionality
- To not require the developer using libs3 to need to know anything about:
    - HTTP
    - XML
    - SSL
  In other words, this API is meant to stand on its own, without requiring
  any implicit knowledge of how S3 services are accessed using HTTP
  protocols.
- To be usable from multithreaded code
- To be usable by code which wants to process multiple S3 requests
  simultaneously from a single thread
- To be usable in the simple, straightforward way using sequentialized
  blocking requests

%prep
%setup -q

%build
CFLAGS=-O3 BUILD=$RPM_BUILD_ROOT/build make exported

%install
BUILD=$RPM_BUILD_ROOT/build INSTALL=$RPM_BUILD_ROOT/usr make install
rm -rf $RPM_BUILD_ROOT/build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/*
/usr/include/*
/usr/lib/*

%changelog
* Tue Aug 05 2008  <bryan@ischo,com> Bryan Ischo
- Initial build.
