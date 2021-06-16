#   Exports
export PATH="$PATH:/opt/flutter/bin"
export CHROME_EXECUTABLE="/opt/google/chrome/chrome"

# Go
set -g GOPATH $HOME/go
set -gx PATH $GOPATH/bin $PATH

#   Aliases
alias code="vscodium"
alias connect="adb connect 192.168.0.110:5555"
alias powersave60="sudo pstate-frequency -S -m 60"
alias powersave="sudo pstate-frequency -S -m 70"
alias open="dolphin"

starship init fish | source
