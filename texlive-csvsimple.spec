# revision 31777
# category Package
# catalog-ctan /macros/latex/contrib/csvsimple
# catalog-date 2013-09-25 21:12:12 +0200
# catalog-license lppl1.3
# catalog-version 1.07
Name:		texlive-csvsimple
Version:	1.07
Release:	3
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

%description
The package provides a simple LaTeX interface for the
processing of files with comma separated values (CSV); it
relies on the key value syntax supported by pgfkeys to simplify
usage. Filtering and table generation is especially supported;
however, this lightweight tool offers no support for data
sorting or data base storage.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/csvsimple/csvsimple.sty
%doc %{_texmfdistdir}/doc/latex/csvsimple/CHANGES
%doc %{_texmfdistdir}/doc/latex/csvsimple/README
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple-example.pdf
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple-example.tex
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple.pdf
%doc %{_texmfdistdir}/doc/latex/csvsimple/csvsimple.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
