# qutemacs - a simple, preconfigured Emacs binding set for qutebrowser
#
# The aim of this binding set is not to provide bindings for absolutely
# everything, but to provide a stable launching point for people to make their
# own bindings.
#
# Installation:
#
# 1. Copy this file or add this repo as a submodule to your dotfiles.
# 2. Add this line to your config.py, and point the path to this file:
# config.source('qutemacs/qutemacs.py')

config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

# c.input.insert_mode.auto_enter = False
# c.input.insert_mode.auto_leave = False
c.input.insert_mode.plugins = True
c.input.insert_mode.auto_load = True

# Forward unbound keys
c.input.forward_unbound_keys = "all"

ESC_BIND = 'clear-keychain ;; mode-leave ; fullscreen --leave'

c.bindings.default['normal'] = {}
# Bindings
c.bindings.commands['normal'] = {
    # Navigation
    '<ctrl-n>': 'scroll-page 0 0.8',
    '<ctrl-p>': 'scroll-page 0 -0.8',
    '<alt-shift-.': 'scroll-to-perc',
    '<alt-shift-.>': 'scroll-to-perc 0',

    # Commands
    '<alt-x>': 'set-cmd-text :',
    '<ctrl-x><ctrl-c>': 'quit',

    # searching
    '<ctrl-s>': 'set-cmd-text /',
    '<ctrl-r>': 'set-cmd-text ?',
    '<Enter>': 'fake-key <Enter>', # to allow selection of links with enter after search

    # hinting
    '<f>': 'hint all', #foreground 
    '<b>': 'hint all tab-bg', #background
    '<w><l>': 'hint all yank-primary',
    '<w><w>': 'yank url',
    '<Alt-w>': 'yank url',
    #'<Alt-d><ctrl-c>': 'yank url',
    #'<d>': 'yank all download',

    # history
    '<alt-right>': 'forward',
    '<alt-left>': 'back',
    '<ctrl-x><h>': 'history',

    # bookmarks
    # 'b': 'bookmark-add',
    '<ctrl-x><b>': 'open qute://bookmarks',

    # tabs
    '<ctrl-tab>': 'tab-next',
    '<ctrl-shift-tab>': 'tab-prev',
    '<shift-alt-d>': 'tab-clone',
    #'<ctrl-x><b>': 'set-cmd-text -s :buffer',
    '<ctrl-x><k>': 'tab-close',
    '<ctrl-w>': 'tab-close',
    '<ctrl-shift-w>': 'tab-only', # close all tabs except last one
    '<ctrl-m>': 'tab-mute',
    '<Alt-1>': 'tab-focus 1',
    '<Alt-2>': 'tab-focus 2',
    '<Alt-3>': 'tab-focus 3',
    '<Alt-4>': 'tab-focus 4',
    '<Alt-5>': 'tab-focus 5',
    '<Alt-6>': 'tab-focus 6',
    '<Alt-7>': 'tab-focus 7',
    '<Alt-8>': 'tab-focus 8',
    '<Alt-9>': 'tab-focus -1',

    # frames
    '<ctrl-x><5><0>': 'close',
    '<ctrl-x><5><1>': 'window-only',
    '<ctrl-x><5><2>': 'set-cmd-text -s :open -w',
    '<ctrl-u><ctrl-x><5><2>': 'set-cmd-text -s :open -p',

    # open links
    '<g>': 'set-cmd-text -s :open',
    '<ctrl-t>': 'set-cmd-text -s :open -t',

    # editing
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    '<ctrl-n>': 'fake-key <Down>',
    '<ctrl-p>': 'fake-key <Up>',
    '<alt-f>': 'fake-key <Ctrl-Right>',
    '<alt-b>': 'fake-key <Ctrl-Left>',
    '<ctrl-d>': 'fake-key <Delete>',
    '<alt-d>': 'fake-key <Ctrl-Delete>',
    '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
    '<ctrl-y>': 'insert-text {primary}',

    # Numbers
    # https://github.com/qutebrowser/qutebrowser/issues/4213
    '1': 'fake-key 1',
    '2': 'fake-key 2',
    '3': 'fake-key 3',
    '4': 'fake-key 4',
    '5': 'fake-key 5',
    '6': 'fake-key 6',
    '7': 'fake-key 7',
    '8': 'fake-key 8',
    '9': 'fake-key 9',
    '0': 'fake-key 0',

    # misc
    #'<ctrl-c><v>': 'spawn --userscript ~/.bin/open_in_mpv.sh',

    # Help
    '<ctrl-h><c>': 'open qute://bindings', # "C-h c" describe key in emacs
    '<ctrl-h><h>': 'set-cmd-text -s :help',

    # escape hatch
    '<ctrl-g>': ESC_BIND,
}

c.bindings.commands['command'] = {
    '<ctrl-s>': 'search-next',
    '<ctrl-r>': 'search-prev',

    '<ctrl-p>': 'completion-item-focus prev',
    '<ctrl-n>': 'completion-item-focus next',

    '<alt-p>': 'command-history-prev',
    '<alt-n>': 'command-history-next',

    # escape hatch
    '<ctrl-g>': 'mode-leave',
}

c.bindings.commands['hint'] = {
    # escape hatch
    '<ctrl-g>': 'mode-leave',
}


c.bindings.commands['caret'] = {
    # escape hatch
    '<ctrl-g>': 'mode-leave',
}

c.bindings.commands['insert'] = {
    # editing
    '<ctrl-f>': 'fake-key <Right>',
    '<ctrl-b>': 'fake-key <Left>',
    '<ctrl-a>': 'fake-key <Home>',
    '<ctrl-e>': 'fake-key <End>',
    #'<ctrl-n>': 'fake-key <Down>',
    #'<ctrl-p>': 'fake-key <Up>',
    #'<alt-f>': 'fake-key <Ctrl-Right>',
    #'<alt-b>': 'fake-key <Ctrl-Left>',
    #'<ctrl-d>': 'fake-key <Delete>',
    #'<alt-d>': 'fake-key <Ctrl-Delete>',
    #'<alt-backspace>': 'fake-key <Ctrl-Backspace>',
    '<ctrl-y>': 'insert-text {primary}',
    '<ctrl-g>': 'mode-leave'
}
