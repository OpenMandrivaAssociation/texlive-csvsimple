Name:		texlive-csvsimple
Version:	1.20
Release:	2
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
%{_texmfdistdir}/tex/latex/csvsimple
%doc %{_texmfdistdir}/doc/latex/csvsimple

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
