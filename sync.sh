#! /bin/sh

# Configs
echo 'Copying dot files...'
cp -R ~/{.zshrc,.vimrc,.bashrc,autostart.sh} .
cp -R ~/.config/{alacritty,kitty,qtile,rofi,picom,dunst,redshift,fish,nvim} ./.config/

# Save all packages to this text file 
echo 'Listing packages...'
pacman -Qe | awk '{print $1}' > package_list.txt

echo 'Pushing to git...'
# Push to git
git add .
git commit -m $((1 + $RANDOM % 10))
git push

