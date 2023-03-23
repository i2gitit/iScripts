!#bash
# Install apps on new Ubuntu Install

# Enable firewall
sudo ufw enable

# Install UFW GUI
sudo apt install gufw

# Install Neofetch (System Information)
sudo apt install neofetch

# Install lolcat (changes color of output)
sudo apt install lolcat

# Install wireshark (passive packet sniffing)
sudo apt install wireshark

# Install virtual box
sudo apt install virtualbox

# Install VLC
sudo apt install VLC

# Install gimp
sudo apt install gimp

# Install Inkscape
sudo apt install inkscape

# Multimedia Codecs
sudo apt install Ubuntu-restricted-extras

# Install TLP (Power Management)
sudo apt-get install tlp tlp-rdw
sudo systemct1 enable tlp

# Install Simple Screen Recorder
sudo apt-get install simplescreenrecorder

# Install OpenShot 
sudo add-apt-repository ppa:openshot.developers/ppa
sudo apt-get update
sudo apt-get install openshot-qt

# install KVM on Ubuntu 20.04
sudo apt -y install bridge-utils cpu-checker libvirt-clients libvirt-daemon qemu qemu-kvm

echo "Script Complete; Enjoy!"