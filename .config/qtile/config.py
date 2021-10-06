#    ____  __  _ __
#   / __ \/ /_(_) /__
#  / / / / __/ / / _ \
# / /_/ / /_/ / /  __/
# \___\_\__/_/_/\___/
#
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from colors import Colors

import subprocess
import os


@hook.subscribe.startup
def start():
    home = os.path.join(os.path.expanduser('~'), "autostart.sh")
    subprocess.call([home])


mod = "mod4"
terminal = "kitty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize Windows
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle floating
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Shutdown/Restart Qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Spawn prompt
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Rofi apps launcher
    Key([mod], "o", lazy.spawn('rofi -show drun')),

    # Volume controls
    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume 0 +5%')),
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume 0 -5%')),

    # Media controls
    Key([mod], "Left", lazy.spawn('playerctl previous')),
    Key([mod], "Right", lazy.spawn('playerctl next')),
    Key([mod], "p", lazy.spawn('playerctl --player=spotify play-pause')),

    # Emoji Rofi launcher
    Key([mod], "period", lazy.spawn('rofi -show emoji -modi emoji')),
    #     Key([], 'XF86MonBrightnessUp',   lazy.spawn('rofi -show drun')),
    # Key([], 'XF86MonBrightnessDown', lazy.function(backlight('dec'))),
]


groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            # label=group_labels[i],
        ))

for i in groups:
    keys.extend([

        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        Key([mod, "shift"], i.name, lazy.window.togroup(
            i.name), lazy.group[i.name].toscreen()),
    ])

palette = Colors()

layouts = [
    layout.Columns(border_focus="B2BEB5",
                   border_normal="B2BEB5",
                   border_width=0,
                   margin=[10, 10, 10, 10],
                   font="Fira Code",
                   fontsize=10,
                   )
]

widget_defaults = dict(
    font='Fira Code',
    fontsize=11,
    padding=7,
)
extension_defaults = widget_defaults.copy()
# Separator Widget
separator = widget.Sep(foreground=palette.DARK)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=12,
                    padding_x=5,
                    borderwidth=0,
                    active=palette.WHITE,
                    inactive=palette.WHITE,
                    rounded=True,
                    font="Fira Code",
                    highlight_method="block",
                    highlight_color=palette.DARK,
                    block_highlight_text_color=palette.WHITE,
                    this_current_screen_border=palette.SECONDARY,
                    foreground=palette.DARK,
                    background=palette.DARK,
                    hide_unused=True
                ),
                widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(
                    fontsize=10,
                    font="Fira Code",
                    format='{name}'
                ),
                widget.Spacer(),
                separator,
                widget.Systray(),
                widget.Clock(format='%a %I:%M %p',
                             padding=10,),
            ],
            20,
            margin=[10, 10, 0, 10],
            background=palette.DARK,
            opacity=1,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,

    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='zoom'),  # Zoom selector
    Match(wm_class='coreshot'),  # gitk
    Match(title='coreshot'),  # gitk
    Match(title='Screenshot'),  # screenshor
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='Emoji Selector'),  # Emoji selector
    Match(title='Zoom'),  # Emoji selector

],
    border_width=0,
)
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
