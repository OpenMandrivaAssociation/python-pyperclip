Name:		python-pyperclip
Version:	1.11.0
Release:	1
Summary:	Cross-platform clipboard module for Python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/asweigart/pyperclip
Source0:	https://files.pythonhosted.org/packages/source/p/pyperclip/pyperclip-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
A cross-platform clipboard module for Python.

%files
%doc README.md
%license LICENSE.txt
%{py_sitedir}/pyperclip
%{py_sitedir}/pyperclip-*.*-info
