#!/bin/bash
# Create ideal file structure
#  --- PAPA KISS ----

mkdir -p ~/Docs/{flutter,react/nextjs,cloned,go,dockers,test} 

# Install starship shell prompt
curl -fsSL https://starship.rs/install.sh | bash

# Restore configs
cp -R ./.config ~/

# Restore profiles
cp -R ./.bashrc ~/
cp -R ./.zshrc ~/

# Restore wallpapers
cp -R ./wallpapers ~/

# Set wallpaper
nitrogen --set-scaled ./wallpapers/wallpaper.png
