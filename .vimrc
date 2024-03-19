" Some basic settings
set nocompatible
set number
set wrap
set encoding=utf-8
syntax on
filetype on
set mouse=a
colorscheme disco

" Set search highlightning and toggle keybinding to f3
set hlsearch!
nnoremap <F3> :set hlsearch!<CR>


" Set the cursor style
let &t_SI = "\e[5 q"   " Insert mode: blinkink vertical 
let &t_EI = "\e[2 q"   " Normal mode: block
let &t_SR = "\e[4 q"   " Replace mode: underline
let &t_ti .= "\e[2 q"  " When Vim starts: block
" Reset terminal cursor on exit
augroup RestoreCursorShapeOnExit
    autocmd!
    autocmd VimLeave * :!printf "\e[0 q" 
augroup END
