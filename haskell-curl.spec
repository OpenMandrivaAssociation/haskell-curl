%define module curl

Name: haskell-%{module}
Version: 1.3.5
Release: %mkrel 2
Summary: Haskell binding to libcurl
Group: Development/Other
License: BSD3
Url: http://hackage.haskell.org/package/curl
Source: http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros
BuildRequires: curl-devel
Requires: curl

%description
libcurl is a client-side URL transfer library, supporting FTP, FTPS, HTTP,
HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS and FILE. libcurl supports
SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload,
proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate,
Kerberos4), file transfer resume, http proxy tunneling and more! 

This package provides a Haskell binding to libcurl.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_docdir/%{module}-%{version}
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot


