#!/usr/bin/env bash

shutdown="⏻ Shutdown"
reboot=" Reboot"
lock=" Lock"
logout="󰍃 Logout"
suspend="󰒲 Suspend"
hibernate=" Hibernate"

chosen=$(printf '%s\n' \
    "$shutdown" \
    "$reboot" \
    "$lock" \
    "$logout" \
    "$suspend" \
    "$hibernate" \
  | rofi -dmenu \
         -p "// SYSTEM" \
         -theme ~/.config/rofi/themes/powermenu.rasi \
         -mesg "press esc to cancel")

case "$chosen" in
    "$shutdown")  systemctl poweroff ;;
    "$reboot")    systemctl reboot ;;
    "$lock")      loginctl lock-session ;;
    "$logout")    loginctl terminate-session "$XDG_SESSION_ID" ;;
    "$suspend")   systemctl suspend ;;
    "$hibernate") systemctl hibernate ;;
esac
