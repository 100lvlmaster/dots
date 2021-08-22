#! /bin/sh

# Create ideal file structure
#  --- PAPA KISS ----

mkdir -p ~/Docs/{flutter,cloned,go,dockers,test,nextjs} 

# Install starship shell prompt
curl -fsSL https://starship.rs/install.sh | bash

# Restore configs
cp -R ./{.config,.bashrc,.zshrc,.vimrc} ~/


# Set wallpaper
nitrogen --set-scaled wallpapers/wallpaper.png

