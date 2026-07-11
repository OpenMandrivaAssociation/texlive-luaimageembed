%global tl_name luaimageembed
%global tl_revision 50788

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Embed images as base64-encoded strings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luaimageembed
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaimageembed.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaimageembed.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to embed images directly as base64-encoded strings
into an LuaLaTeX document. This can be useful, e. g. to package a
document with images into a single TeX file, or with automatically
generated graphics.

