#   Exports
export PATH="$PATH:/opt/flutter/bin"
export CHROME_EXECUTABLE="/opt/google/chrome/chrome"

# Go
set -g GOPATH $HOME/go
set -gx PATH $GOPATH/bin $PATH

#   Aliases
alias open="xdg-open"
alias cl="clear"
alias r="ranger"

starship init fish | source
