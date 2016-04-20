Name:           python-zmq
Version:        14.7.0
Release:        1%{?dist}
Summary:        Software library for fast, message-based applications

License:        LGPL and BSD
URL:            http://www.zeromq.org/bindings:python
Source0:        https://pypi.python.org/packages/source/p/pyzmq/pyzmq-%{version}.tar.gz

BuildRequires:  chrpath
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  zeromq-devel
BuildRequires:  python-nose
BuildRequires:  Cython

Provides: python2-zmq


%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the python bindings.


%prep
%setup -q -n pyzmq-%{version}

rm -rf bundled

find zmq -name "*.c" -delete
%{__python} setup.py cython

chmod -x examples/pubsub/topics_pub.py
chmod -x examples/pubsub/topics_sub.py


%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
chrpath --delete %{buildroot}%{python_sitearch}/zmq/{backend/cython,devices}/*.so


%check
rm zmq/__*
PYTHONPATH=%{buildroot}%{python_sitearch} %{__python} setup.py test


%files
%doc AUTHORS.md CONTRIBUTING.md COPYING.* README.md examples/
%{python_sitearch}/*.egg-info
%{python_sitearch}/zmq/


%changelog
* Wed Apr 20 2016 Jajauma's Packages <jajauma@yandex.ru> - 14.7.0-1
- Public release
