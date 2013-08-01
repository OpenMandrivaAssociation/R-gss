%global packname  gss
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.0_14
Release:          1
Summary:          General Smoothing Splines
Group:            Sciences/Mathematics
License:          GPLv3
URL:              http://cran.r-project.org/web/packages/gss/index.html
Source0:          http://cran.r-project.org/src/contrib/gss_2.0-14.tar.gz
Requires:         R-core
BuildRequires:    R-devel

%description
A comprehensive package for structural multivariate function 
estimation using smoothing splines.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R