# ✨My dotfiles✨

![screenshot](screenshot.png)
![screenshot1](screenshot1.png)

- **WM:** Qtile
- **Terminal:** Alacritty
- **Shell:** zsh
- **File Explorer:** Ranger
- **App launcher**: Rofi
- **Doc reader:** Zathura
- **Font:** Mononoki
- **Colorscheme:** Tomorrow Night

## Installation

First, clone this repository.
```sh
git clone https://github.com/davidfffff/dotfiles
cd dotfiles
```

Install [paru](https://github.com/Morganamilo/paru) if not already installed.
```sh
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
```
Install the packages.
```sh
paru -S --noconfirm qtile qtile-extras alacritty rofi ranger ueberzug zsh zsh-commpletions zsh-autosuggestions zsh-syntax-highlighting picom-simpleanims-git ttf-material-design-icons-git ttf-jetbrains-mono-nerd doas man htop xorg-xsetroot hsetroot xclip imv zathura zathura-pdf-mupdf mpv hacksaw brillo polkit python-psutil python-iwlib python-pulsectl-asyncio python-dbus-next dunst
```
Make a backup in case other configuration files exist.
```sh
mv ~/.config config_backup
```

Copy all the configs from the repo.
```sh
cp -r .* ~/
rm -r ~/.git
```

Allow user to use doas(optional).
```sh
echo "permit $USER as root" | sudo tee /etc/doas.conf
```

Set zsh as default shell.
```sh
chsh -s /usr/bin/zsh
```
### Wallpaper artists
- https://www.artstation.com/paindude

### Cool stuff

- [ranger-devicons](https://github.com/alexanderjeurissen/ranger_devicons)
- [disco.vim](https://github.com/jsit/disco.vim)
