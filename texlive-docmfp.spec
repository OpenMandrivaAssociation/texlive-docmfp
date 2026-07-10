%global tl_name docmfp
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2d
Release:	%{tl_revision}.1
Summary:	Document non-LaTeX code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/docmfp
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extends the doc package to cater for documenting non-LaTeX code, such as
Metafont or MetaPost, or other programming languages.

