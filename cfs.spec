Summary:	Cryptographic Filesystem
Summary(pl):	Kryptograficzny system plików
Name:		cfs
Version:	1.3.3
Release:	2
License:	distributable
# Original source is unknown
Group:		Applications/File
Source0:	ftp://ftp.zedz.net/pub/crypto/disk/cfs/%{name}_%{version}.orig.tar.gz
# Source0-md5:	cb4c5c107b77a50c25628f6655aae378
Patch0:		http://non-us.debian.org/debian-non-US/dists/potato/non-US/main/source/%{name}_1.3.3-8.diff.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CFS pushes encryption services into the Unix(tm) file system. It
supports secure storage at the system level through a standard Unix
file system interface to encrypted files. Users associate a
cryptographic key with the directories they wish to protect. Files in
these directories (as well as their pathname components) are
transparently encrypted and decrypted with the specified key without
further user intervention; cleartext is never stored on a disk or sent
to a remote file server. CFS employs a novel combination of DES stream
and codebook cipher modes to provide high security with good
performance on a modern workstation. CFS can use any available file
system for its underlying storage without modification, including
remote file servers such as NFS. System management functions, such as
file backup, work in a normal manner and without knowledge of the key.

%description -l pl
CFS dodaje us³ugi szyfruj±ce do systemu plików Unixów. Obs³uguje on
bezpieczny zapis informacji poprzez standardowy interfejs systemu
plików dostêpny w Unixach. U¿ytkownicy przypisuj± kryptograficzne
klucze tym katalogom, które chc± zabezpieczyæ. Pliki w tych katalogach
(jak równie¿ ich nazwy) s± prze¼roczy¶cie szyfrowane i deszyfrowane z
podanym kluczem; dane czystym tekstem nigdy nie s± zapisywane na dysku
czy przesy³ane przez sieæ do zdalnego serwera.

%prep
%setup -q -n %{name}-%{version}.orig

%build
%{__make} cfs esm \
	CC="%{__cc}" \
	COPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install_cfs install_esm \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	ETCDIR=$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(,,)
