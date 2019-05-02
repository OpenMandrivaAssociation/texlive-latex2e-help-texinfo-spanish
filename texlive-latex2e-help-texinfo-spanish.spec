# revision 34129
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-latex2e-help-texinfo-spanish
Version:	20190228
Release:	1
Summary:	TeXLive latex2e-help-texinfo-spanish package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo-spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2e-help-texinfo-spanish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive latex2e-help-texinfo-spanish package.

#-----------------------------------------------------------------------
%files
%doc %{_infodir}/latex2e-es.info*
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-spanish/latex2e-es.dbk
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-spanish/latex2e-es.html
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-spanish/latex2e-es.pdf
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-spanish/latex2e-es.texi
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-spanish/latex2e-es.txt
%doc %{_texmfdistdir}/doc/latex/latex2e-help-texinfo-spanish/latex2e-es.xml

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
