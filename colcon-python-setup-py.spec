#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-python-setup-py
Version  : 0.2.2
Release  : 10
URL      : https://files.pythonhosted.org/packages/3b/c4/b9501c191351d886a31022a80d22205cf501f137772c64ba8f2015b0cd02/colcon-python-setup-py-0.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/c4/b9501c191351d886a31022a80d22205cf501f137772c64ba8f2015b0cd02/colcon-python-setup-py-0.2.2.tar.gz
Summary  : Extension for colcon to support Python packages with the metadata in the setup.py file.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-python-setup-py-python = %{version}-%{release}
Requires: colcon-python-setup-py-python3 = %{version}-%{release}
Requires: colcon-core
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core
BuildRequires : setuptools

%description
colcon-python-setup-py
======================
An extension for `colcon-core <https://github.com/colcon/colcon-core>`_ to identify packages with a ``setup.py`` file by introspecting the arguments to the ``setup()`` function call of  `setuptools <https://setuptools.readthedocs.io/en/latest/>`_.

%package python
Summary: python components for the colcon-python-setup-py package.
Group: Default
Requires: colcon-python-setup-py-python3 = %{version}-%{release}

%description python
python components for the colcon-python-setup-py package.


%package python3
Summary: python3 components for the colcon-python-setup-py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-python-setup-py package.


%prep
%setup -q -n colcon-python-setup-py-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564850766
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
