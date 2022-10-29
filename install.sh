#!/bin/sh

echo "Updating packages"
pacman -Syu

echo "Installing paru"
git clone https://aur.archlinux.org/paru.git
cd paru; makepkg -si;cd

echo "Installing needed packages"
paru -S bspwm sxhkd alacritty rofi polybar ranger ueberzug \
	zsh zsh-completions zsh-autosuggestions zsh-syntax-highlighting \
	picom-ibhagwan-git ttf-material-design-icons-desktop-git \
	nerd-fonts-fantasque-sans-mono firefox doas man htop \
	xorg-xsetroot hsetroot dunst sxiv libnotify

cp --parents -r .local/bin ~
cp -r .config ~

echo "permit ${USER} as root" | sudo tee /etc/doas.conf

echo "Setting zsh as default shell"
chsh -s /usr/bin/zsh

echo "Installing starship prompt"
curl -sS https://starship.rs/install.sh | sh
