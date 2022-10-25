# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt beep nomatch notify
unsetopt autocd
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/david/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

#(cat ~/.cache/wal/sequences &)
eval "$(starship init zsh)"
export PATH="/home/david/.local/bin:$PATH"

[ -f "/home/david/.ghcup/env" ] && source "/home/david/.ghcup/env" # ghcup-env

# Random cowsay with fortune
# cowsay -f $(ls /usr/share/cows | grep .cow | shuf | head -1) $(fortune -s)

# Lock the screen
alias lock="~/lock.sh"

# Run fetching program
# neofetch
# pfetch
#alias ufetch="~/ufetch.sh"
#ufetch

# Syntax highlightning
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Output cloloring
alias diff='diff --color=auto'
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias ls='ls --color=auto'
export MANPAGER="less -R --use-color -Dd+r -Du+b"
export LESS='-R --use-color -Dd+r$Du+b'

# Autosuggestions
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# Muestra el horario en la terminal
#alias horario="echo '\n' && kitty +icat Documents/Notes/horario.png"

rm(){ mv "$@" ~/trashcan/ }

# Following line was automatically added by arttime installer
export PATH=/home/gato/.local/bin:$PATH
