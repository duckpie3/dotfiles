xrandr -s 1920x1080
xrdb ~/.Xresources &
~/.restore_bg
picom --no-vsync &
exec bspwm
