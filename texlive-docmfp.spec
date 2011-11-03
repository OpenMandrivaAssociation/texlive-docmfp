# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/docmfp
# catalog-date 2009-09-02 16:56:11 +0200
# catalog-license lppl
# catalog-version 1.2d
Name:		texlive-docmfp
Version:	1.2d
Release:	1
Summary:	Document non-LaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/docmfp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Extends the doc package to cater for documenting non-LaTeX
code, such as MetaFont or MetaPost, or other programming
languages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/docmfp/docmfp.sty
%doc %{_texmfdistdir}/doc/latex/docmfp/README
%doc %{_texmfdistdir}/doc/latex/docmfp/docmfp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/docmfp/docmfp.dtx
%doc %{_texmfdistdir}/source/latex/docmfp/docmfp.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
