#!/usr/bin/env bash
# Wallpaper
nitrogen --restore &
# Dunst
dunst &
#/usr/lib/polkit-kde-authentication-agent-1 &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/pam_kwallet_init &

# Network manager for non ethernet connections
pkill volumeicon 
pkill cbatticon
pkill xfce4-power-manager
nm-applet &
volumeicon &
cbatticon &
xfce4-power-manager &

# Not using picom atm
# picom &
picom --config ~/.config/picom/picom.conf &
