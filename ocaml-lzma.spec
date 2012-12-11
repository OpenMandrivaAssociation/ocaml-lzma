Name:           ocaml-lzma
Version:        0.01
Release:        %mkrel 3
Summary:        OCaml bindings for the LZMA compression library
License:        LGPL with static compilation exception
Group:          Development/Other
URL:            http://forge.ocamlcore.org/projects/ocaml-lzma/
Source0:        http://forge.ocamlcore.org/frs/download.php/378/ocaml-lzma-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  liblzma-devel

%description
OCaml bindings for the LZMA compression library.
Lzma provides very high compression ratio and fast decompression,
the average compression ratio is 30% better than that of gzip and
15% better than that of bzip2.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make
make doc

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml/lzma
mkdir -p %{buildroot}%{_libdir}/ocaml/stublibs
make install \
  PREFIX=%{buildroot}%{_libdir}/ocaml/lzma \
  SO_PREFIX=%{buildroot}%{_libdir}/ocaml/stublibs

mkdir examples
cp test_* examples/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt description.txt LICENSE.txt
%dir %{_libdir}/ocaml/lzma
%{_libdir}/ocaml/lzma/META
%{_libdir}/ocaml/lzma/*.cma
%{_libdir}/ocaml/lzma/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc examples
%{_libdir}/ocaml/lzma/*.a
%{_libdir}/ocaml/lzma/*.o
%{_libdir}/ocaml/lzma/*.cmxa
%{_libdir}/ocaml/lzma/*.cmx
%{_libdir}/ocaml/lzma/*.cmo
%{_libdir}/ocaml/lzma/*.mli
%{_libdir}/ocaml/stublibs/*.cmxs


%changelog
* Mon Nov 14 2011 Funda Wang <fwang@mandriva.org> 0.01-3mdv2012.0
+ Revision: 730508
- mandriva come with LZMA_PRESET_TEXT now

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.01-2mdv2011.0
+ Revision: 601657
- fix build with xz 5.0

* Mon Apr 26 2010 Florent Monnier <blue_prawn@mandriva.org> 0.01-1mdv2011.0
+ Revision: 539376
- BuildRequires: liblzma-devel
- BuildRequires: ocaml
- import ocaml-lzma


