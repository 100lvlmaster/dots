#!/bin/sh

# Install paru package manager

sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si


# Install all packages
awk '{print $1}'  package_list.txt |  xargs paru -S