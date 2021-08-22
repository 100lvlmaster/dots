#!/usr/bin/env bash
# Wallpaper
nitrogen --restore &
# Dunst
dunst &
#/usr/lib/polkit-kde-authentication-agent-1 &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/pam_kwallet_init &

# Network manager for non ethernet connections
nm-applet &

# Not using picom atm
# picom &
picom --config ~/.config/picom/picom.conf &
