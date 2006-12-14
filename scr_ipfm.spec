Summary:	scr_ipfm - on-site display of ipfm summaries
Summary(pl):	- scr_ipfm - przedstawia na stronie wyniki ipfm'a
Name:		scr_ipfm
Version:	0.64
Release:	1
License:	GPL
Group:		Aplications/WWW
######		Unknown group!
Source0:	http://dl.sourceforge.net/scripfm/%{name}-%{version}.tar.gz
URL:		http://scripfm.sourceforge.net/
Requires:	apache
Requires:	ipfm
Requires:	libcap
Requires:	sed
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define _ipfmdir /usr/share/scr_ipfm
%define _ipfmconf /etc/ipfm

%description
scr_ipfm displays on the web the summaries of ipfm

%description -l pl
scr_ipfm wy¶wietla na stronie www wyniki ipfm'a

%prep
%setup -q -a0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ipfmdir}
install -d $RPM_BUILD_ROOT%{_ipfmconf}

cp -af *.php contrib images themes $RPM_BUILD_ROOT%{_ipfmdir}

cp -af  ipfm.conf-sample $RPM_BUILD_ROOT%{_ipfmconf}

echo "alias %{_datadir}/scr_ipfm/ /scripfm" > %{_sysconfdir}/httpd/scr_ipfm.conf
ln -s "%{_sysconfdir}/httpd/scr_ipfm.conf" "%{_sysconfdir}/httpd/httpd.conf/99_scr_ipfm.conf"
%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$LANG" = "pl_PL" ]; then
echo
echo "Zedytuj plik konfiguracyjny w %{_sysconfdir}/ipfm/ipfm.conf-sample i zast±p ipfm.conf"
echo "Wiêcej: %{_datadir}/doc/scr_ipfm-%{version}/"
echo
else
echo
echo "Edit configuration file at %{_sysconfdir}/ipfm/ipfm.cnf-sample and replace ipfm.conf"
echo "More: %{_datadir}/doc/scr_ipfm-%{version}/"
echo
fi

%files
%defattr(644,root,root,755)
%doc BUGS COPYING ChangeLog README README_pl THANKS TODO
%dir %{_ipfmdir}
%{_ipfmdir}/contrib/
%{_ipfmdir}/images/
%{_ipfmdir}/themes/
%{_ipfmdir}/*.*
%dir %(_ipfmdir)
%config(noreplace) %{_ipfmconf}/ipfm.conf-sample
