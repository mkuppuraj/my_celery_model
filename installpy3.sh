# This shell script installs below packages
# Python 3.4.3
# zc.buildout 2.5.0
# pip
# setuptools

PY3=3.4.3
ZC=2.5.0
PIP=7.1.2
SETUP=18.7.1
PREFIX=`pwd`/usr

rm -rf $PREFIX
mkdir $PREFIX

if [ ! -d 'downloads' ];
then
    mkdir downloads
fi

echo " https://www.python.org/ftp/python/$PY3/Python-$PY3.tgz -P ./downloads"
wget https://www.python.org/ftp/python/$PY3/Python-$PY3.tgz -P ./downloads
echo " https://pypi.python.org/packages/source/z/zc.buildout/zc.buildout-$ZC.tar.gz -P ./downloads"
wget https://pypi.python.org/packages/source/z/zc.buildout/zc.buildout-$ZC.tar.gz -P ./downloads
echo " https://pypi.python.org/packages/source/p/pip/pip-$PIP.tar.gz -P ./downloads"
wget https://pypi.python.org/packages/source/p/pip/pip-$PIP.tar.gz -P ./downloads
echo " https://pypi.python.org/packages/source/s/setuptools/setuptools-$SETUP.tar.gz -P ./downloads"
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-$SETUP.tar.gz -P ./downloads

# Install Python
tar xvf downloads/Python-$PY3.tgz
cd Python-$PY3/
./configure --prefix=$PREFIX
make
make install
cd ../
rm -rf Python-$PY3/

# Install Setuptools
tar xvf downloads/setuptools-$SETUP.tar.gz
cd setuptools-$SETUP/
$PREFIX/bin/python3 setup.py install
cd ../
rm -rf setuptools-$SETUP/

# Install zc.buildout
tar xvf downloads/zc.buildout-$ZC.tar.gz
cd zc.buildout-$ZC/
$PREFIX/bin/python3 setup.py install
cd ../
rm -rf zc.buildout-$ZC/

# Install pip
tar xvf downloads/pip-$PIP.tar.gz
cd pip-$PIP/
$PREFIX/bin/python3 setup.py install
cd ../
rm -rf pip-$PIP/
