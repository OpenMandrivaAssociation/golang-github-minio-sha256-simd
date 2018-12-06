# https://github.com/minio/sha256-simd
%global goipath github.com/minio/sha256-simd
%global commit  ad98a36ba0da87206e3378c556abbfeaeaa98668
%global date    20171213

%gometa

Name:           %{goname}
Version:        0
Release:        0.9%{?dist}
Summary:        SHA256 implementation using SIMD instructions for Go
License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.9.20171213gitad98a36
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.8.20171213gitad98a36
- Bump to commit ad98a36.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git96c8f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git96c8f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.git96c8f86
- Bump to commit 96c8f86.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitf3ec2e4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf3ec2e4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.gitf3ec2e4
- Bump to commit f3ec2e4, adding support for the s390x arch.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.gite82e73b
- First package for Fedora

