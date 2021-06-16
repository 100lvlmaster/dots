#!/bin/sh

# Configs
cp -R ~/.config/kitty/ ./.config/
cp -R ~/.config/qtile ./.config/
cp -R ~/.config/rofi ./.config/
cp -R ~/.config/picom ./.config/
cp -R ~/.config/dunst ./.config/
cp -R ~/.config/redshift ./.config/
cp -R ~/.config/fish ./.config/
cp -R ~/.config/nvim/init.vim ./.config/nvim
cp -R ~/.config/nvim/coc-settings.json ./.config/nvim
cp -R ~/.zshrc ./
cp -R ~/.bashrc ./
cp -R ~/.nvimrc ./
cp -R ~/.vimrc ./

# Wallpapers
cp -R ~/wallpapers ./

# Push to git
git add .
git commit -m $((1 + $RANDOM % 10))
git push
