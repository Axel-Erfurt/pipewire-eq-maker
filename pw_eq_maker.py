#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### made by Axel Schneider 2024
### https://github.com/Axel-Erfurt
### using Parametric-Eq-generator-for-pipewire by demonich
### https://github.com/demonich/Parametric-Eq-generator-for-pipewire

"""
a file named sink-eq10.conf will be created in the script folder
Copy the file 'sink-eq10.conf' to the folder ~/.config/pipewire/pipewire.conf.d
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        Gtk.Window.__init__(self, application=application)
        self.connect("destroy", Gtk.ApplicationWindow.close)
        self.set_title("Application")
        #self.set_default_size(680, 420)
        
        self.value_list = []
        for i in range(1, 12):
            self.value_list.append("0.0")

        grid = Gtk.Grid(row_spacing = 30, column_spacing = 30, 
                        hexpand = True, margin_left = 20, 
                        margin_right = 20)
        self.add(grid)

        menubutton = Gtk.MenuButton()

        menumodel = Gio.Menu()
        menubutton.set_menu_model(menumodel)
        menumodel.append("Save EQ", "app.Save")
        menumodel.append("Quit", "app.Quit")
        
        self.headerbar = Gtk.HeaderBar()
        self.headerbar.set_show_close_button(True)
        self.headerbar.add(menubutton)
        self.headerbar.set_title("EQ Maker")
        self.headerbar.set_subtitle("for pipewire")
        self.set_titlebar(self.headerbar)
        
        self.hz_list = ["32Hz", "63Hz", "125Hz", "250Hz", "500Hz", "1kHz", "2kHz", "4kHz", "8kHz", "16kHz", "Boost"]
        
        for i in range(1, 12):
            sld = Gtk.Scale.new_with_range(1, -12.0, 12.0, 0.1)
            sld.set_inverted(True)
            sld.set_value(0)
            sld.set_name(f"sld_{i}")
            sld.connect("value-changed", self.val_changed, i)
            grid.attach(sld, i, 1, 1, 10)
            lbl = Gtk.Label(label=self.hz_list[i - 1])
            lbl.set_name((f"lbl_{i}"))
            grid.attach(lbl, i, 11, 1, 1)
        
        self.lbl = Gtk.Label(label = "Info", justify = 2)
        grid.attach(self.lbl, 1, 12, 11, 1)
        
        self.out_text = """Preamp: -6 dB
