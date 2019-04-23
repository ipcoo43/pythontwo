
docker pull ubuntu:16.04
docker run -it ubuntu:16.04
apt update
apt install -y python3 python3-pip
pip3 install selenium
pip3 install beautifulsoup4
apt install -y wget libfontconfig
mkdir -p /home/root/src && cd $_
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
cd phantomjs-2.1.1-linux-x86_64/bin/
cp phantomjs /usr/local/bin/
apt install -y fonts-nanum*
exit
docker ps -a
docker commit <컨테이너이름:858f2bb41f78> ubnuntu-phantomjs