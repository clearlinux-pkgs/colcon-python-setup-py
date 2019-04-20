#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-python-setup-py
Version  : 0.2.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/65/97/f0dac66d6afa400e339229398ffd250b7be320261fa32a13db3e41764567/colcon-python-setup-py-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/97/f0dac66d6afa400e339229398ffd250b7be320261fa32a13db3e41764567/colcon-python-setup-py-0.2.1.tar.gz
Summary  : Extension for colcon to support Python packages with the metadata in the setup.py file.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-python-setup-py-python = %{version}-%{release}
Requires: colcon-python-setup-py-python3 = %{version}-%{release}
Requires: colcon-core
Requires: setuptools
BuildRequires : buildreq-distutils3

%description
======================

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
%setup -q -n colcon-python-setup-py-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539915614
python3 setup.py build

%install
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
