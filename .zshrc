# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt nomatch notify
unsetopt autocd beep extendedglob
bindkey -e
# End of lines configured by zsh-newuser-install

# The following lines were added by compinstall
zstyle :compinstall filename '$HOME/.zshrc'
autoload -Uz compinit
compinit
# End of lines added by compinstall

zstyle ':completion:*' menu select

# Key bindings
bindkey '^[[1;5D' backward-word
bindkey '^[[1;5C' forward-word
bindkey '^H' backward-kill-word

# Set the prompt
# PROMPT='%B%F{cyan}%~%b %(?.%F{green}.%F{red}) '

# Enhanced pretty zsh prompt
setopt PROMPT_SUBST
autoload -Uz colors && colors

export VIRTUAL_ENV_DISABLE_PROMPT=1         # virtualenv/venv
export PYENV_VIRTUALENV_DISABLE_PROMPT=1    # pyenv-virtualenv
export CONDA_CHANGEPS1=false                # conda (alt: `conda config --set changeps1 False`)

prompt_git() {
  local branch dirty
  command -v git >/dev/null 2>&1 || return 0
  git rev-parse --is-inside-work-tree >/dev/null 2>&1 || return 0
  branch=$(git symbolic-ref --quiet --short HEAD 2>/dev/null || git rev-parse --short HEAD 2>/dev/null)
  [[ -n "$(git status --porcelain 2>/dev/null)" ]] && dirty="*" || dirty=""
  printf '%%F{blue} %s%s%%f' "$branch" "$dirty"
}

prompt_venv() {
  local env=""
  if [[ -n "$VIRTUAL_ENV" ]]; then
    env="${VIRTUAL_ENV:t}"
  elif [[ -n "$CONDA_DEFAULT_ENV" ]]; then
    env="$CONDA_DEFAULT_ENV"
  elif [[ -n "$PYENV_VERSION" ]]; then
    env="$PYENV_VERSION"
  fi
  [[ -n "$env" ]] && printf '%%F{magenta}(%s)%%f' "$env"
}

PROMPT=$'%F{8}%D{%H:%M}%f %F{blue} %n%f %F{red} %m%f %F{yellow}  %~%f $(prompt_venv) $(prompt_git)
%(?.%F{green}❯%f.%F{red}❯%f) '

export PATH="$HOME/.local/bin:$PATH"
export EDITOR=nvim
export VISUAL=nvim

# Output cloloring
alias diff='diff --color=auto'
alias grep='grep --color=auto'
alias ip='ip -color=auto'
alias ls='ls -F --color=auto'
export MANPAGER="less -R --use-color -Dd+r -Du+b"
export LESS='-R --use-color -Dd+r$Du+b'

# Useful aliases
alias hx="helix"

# Syntax highlightning
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
# Autosuggestions
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

ZSH_AUTOSUGGEST_STRATEGY=(history completion)

eval "$(zoxide init zsh)"
