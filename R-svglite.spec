#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-svglite
Version  : 2.1.3
Release  : 17
URL      : https://cran.r-project.org/src/contrib/svglite_2.1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/svglite_2.1.3.tar.gz
Summary  : An 'SVG' Graphics Device
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-svglite-lib = %{version}-%{release}
Requires: R-cpp11
Requires: R-systemfonts
BuildRequires : R-cpp11
BuildRequires : R-systemfonts
BuildRequires : buildreq-R
BuildRequires : libpng-dev

%description
Graphics'. 'svglite' is a fork of the older 'RSvgDevice' package.

%package lib
Summary: lib components for the R-svglite package.
Group: Libraries

%description lib
lib components for the R-svglite package.


%prep
%setup -q -n svglite
pushd ..
cp -a svglite buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702281011

%install
export SOURCE_DATE_EPOCH=1702281011
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/svglite/DESCRIPTION
/usr/lib64/R/library/svglite/INDEX
/usr/lib64/R/library/svglite/Meta/Rd.rds
/usr/lib64/R/library/svglite/Meta/features.rds
/usr/lib64/R/library/svglite/Meta/hsearch.rds
/usr/lib64/R/library/svglite/Meta/links.rds
/usr/lib64/R/library/svglite/Meta/nsInfo.rds
/usr/lib64/R/library/svglite/Meta/package.rds
/usr/lib64/R/library/svglite/Meta/vignette.rds
/usr/lib64/R/library/svglite/NAMESPACE
/usr/lib64/R/library/svglite/NEWS.md
/usr/lib64/R/library/svglite/R/svglite
/usr/lib64/R/library/svglite/R/svglite.rdb
/usr/lib64/R/library/svglite/R/svglite.rdx
/usr/lib64/R/library/svglite/doc/fonts.R
/usr/lib64/R/library/svglite/doc/fonts.Rmd
/usr/lib64/R/library/svglite/doc/fonts.html
/usr/lib64/R/library/svglite/doc/index.html
/usr/lib64/R/library/svglite/doc/scaling.Rmd
/usr/lib64/R/library/svglite/doc/scaling.html
/usr/lib64/R/library/svglite/help/AnIndex
/usr/lib64/R/library/svglite/help/aliases.rds
/usr/lib64/R/library/svglite/help/figures/README-unnamed-chunk-3-1.png
/usr/lib64/R/library/svglite/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/svglite/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/svglite/help/figures/logo.png
/usr/lib64/R/library/svglite/help/figures/logo.svg
/usr/lib64/R/library/svglite/help/paths.rds
/usr/lib64/R/library/svglite/help/svglite.rdb
/usr/lib64/R/library/svglite/help/svglite.rdx
/usr/lib64/R/library/svglite/html/00Index.html
/usr/lib64/R/library/svglite/html/R.css
/usr/lib64/R/library/svglite/tests/testthat.R
/usr/lib64/R/library/svglite/tests/testthat/helper-aliases.R
/usr/lib64/R/library/svglite/tests/testthat/helper-manual.R
/usr/lib64/R/library/svglite/tests/testthat/helper-style.R
/usr/lib64/R/library/svglite/tests/testthat/test-clip.R
/usr/lib64/R/library/svglite/tests/testthat/test-clip.svg
/usr/lib64/R/library/svglite/tests/testthat/test-colour.R
/usr/lib64/R/library/svglite/tests/testthat/test-devSVG.R
/usr/lib64/R/library/svglite/tests/testthat/test-ids.R
/usr/lib64/R/library/svglite/tests/testthat/test-lines.R
/usr/lib64/R/library/svglite/tests/testthat/test-no-clip.svg
/usr/lib64/R/library/svglite/tests/testthat/test-output.R
/usr/lib64/R/library/svglite/tests/testthat/test-path.R
/usr/lib64/R/library/svglite/tests/testthat/test-points.R
/usr/lib64/R/library/svglite/tests/testthat/test-raster.R
/usr/lib64/R/library/svglite/tests/testthat/test-rect.R
/usr/lib64/R/library/svglite/tests/testthat/test-scale-text.html
/usr/lib64/R/library/svglite/tests/testthat/test-scale-text.svg
/usr/lib64/R/library/svglite/tests/testthat/test-scale.R
/usr/lib64/R/library/svglite/tests/testthat/test-text-fonts.R
/usr/lib64/R/library/svglite/tests/testthat/test-text.R
/usr/lib64/R/library/svglite/tests/testthat/test-text.svg

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/svglite/libs/svglite.so
/usr/lib64/R/library/svglite/libs/svglite.so.avx2
/usr/lib64/R/library/svglite/libs/svglite.so.avx512
