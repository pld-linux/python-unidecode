%define		module	Unidecode
Summary:	ASCII transliterations of Unicode text
Name:		python-unidecode
Version:	0.04.9
Release:	2
License:	GPL v1+ or Artistic
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/U/Unidecode/%{module}-%{version}.tar.gz
# Source0-md5:	c156f2cf31dd186532f8b993629b5b91
URL:		http://pypi.python.org/pypi/Unidecode/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unidecode provides a function, 'unidecode(...)' that takes Unicode
data and tries to represent it in ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at transliteration -- i.e.,
conveying, in Roman letters, the pronunciation expressed by the text
in some other writing system.

This is a Python port of Text::Unidecode Perl module by Sean M. Burke
<sburke@cpan.org>.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/unidecode
