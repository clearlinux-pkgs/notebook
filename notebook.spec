#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : notebook
Version  : 5.7.4
Release  : 36
URL      : https://files.pythonhosted.org/packages/6e/22/b5dcce67559d63d0f22e46d806305710808c698a1b91c07eb09e389785e0/notebook-5.7.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/22/b5dcce67559d63d0f22e46d806305710808c698a1b91c07eb09e389785e0/notebook-5.7.4.tar.gz
Summary  : A web-based notebook environment for interactive computing
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: notebook-bin = %{version}-%{release}
Requires: notebook-license = %{version}-%{release}
Requires: notebook-python = %{version}-%{release}
Requires: notebook-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Send2Trash
Requires: ipykernel
Requires: ipython_genutils
Requires: jupyter_client
Requires: jupyter_core
Requires: nbconvert
Requires: nbformat
Requires: prometheus_client
Requires: pyzmq
Requires: terminado
Requires: tornado
Requires: traitlets
BuildRequires : Jinja2
BuildRequires : Send2Trash
BuildRequires : buildreq-distutils3
BuildRequires : ipykernel
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : nbconvert
BuildRequires : nbformat
BuildRequires : prometheus_client
BuildRequires : pyzmq
BuildRequires : terminado
BuildRequires : tornado
BuildRequires : traitlets

%description
The Jupyter Notebook is a web application that allows you to create and
        share documents that contain live code, equations, visualizations, and
        explanatory text. The Notebook has support for multiple programming
        languages, sharing, and interactive widgets.

%package bin
Summary: bin components for the notebook package.
Group: Binaries
Requires: notebook-license = %{version}-%{release}

%description bin
bin components for the notebook package.


%package license
Summary: license components for the notebook package.
Group: Default

%description license
license components for the notebook package.


%package python
Summary: python components for the notebook package.
Group: Default
Requires: notebook-python3 = %{version}-%{release}

%description python
python components for the notebook package.


%package python3
Summary: python3 components for the notebook package.
Group: Default
Requires: python3-core

%description python3
python3 components for the notebook package.


%prep
%setup -q -n notebook-5.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545246676
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/notebook
cp COPYING.md %{buildroot}/usr/share/package-licenses/notebook/COPYING.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-bundlerextension
/usr/bin/jupyter-nbextension
/usr/bin/jupyter-notebook
/usr/bin/jupyter-serverextension

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/notebook/COPYING.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
