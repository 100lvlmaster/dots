#   Starship 

eval "$(starship init zsh)"

#   Exports

export PATH="$PATH:/opt/flutter/bin"

#	Go
export PATH="$PATH:$HOME/go/bin"

#   Aliases

alias connect="adb connect 192.168.0.110:5555"
alias powersave60="sudo pstate-frequency -S -m 60"
alias powersave="sudo pstate-frequency -S -m 70"
alias open="xdg-open"

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
