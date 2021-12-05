#   Exports
export PATH="$PATH:/opt/flutter/bin"
export CHROME_EXECUTABLE="/opt/google/chrome/chrome"
export BROWSER=/usr/bin/brave
# Go
set -g GOPATH $HOME/go
set -gx PATH $GOPATH/bin $PATH

#   Aliases
alias open="xdg-open"
alias cl="clear"
alias r="ranger"
alias sail='[ -f sail ] && bash sail || bash vendor/bin/sail'


starship init fish | source
