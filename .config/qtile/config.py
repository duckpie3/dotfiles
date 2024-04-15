# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re, os

from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from colorscheme import *

# Keybindings and groups

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", 
        lazy.layout.grow_left().when(layout="bsp"),
        lazy.layout.grow().when(layout="monadtall"),
        desc="Grow window to the left"),
    Key([mod, "control"], "right",
        lazy.layout.grow_right().when(layout="bsp"),
        lazy.layout.shrink().when(layout="monadtall"),
        desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down().when(layout="bsp"), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up().when(layout="bsp"), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Put the focused window to/from floating mode"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Put the focused window to/from fullscreen"),

    
    Key([mod, "control"], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
    # Misc
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun -display-drun ''"), desc="Open rofi app menu"),
    Key([], "Print", lazy.spawn("screenshot"), desc="Take full screenshot"),
    Key(["shift"], "Print", lazy.spawn("screenshot -s"), desc="Take screenshot from selection"),
    Key(["control"], "Print", lazy.spawn("screenshot -c"), desc="Take full screenshot to clipboard"),
    Key(["shift", "control"], "Print", lazy.spawn("screenshot -sc"), desc="Take screenshot from selection to clipboard"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("notify-brightness + 5"), desc="Increase screen brightness"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("notify-brightness - 5"), desc="Decrease screen brightness"),

    Key([],"XF86AudioRaiseVolume", lazy.spawn("notify-volume + 5"), desc="Increase volume"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("notify-volume - 5"), desc="Decrease volume"),
    Key([],"XF86AudioMute", lazy.spawn("notify-volume mute"), desc="Mute volume"),
]

layout_defaults = {
    "margin": 4,
    "border_width": 2,
    "border_focus": gray2,
    "border_normal": bg_alt,
    "single_border_width": 0,
}


groups = [
    Group(
        "1",
        label="󰇧"
    ),
    Group(
        "2",
        label="󰞷"
    ),
    Group(
        "3",
        label="󰓓",
        matches=[Match(wm_class='steam')],
        layouts=[layout.MonadTall(ratio=0.8, **layout_defaults), layout.Floating(**layout_defaults)],
    ),
    Group(
        "4",
        label="󰊠",
        matches=[Match(wm_class=re.compile(r'steam_app*'))],
        layout="floating",
    ),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Layouts
layouts = [
    #layout.Bsp(**layout_defaults),
    layout.MonadTall(change_ratio=0.02, **layout_defaults),
    layout.MonadWide(change_ratio=0.02, ratio=0.7, **layout_defaults),
    layout.Floating(**layout_defaults),
]

# Widget defaults
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    foreground=fg,
    background=gray2,
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()

# Widget decorations
rect = {
    "decorations": [
        RectDecoration(radius=12, filled=True, padding_y=4, padding_x=4, group=False, use_widget_background=True)
    ],
    "padding": 14,
}

pl = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", padding_y=0, use_widget_background=True)
    ]
}

rect_g = {
    "decorations": [
        RectDecoration(radius=12, filled=True, padding_y=4, padding_x=4, group=True, use_widget_background=True)
    ],
    "padding": 5,
}

rect_systray = {
    "decorations": [
        RectDecoration(radius=12, filled=True, padding_y=4, padding_x=4, group=True, use_widget_background=True)
    ],
    "padding": 12,
}

# Widgets
rofi_power_menu = 'rofi -show power-menu -modi "power-menu:rofi-power-menu --choices=shutdown/reboot/suspend/logout" -theme-str " listview { lines: 4; scrollbar: false; } * { accent: @red; } window { location: northwest; width: 250px; y-offset: 44px; x-offset: 4px; children : [ listview ]; }"'
mdi = 'Material Design Icons Desktop'
systray = widget.Systray(**rect_systray)

screens = [
    Screen(
       top=bar.Bar(
            [
                # Left
                widget.Image(filename="~/.config/qtile/arch.svg", mask=True, margin=4, padding=8, adjust_x=4, colour=black, background=red, mouse_callbacks={"Button1":lazy.spawn(rofi_power_menu)}, **pl),
                widget.Spacer(length=10, background=bg),
                widget.Memory(format='󰍛{MemUsed: .1f}{mm}', measure_mem='G', **rect),
                widget.CPU(format=' CPU {load_percent}%', **rect_g),
                widget.ThermalSensor(format='󰔏 {temp:.0f}{unit} ', threshold=85, foreground_alert=red, **rect_g),
                widget.NvidiaSensors(format='GPU 󰔏 {temp}°C', threshold=75, foreground=widget_defaults['foreground'], foreground_alert=red, **rect),
                widget.DF(format='󰄫 {uf}|{r:.0f}%', warn_color=red, **rect),
                widget.WiFiIcon(interface='wlo1', padding_y=10, active_colour=fg, **rect),
                #widget.IWD(show_image=True, interface='wlo1', padding_y=10, active_colour=fg, **rect),
                
                widget.Spacer(background=bg),
                # Center
                widget.GroupBox(disable_drag=True, font=mdi, fontsize=20, background=bg, highlight_method='line', highlight_color=bg, inactive=gray1, active=fg, this_current_screen_border=magenta, urgent_alert_method='text', urgent_text=red),
                widget.Spacer(background=bg),

                # Right
                widget.CurrentLayout(background=bg),
                widget.WidgetBox(widgets=[systray], close_button_location='right', font=mdi, fontsize=24 ,text_closed='󰍞', text_open='󰍟', **rect_g),
                widget.PulseVolume(step=5, limit_max_volume=True, font=mdi, fontsize=18, emoji_list=["󰸈", "󰕿", "󰖀", "󰕾"], emoji=True, **rect),
                widget.Battery(format='{char} {percent:2.0%}', full_char='󰁹', charge_char='󰂄', discharge_char='󱟞', empty_char='󰂃', not_charging_char='󰚥', low_foreground=red, low_percentage=0.2, notify_below=0.2, show_short_text=False, **rect),
                widget.Clock(format="󰸗 %d %b, %Y 󰥔 %H:%M", mouse_callbacks={"Button1": lazy.spawn("show_cal")}, **rect),
            ],
            36,
            background=bg,
            border_width=[0, 0, 0, 0],  # Draw borders
            margin=[4,4,0,4],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1",lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
focus_on_window_activation = 'never'
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=2,
    border_focus=gray2,
    border_normal=bg_alt,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

