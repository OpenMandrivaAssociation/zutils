%global debug_package %{nil}

Name:		zutils
Summary:	Utilities dealing with compressed files
Version:	1.10
Release:	1
License:	GPLv3+
Group:		Archiving/Compression
URL:		http://www.nongnu.org/zutils/zutils.html
Source0:	http://download.savannah.gnu.org/releases/zutils/%{name}-%{version}.tar.lz
Source1:	%{name}.rpmlintrc
BuildRequires:	lzip
# (tpg) enable when obsoleting gzip-utils
# MD don't provide it without obsoleting it properly
# and gzip is actually more current, so ....
#Provides:	gzip-utils
#Conflicts:	gzip-utils

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
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

# (tpg) enable when obsoleting gzip-utils
#install -d -m 755 %{buildroot}/bin
#mv %{buildroot}%{_bindir}/zcat %{buildroot}/bin/
#ln -s ../../bin/zcat %{buildroot}%{_bindir}/zcat

%files
# (tpg) enable when obsoleting gzip-utils
#/bin/zcat
%{_sysconfdir}/zutilsrc
%{_bindir}/z*
%{_infodir}/zutils.info*
%{_mandir}/man1/z*.1*
