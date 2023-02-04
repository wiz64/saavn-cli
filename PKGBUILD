# Maintainer: wiz64 <contact@wiz64.com>
pkgname=saavn-cli
_pkgname=saavn-cli
pkgver=1.1.3.r3.gd73ad9d
pkgrel=1
pkgdesc="Command Line tool to search, download MP3 songs from Saavn Library. Open-source, and High Quality Music"
arch=('any')
url="https://github.com/wiz64/${_pkgname}"
license=('MIT')
provides=($_pkgname)
conflicts=($_pkgname)
depends=('python-pip')
makedepends=('git')
source=("$pkgname::git+https://github.com/wiz64/saavn-cli.git")
md5sums=('SKIP')

pkgver() {
  cd $pkgname
  git describe --tags --long | sed -r -e 's,^[^0-9]*,,;s,([^-]*-g),r\1,;s,[-_],.,g'
}

package() {
    cd $pkgname
  #make DESTDIR="$pkgdir" install
    python -m pip install -r requirements.txt 
    python -m pip install pyinstaller 
    python -m PyInstaller --icon=icon.ico --onefile saavn-cli.py -n saavn-cli
    chmod 777 dist/saavn-cli 
    cd dist
    install -D -m755 saavn-cli "$pkgdir/usr/bin/saavn-cli"
}
