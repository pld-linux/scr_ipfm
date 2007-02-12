# TODO: webapps, banner instead of echo
Summary:	scr_ipfm - on-site display of ipfm summaries
Summary(pl.UTF-8):   scr_ipfm - przedstawianie wyników z ipfm-a na stronie WWW
Name:		scr_ipfm
Version:	0.64
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/scripfm/%{name}-%{version}.tar.gz
# Source0-md5:	5867737ef5cbade35a42c66020b4f045
URL:		http://scripfm.sourceforge.net/
Requires:	apache
Requires:	ipfm
Requires:	sed
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ipfmdir	%{_datadir}/scr_ipfm
%define		_ipfmconf	/etc/ipfm

%description
scr_ipfm displays on the web the summaries of ipfm.

%description -l pl.UTF-8
scr_ipfm wyświetla na stronie WWW wyniki ipfm-a

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ipfmdir}
install -d $RPM_BUILD_ROOT%{_ipfmconf}

cp -af *.php contrib images themes $RPM_BUILD_ROOT%{_ipfmdir}

cp -af ipfm.conf-sample $RPM_BUILD_ROOT%{_ipfmconf}

echo "alias %{_datadir}/scr_ipfm/ /scripfm/" > %{_sysconfdir}/httpd/scr_ipfm.conf
ln -s "%{_sysconfdir}/httpd/scr_ipfm.conf" "%{_sysconfdir}/httpd/httpd.conf/99_scr_ipfm.conf"

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Edit configuration file at %{_sysconfdir}/ipfm/ipfm.cnf-sample and replace ipfm.conf"
echo "More: %{_datadir}/doc/%{name}-%{version}/"

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README README_pl THANKS TODO
%dir %{_ipfmdir}
%{_ipfmdir}/contrib
%{_ipfmdir}/images
%{_ipfmdir}/themes
%{_ipfmdir}/*.*
%config(noreplace) %verify(not md5 mtime size) %{_ipfmconf}/ipfm.conf-sample
