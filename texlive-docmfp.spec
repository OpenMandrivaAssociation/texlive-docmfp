# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/docmfp
# catalog-date 2009-09-02 16:56:11 +0200
# catalog-license lppl
# catalog-version 1.2d
Name:		texlive-docmfp
Version:	1.2d
Release:	5
Summary:	Document non-LaTeX code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/docmfp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmfp.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2d-2
+ Revision: 751006
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2d-1
+ Revision: 718243
- texlive-docmfp
- texlive-docmfp
- texlive-docmfp
- texlive-docmfp

