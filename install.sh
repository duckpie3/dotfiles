#!/bin/sh

# Script to install my dotfiles

if [ "$USER" != "root" ]; then
    echo "Please run this script as root"
    exit 1
fi

# Ask the user for its username. This is so it can run the commands that require non root
read -p "Please provide your username: " username

userhome="/home/$username/"

echo "Checking for updates"
pacman -Syu --noconfirm && \

echo "Installing paru"
sudo -u $username git clone https://aur.archlinux.org/paru.git && \
cd paru && sudo -u $username makepkg -si --noconfirm && cd ..

# Make a backup of previous config(if there is one)
echo "Making a backup, just in case..."
mkdir $userhome/config_backup
cp -r $userhome/.config $userhome/config_backup/.config
cp $userhome/.xinitrc $userhome/config_backup/
cp $userhome/.zshrc $userhome/config_backup/
cp $userhome/.Xresources $userhome/config_backup/

# Copy config files
cp -r .local/ $userhome/
cp -r .config $userhome/
cp -r .vim $userhome/
mkdir -p $userhome/Pictures/wallpapers 
mkdir $userhome/Pictures/screenshots
cp .xinitrc .zshrc .Xresources $userhome

echo "Installing needed packages"
sudo -u $username paru -S --noconfirm qtile qtile-extras alacritty rofi ranger ueberzug \
		    zsh zsh-completions zsh-autosuggestions zsh-syntax-highlighting \
		    picom-simpleanims-git ttf-material-design-icons-desktop-git \
		    ttf-mononoki-nerd doas man htop \
		    xorg-xsetroot hsetroot xclip nsxiv \
		    zathura mpv shotgun hacksaw brillo polkit \
		    python-psutil python-iwlib python-pulsectl-asyncio

# Give root permisions with doas
echo "permit $username as root" | tee /etc/doas.conf

echo "Setting zsh as default shell"
sudo -u $username chsh -s /usr/bin/zsh

# Ask to install starship prompt
while true; do
    read -p "Do you wish to install starship prompt? " yn
    case $yn in
        [Yy]* ) curl -sS https://starship.rs/install.sh | sh ; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo "Congratulations, everything should be installed now :)"