Filter 1: ON LSC Fc 32 Hz Gain val_1 dB Q 0.70
Filter 2: ON PK Fc 63 Hz Gain val_2 dB Q 0.50
Filter 3: ON PK Fc 125 Hz Gain val_3 dB Q 2.04
Filter 4: ON PK Fc 250 Hz Gain val_4 dB Q 0.87
Filter 5: ON PK Fc 500 Hz Gain val_5 dB Q 1.83
Filter 6: ON PK Fc 1000 Hz Gain val_6 dB Q 1.02
Filter 7: ON PK Fc 2000 Hz Gain val_7 dB Q 3.94
Filter 8: ON PK Fc 4000 Hz Gain val_8 dB Q 3.02
Filter 9: ON PK Fc 8000 Hz Gain val_9 dB Q 2.24
Filter 10: ON HSC Fc 16000 Hz Gain val_10 dB Q 0.70"""
        
    def val_changed(self, wdg, i, *args):
        v = wdg.get_value()
        name = wdg.get_name()
        #print(f"{name} value: {v}")
        self.lbl.set_text(f"{self.hz_list[i-1]}: {v}db")
        self.value_list[i - 1] = f"{v}"
        
    def open_message_window(self, message, *args):
        dialog = Gtk.MessageDialog(
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=message)
        dialog.run()

        dialog.destroy()
        
class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        self.window = ApplicationWindow(self)
        self.window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        
        save_action = Gio.SimpleAction.new("Save", None)
        save_action.connect("activate", self.save_callback)
        self.add_action(save_action)

        quit_action = Gio.SimpleAction.new("Quit", None)
        quit_action.connect("activate", self.quit_callback)
        self.add_action(quit_action)

    def save_callback(self, action, parameter):
        self.window.out_text = self.window.out_text.replace("val_1", self.window.value_list[0]) \
                            .replace("val_2", self.window.value_list[1]) \
                            .replace("val_3", self.window.value_list[2]) \
                            .replace("val_4", self.window.value_list[3]) \
                            .replace("val_5", self.window.value_list[4]) \
                            .replace("val_6", self.window.value_list[5]) \
                            .replace("val_7", self.window.value_list[6]) \
                            .replace("val_8", self.window.value_list[7]) \
                            .replace("val_9", self.window.value_list[8]) \
                            .replace("val_10", self.window.value_list[9])
        with open("sink-eq10.txt", "w") as f:
            f.write(self.window.out_text)
            
        txt_file = "sink-eq10.txt"
        
        output_string = ""

        # Commentary
        output_string += ("\
        # sink-eq10.conf \n\
        # \n\
        # 10 band (or any band, originally, it's 6 band) sink equalizer \n\
        # \n\
        # Copy this file into a conf.d/ directory such as \n\
        #   ~/.config/pipewire/pipewire.conf.d/ \n\
        # \n\
        # Edit it for your needs and then restart pipewire service \n\
        #   systemctl --user restart pipewire.service \n\
        # \n\n")

        output_file = open("sink-eq10.conf", "a+")

        # Beginning of conf
        output_string += ('\
        context.modules = [ \n\
            { name = libpipewire-module-filter-chain \n\
                args = { \n\
                    node.description = "Pipewire Equalizer" \n\
                    media.name       = "Pipewire Equalizer" \n\
                    filter.graph = { \n\
                        nodes = [ \n')

        with open(txt_file, "r") as input_file:
            # read first string, useless for now
            string = input_file.readline().strip()

            # LOWSHELF
            output_string += ('\
                            { \n\
                                type  = builtin \n\
                                name  = eq_band_1 \n\
                                label = bq_lowshelf \n')
            # read second string for 'lowshelf'
            string = input_file.readline().strip() # strip is to prevent \n at the end of the line
            output_string += ('\
                                control = { "Freq" = ' + string.split(" ")[5] + ' "Q" = ' + string.split(" ")[11] + ' "Gain" = ' + string.split(" ")[8] + ' }\n\
                            }')

            # PEAKS
            peaks = 8
            # read and write parameters for 'peaks'
            for i in range(peaks):
                string = input_file.readline().strip()
                output_string += ('\n\
                            { \n\
                                type  = builtin \n\
                                name  = eq_band_' + str(i+2) + '\n\
                                label = bq_peaking \n\
                                control = { "Freq" = ' + string.split(" ")[5] + ' "Q" = ' + string.split(" ")[11] + ' "Gain" = ' + string.split(" ")[8] + ' }\n\
                            }')

            # HIGHSHELF
            output_string += ('\n\
                            { \n\
                                type  = builtin \n\
                                name  = eq_band_10 \n\
                                label = bq_highshelf \n')
            # read 10th string for 'highshelf'
            string = input_file.readline().strip() # strip is to prevent \n at the end of the line
            output_string += ('\
                                control = { "Freq" = ' + string.split(" ")[5] + ' "Q" = ' + string.split(" ")[11] + ' "Gain" = ' + string.split(" ")[8] + ' }\n\
                            }')

        output_string += ('\n\
                                               {\n\
                                type  = builtin\n\
                                name  = m_gain\n\
                                label = bq_highshelf\n\
                                control = { "Freq" = 0.0 "Q" = 1.0 "Gain" = my_gain }\n\
                                } \n\
                        ] \n\
                        links = [ \n\
                            { output = "eq_band_1:Out" input = "eq_band_2:In" } \n\
                            { output = "eq_band_2:Out" input = "eq_band_3:In" } \n\
                            { output = "eq_band_3:Out" input = "eq_band_4:In" } \n\
                            { output = "eq_band_4:Out" input = "eq_band_5:In" } \n\
                            { output = "eq_band_5:Out" input = "eq_band_6:In" } \n\
                            { output = "eq_band_6:Out" input = "eq_band_7:In" } \n\
                            { output = "eq_band_7:Out" input = "eq_band_8:In" } \n\
                            { output = "eq_band_8:Out" input = "eq_band_9:In" } \n\
                            { output = "eq_band_9:Out" input = "eq_band_10:In" } \n\
                            { output = "eq_band_10:Out" input = "m_gain:In" } \n\
                        ] \n\
                    } \n\
                audio.channels = 2 \n\
                audio.position = [ FL FR ] \n\
                    capture.props = { \n\
                        node.name   = "effect_input.eq10" \n\
                        media.class = Audio/Sink \n\
                    } \n\
                    playback.props = { \n\
                        node.name   = "effect_output.eq10" \n\
                        node.passive = true \n\
                    } \n\
                } \n\
            } \n\
        ]')

        output_string = output_string.replace("my_gain", self.window.value_list[10])
        
        with open("sink-eq10.conf", "w") as f:
            f.write(output_string)
            
        self.window.open_message_window("sink-eq10.conf saved in the script folder\n\nCopy the file 'sink-eq10.conf' to \n~/.config/pipewire/pipewire.conf.d")
        
    def quit_callback(self, action, parameter):
        self.quit()

application = Application()
exit_status = application.run(sys.argv)
sys.exit(exit_status)