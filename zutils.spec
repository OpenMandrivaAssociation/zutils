Name:		zutils
Summary:	Utilities dealing with compressed files
Version:	0.9
Release:	1
License:	GPLv3+
Group:		Archiving/Compression
URL:		http://www.nongnu.org/zutils/zutils.html
Source0:	http://download.savannah.gnu.org/releases/zutils/%{name}-%{version}.tar.lz
BuildRequires:	lzip
Provides:	gzip-utils
Conflicts:	gzip-utils

%description
Zutils is a collection of utilities able to deal with any combination
of compressed and non-compressed files transparently. If any given file,
including standard input, is compressed, its decompressed content is used.
Compressed files are decompressed on the fly; no temporary files are created.
These utilities are not wrapper scripts but safer and more efficient C++
programs. In particular the "--recursive" option is very efficient in those
utilities supporting it.

The provided utilities are:
Zcat - Decompresses and copies files to standard output.
Zcmp - Decompresses and compares two files byte by byte.
Zdiff - Decompresses and compares two files line by line.
Zgrep - Decompresses and searches files for a regular expression.
Ztest - Tests integrity of compressed files.

The supported compressors are bzip2, gzip, lzip and xz. 

%prep
%setup -q

%build
%configure
%make

%check
make check

%install
%makeinstall_std
%__install -d -m 755 %{buildroot}/bin
%__mv %{buildroot}%{_bindir}/zcat %{buildroot}/bin/
%__ln_s ../../bin/zcat %{buildroot}%{_bindir}/zcat

%files
/bin/zcat
%{_bindir}/z*
%{_infodir}/zutils.info*
%{_mandir}/man1/z*.1*

%post
%_install_info

%postun
%_remove_install_info
