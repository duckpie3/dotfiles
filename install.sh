#!/bin/sh

# Script to install my dotfiles

if [ "$USER" != "root" ]; then
    echo "Please run this script as root"
    exit 1
fi

# Ask the user for its user. This is so it can run the commands that require non root
read -p "Please provide your user: " user

home="/home/$user/"

echo "Checking for updates"
pacman -Syu --noconfirm && \

echo "Installing paru"
sudo -u $user git clone https://aur.archlinux.org/paru.git && \
cd paru && sudo -u $user makepkg -si --noconfirm && cd ..

# Make a backup of previous config(if there is one)
echo "Making a backup, just in case..."
mkdir $home/config_backup
cp -r $home/.config $home/config_backup/.config
cp $home/.xinitrc $home/config_backup/
cp $home/.zshrc $home/config_backup/
cp $home/.Xresources $home/config_backup/

# Copy config files
sudo -u $user cp -r .local/ $home/
sudo -u $user cp -r .config $home/
sudo -u $user cp -r .vim $home/
sudo -u $user mkdir -p $home/Pictures/wallpapers 
sudo -u $user mkdir $home/Pictures/screenshots
sudo -u $user cp .xinitrc .zshrc .Xresources $home

echo "Installing needed packages"
sudo -u $user paru -S --noconfirm qtile qtile-extras alacritty rofi ranger ueberzug \
		    zsh zsh-completions zsh-autosuggestions zsh-syntax-highlighting \
		    picom-simpleanims-git ttf-material-design-icons-desktop-git \
		    ttf-mononoki-nerd doas man htop \
		    xorg-xsetroot hsetroot xclip nsxiv \
		    zathura mpv shotgun hacksaw brillo polkit \
		    python-psutil python-iwlib python-pulsectl-asyncio dunst

# Give root permisions with doas
echo "permit $user as root" | tee /etc/doas.conf

echo "Setting zsh as default shell"
sudo -u $user chsh -s /usr/bin/zsh

# Ask to install starship prompt
while true; do
    read -p "Do you wish to install starship prompt[Y/n]? " yn
    case $yn in
        [Yy]* ) curl -sS https://starship.rs/install.sh | sh ; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo "Congratulations, everything should be installed now :)"
