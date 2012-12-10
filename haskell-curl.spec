%global debug_package %{nil}
#% define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module curl
Name:           haskell-%{module}
Version:        1.3.8
Release:        1
Summary:        Haskell binding to libcurl
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  curl-devel
Requires(pre):  ghc
requires:       curl

%description
libcurl is a client-side URL transfer library, supporting FTP, FTPS, HTTP,
HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS and FILE.
libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading,
HTTP form based upload, proxies, cookies, user+password authentication
(Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer resume,
http proxy tunneling and more!
.
This package provides a Haskell binding to libcurl.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



