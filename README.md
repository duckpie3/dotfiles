# My Dotfiles

Welcome to my personal dotfiles repository! This branch focuses on my current **Wayland** setup configured around **Hyprland**. 

> Note: There are some older configurations in this repository (like Qtile and Picom) that I keep for archival purposes, but they are no longer actively used or maintained.

## 🪟 Window Manager & Environment
*   **Window Manager:** [Hyprland](https://hyprland.org/) - A highly customizable dynamic tiling Wayland compositor.
*   **Status Bar:** [Waybar](https://github.com/Alexays/Waybar) - Highly customizable Wayland bar for Sway and Wlroots based compositors.
*   **App Launchers:** [Tofi](https://github.com/philj56/tofi) / [Rofi](https://github.com/davatorium/rofi)
*   **Notifications:** [Mako](https://github.com/emersion/mako) / [Dunst](https://github.com/dunst-project/dunst)

## 💻 Terminal & CLI
*   **Terminal Emulator:** [Alacritty](https://github.com/alacritty/alacritty)
*   **Shell:** [Zsh](https://www.zsh.org/) (Configured via `.zshrc`)
*   **File Managers:** 
    *   [Yazi](https://github.com/sxyazi/yazi) (Blazing fast terminal file manager written in Rust)
    *   [Ranger](https://github.com/ranger/ranger)
    *   [Superfile](https://github.com/yorukot/superfile)
*   **System Monitor:** [Btop](https://github.com/aristocratos/btop)

## 📝 Editors & Viewers
*   **Editors:** [Helix](https://helix-editor.com/) / Vim
*   **PDF Reader:** [Zathura](https://pwmt.org/projects/zathura/)
*   **Image Viewer:** [IMV](https://sr.ht/~exec64/imv/)

## 📂 Repository Structure

```text
.
├── .config/
│   ├── alacritty/   # Terminal configuration
│   ├── btop/        # System monitor configuration
│   ├── helix/       # Modern modal editor
│   ├── hypr/        # Hyprland window manager configuration
│   ├── mako/        # Notification daemon
│   ├── tofi/        # Wayland launcher
│   ├── waybar/      # Status bar
│   ├── yazi/        # File manager
│   └── zathura/     # PDF viewer
├── .local/          # Local scripts and data
├── .vimrc           # Vim configuration
└── .zshrc           # Shell aliases, environments, and configuration
```

## 🚀 Installation

*Note: Proceed with caution and ensure you back up your existing configurations before symlinking or copying these files.*

1. Clone the repository:
   ```bash
   git clone -b hyprland https://github.com/duckpie3/dotfiles.git ~/dotfiles
   ```
2. Symlink the configurations to your `~/.config` or home directory using `ln -s` or a tool like [GNU Stow](https://www.gnu.org/software/stow/).
