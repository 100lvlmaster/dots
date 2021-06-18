#   Exports
export PATH="$PATH:/opt/flutter/bin"
export CHROME_EXECUTABLE="/opt/google/chrome/chrome"

# Go
set -g GOPATH $HOME/go
set -gx PATH $GOPATH/bin $PATH

#   Aliases
alias code="vscodium"
alias open="dolphin"
alias cl="clear"

starship init fish | source
