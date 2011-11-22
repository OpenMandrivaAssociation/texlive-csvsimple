# revision 24575
# category Package
# catalog-ctan /macros/latex/contrib/csvsimple
# catalog-date 2011-11-11 11:59:57 +0100
# catalog-license lppl1.3
# catalog-version 1.04
Name:		texlive-csvsimple
Version:	1.04
Release:	1
Summary:	Simple CSV file processing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csvsimple
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvsimple.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csvsimple.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a simple LaTeX interface for the
processing of files with comma separated values (CSV); it
relies on the key value syntax supported by pgfkeys to simplify
usage. Filtering and table generation is especially supported;
however, this lightweight tool offers no support for data
sorting or data base storage.

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
%{_texmfdistdir}/tex/latex/csvsimple/csvsimple.sty
%doc %{_texmfdistdir}/doc/latex/csvsimple/CHANGES
%doc %{_texmfdistdir}/doc/latex/csvsimple/README
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple-example.csv
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple-example.pdf
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple-example.tex
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
