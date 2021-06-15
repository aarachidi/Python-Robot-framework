sudo apt update
wget https://dl.google.com/go/go1.13.5.linux-amd64.tar.gz
tar -xvzf go1.13.5.linux-amd64.tar.gz
sudo mv go /usr/local
PATH=$PATH:/usr/local/go/bin
source ~/.bashrc
sudo apt-get install git
sudo apt-get install unzip
sudo apt-get install qemu-user-static
sudo apt-get install e2fsprogs
sudo apt-get install dosfstools
sudo apt-get install libarchive-tools
wget https://releases.hashicorp.com/packer/1.4.5/packer_1.4.5_linux_amd64.zip
unzip packer_1.4.5_linux_amd64.zip
sudo mv packer /usr/local/bin/
git clone https://github.com/mkaczanowski/packer-builder-arm
mv script.sh packer-builder-arm
mv listPackage packer-builder-arm
cd packer-builder-arm
go mod download
go build
chmod 777 script.sh
sudo ./script.sh
sudo packer build boards/raspberry-pi/raspbian.json
