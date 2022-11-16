Name:		texlive-luaimageembed
Version:	50788
Release:	1
Summary:	Embed images as base64-encoded strings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luaimageembed
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaimageembed.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaimageembed.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to embed images directly as base64-encoded
strings into an LuaLaTeX document. This can be useful, e. g. to
package a document with images into a single TeX file, or with
automatically generated graphics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luaimageembed
%doc %{_texmfdistdir}/doc/lualatex/luaimageembed

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
