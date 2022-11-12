Name:		texlive-docmfp
Version:	15878
Release:	1
Summary:	Document non-LaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/docmfp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extends the doc package to cater for documenting non-LaTeX
code, such as MetaFont or MetaPost, or other programming
languages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/docmfp/docmfp.sty
%doc %{_texmfdistdir}/doc/latex/docmfp/README
%doc %{_texmfdistdir}/doc/latex/docmfp/docmfp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/docmfp/docmfp.dtx
%doc %{_texmfdistdir}/source/latex/docmfp/docmfp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
