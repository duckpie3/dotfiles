export PATH="$HOME/.local/bin:$PATH"
xrdb ~/.Xresources &
~/.restore_bg
picom -b
exec qtile start
