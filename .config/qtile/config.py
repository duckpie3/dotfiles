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

from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.popup.toolkit import (
    PopupGridLayout,
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
from colors import tomorrow_night as tn
import subprocess

result = subprocess.run(['cat', '~/sysinfo.txt'], stdout=subprocess.PIPE)


def show_popup(qtile):

    controls = [
        PopupImage(
            filename="~/Pictures/jiji.png",
            #pos_x=0,
            #pos_y=0,
            width=1,
            height=1,
            col = 0,
        ),

        PopupText(
            text = result.stdout,
            col = 1,
            h_align = 'center',
            font = 'Mononoki Nerd Font',
            fontsize = 15,
        )
    ]

    layout = PopupGridLayout(
        qtile,
        width=400,
        height=400,
        rows = 2,
        cols= 2,
        margin=10,
        controls=controls,
        background=tn['background'],
        initial_focus=None,
    )

    layout.show(centered=False)



mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Put the focused window to/from floating mode"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Put the focused window to/from fullscreen"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Open rofi app menu"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("brillo -q -u 150000 -A 5"), desc="Increase screen brightness"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brillo -q -u 150000 -U 5"), desc="Decrease screen brightness"),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 5%+"), desc="Increase volume"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("wpctl set-volume -l 0.0 @DEFAULT_AUDIO_SINK@ 5%-"), desc="Decrease volume"),
    Key([],"XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), desc="Mute volume"),
]


groups = [
    Group(
        "1",
        label="󰞷"
    ),
    Group(
        "2",
        label="󰓓"
    ),
    Group(
        "3",
        label="󰇧",
    ),
    Group(
        "4",
        label="󰉋",
    ),
    Group(
        "5",
        label="󰋑",
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

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=0, margin=6),
    layout.Spiral(main_pane="left", clockwise=True, new_client_position='bottom', border_width=0, margin=6),
    layout.Max(),
    layout.Floating(border_width=0),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Mononoki Nerd Font",
    foreground=tn["foreground"],
    fontsize=15,
    padding=6,
)
extension_defaults = widget_defaults.copy()

rofi_power_menu = 'rofi -show power-menu -modi power-menu:rofi-power-menu -theme-str "entry { enabled: false; } listview { lines: 6; scrollbar: false; } * { accent: @red; } window { location: northwest; width: 250px; }"'

powerline = {
    "decorations": [
        PowerLineDecoration(path='forward_slash')
    ]
}

powerline_b = {
    "decorations": [
        PowerLineDecoration(path='back_slash')
    ]
}

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.Image(filename='~/.local/share/icons/arch.png', mouse_callbacks={"Button1":lazy.spawn(rofi_power_menu)}, **powerline, background='#ffffff'),
                #widget.TextBox(" 󰣇", fontsize=28, padding=10, font='Material Design Icons Desktop', **powerline, foreground=tn["background"], background=tn["alert"], mouse_callbacks={"Button1":lazy.function(show_popup)}),
                widget.TextBox(" 󰣇", fontsize=28, padding=10, font='Material Design Icons Desktop', **powerline, foreground=tn["background"], background=tn["alert"], mouse_callbacks={"Button1":lazy.spawn(rofi_power_menu)}),
                widget.GroupBox(disable_drag=True, fontsize=20, highlight_method='line', highlight_color=tn["15"], inactive=tn["background"], active=tn['foreground'],this_current_screen_border=tn["8"], padding_x=4, font='Material Design Icons Desktop', **powerline, background=tn["15"]),
                #widget.Wlan(interface='wlo1', format='{essid} {percent:2.0%}'),
                widget.Memory(format='󰍛{MemUsed: .1f}{mm}', measure_mem='G', **powerline, background=tn["14"],),
                widget.CPU(format='CPU {load_percent}%', background=tn["13"]),
                widget.ThermalSensor(format='󰔏 {temp:.0f}{unit}', **powerline, background=tn["13"]),
                widget.NvidiaSensors(format='GPU 󰔏 {temp}°C', **powerline, background=tn["12"]),
                #widget.TaskList(),
                widget.Spacer(**powerline_b, background=tn["background"]),
                #widget.CurrentLayoutIcon(scale=0.6, foreground='#ffffff', **powerline_b),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(**powerline_b, background=tn['12']),
                widget.PulseVolume(step=5, limit_max_volume=True, fmt='󰕾 {}', **powerline_b, background=tn['13']),
                widget.Battery(format='{char} {percent:2.0%}', charge_char='󰂄', discharge_char='󱟞', empty_char='󰂃', low_foreground=tn['alert'], **powerline_b, background=tn['14']),
                widget.Clock(format="󰸗 %d %b, %Y 󰥔 %H:%M %p ", background=tn['15']),
                #widget.QuickExit(),
            ],
            32,
            border_width=[0, 0, 0, 0],  # Draw borders
            background=tn["background"],
            margin=[6, 6, 0, 6],
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
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
focus_on_window_activation = "smart"
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
