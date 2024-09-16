#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        self.set_default_size(600, 500)
        
        self.import_text = ""
        self.out_text = """Preamp: -6 dB
Filter 1: ON LSC Fc freq_1 Hz Gain val_1 dB Q q_factor_1
Filter 2: ON PK Fc freq_2 Hz Gain val_2 dB Q q_factor_2
Filter 3: ON PK Fc freq_3 Hz Gain val_3 dB Q q_factor_3
Filter 4: ON PK Fc freq_4 Hz Gain val_4 dB Q q_factor_4
Filter 5: ON PK Fc freq_5 Hz Gain val_5 dB Q q_factor_5
Filter 6: ON PK Fc freq_6 Hz Gain val_6 dB Q q_factor_6
Filter 7: ON PK Fc freq_7 Hz Gain val_7 dB Q q_factor_7
Filter 8: ON PK Fc freq_8 Hz Gain val_8 dB Q q_factor_8
Filter 9: ON PK Fc freq_9 Hz Gain val_9 dB Q q_factor_9
Filter 10: ON HSC Fc freq_last Hz Gain val_last dB Q q_factor_last"""
        
        self.q_list = ["0.7", "0.5", "2.0", "1.0", "1.0", "2.0", "2.0", "2.0", "1.0", "0.7"]
        self.g_list = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"]
        self.f_list = ["32", "63", "125", "250", "500", "1000", "2000", "4000", "8000", "16000"]

        self.lbl = Gtk.Label(label = "Info", justify = 2, hexpand = True, vexpand = False)
        vbox = Gtk.VBox()
        vbox.set_homogeneous(False)
        self.add(vbox)
        
        hbox_q = Gtk.HBox(hexpand = False, vexpand = False, homogeneous = True)
        hbox_g = Gtk.HBox(hexpand = False, vexpand = True, homogeneous = True)
        hbox_f = Gtk.HBox(hexpand = False, vexpand = False, homogeneous = True)
        
        vbox.pack_start(hbox_q, False, False, 4)
        vbox.add(hbox_g)
        vbox.pack_start(hbox_f, False, False, 4)
        
        self.q_slider_0 = self.make_q_btn()
        self.q_slider_0.set_value(float(self.q_list[0]))
        self.q_slider_0.set_label(self.q_list[0])
        self.q_slider_1 = self.make_q_btn()
        self.q_slider_1.set_value(float(self.q_list[1]))
        self.q_slider_1.set_label(self.q_list[1])
        self.q_slider_2 = self.make_q_btn()
        self.q_slider_2.set_value(float(self.q_list[2]))
        self.q_slider_2.set_label(self.q_list[2])
        self.q_slider_3 = self.make_q_btn()
        self.q_slider_3.set_value(float(self.q_list[3]))
        self.q_slider_3.set_label(self.q_list[3])
        self.q_slider_4 = self.make_q_btn()
        self.q_slider_4.set_value(float(self.q_list[4]))
        self.q_slider_4.set_label(self.q_list[4])
        self.q_slider_5 = self.make_q_btn()
        self.q_slider_5.set_value(float(self.q_list[5]))
        self.q_slider_2.set_label(self.q_list[5])
        self.q_slider_6 = self.make_q_btn()
        self.q_slider_6.set_value(float(self.q_list[6]))
        self.q_slider_6.set_label(self.q_list[6])
        self.q_slider_7 = self.make_q_btn()
        self.q_slider_7.set_value(float(self.q_list[7]))
        self.q_slider_7.set_label(self.q_list[7])
        self.q_slider_8 = self.make_q_btn()
        self.q_slider_8.set_value(float(self.q_list[8]))
        self.q_slider_8.set_label(self.q_list[8])
        self.q_slider_9 = self.make_q_btn()
        self.q_slider_9.set_value(float(self.q_list[9]))
        self.q_slider_9.set_label(self.q_list[9])
        self.q_slider_0.connect("value-changed", self.update_q_list)
        self.q_slider_1.connect("value-changed", self.update_q_list)
        self.q_slider_2.connect("value-changed", self.update_q_list)
        self.q_slider_3.connect("value-changed", self.update_q_list)
        self.q_slider_4.connect("value-changed", self.update_q_list)
        self.q_slider_5.connect("value-changed", self.update_q_list)
        self.q_slider_6.connect("value-changed", self.update_q_list)
        self.q_slider_7.connect("value-changed", self.update_q_list)
        self.q_slider_8.connect("value-changed", self.update_q_list)
        self.q_slider_9.connect("value-changed", self.update_q_list)
        
        hbox_q.add(self.q_slider_0)
        hbox_q.add(self.q_slider_1)
        hbox_q.add(self.q_slider_2)
        hbox_q.add(self.q_slider_3)
        hbox_q.add(self.q_slider_4)
        hbox_q.add(self.q_slider_5)
        hbox_q.add(self.q_slider_6)
        hbox_q.add(self.q_slider_7)
        hbox_q.add(self.q_slider_8)
        hbox_q.add(self.q_slider_9)
        hbox_q.add(Gtk.Label(label="Boost"))
        
        self.g_slider_0 = self.make_g_btn()
        self.g_slider_1 = self.make_g_btn()
        self.g_slider_2 = self.make_g_btn()
        self.g_slider_3 = self.make_g_btn()
        self.g_slider_4 = self.make_g_btn()
        self.g_slider_5 = self.make_g_btn()
        self.g_slider_6 = self.make_g_btn()
        self.g_slider_7 = self.make_g_btn()
        self.g_slider_8 = self.make_g_btn()
        self.g_slider_9 = self.make_g_btn()
        self.g_slider_10 = self.make_g_btn()
        self.g_slider_0.connect("value-changed", self.update_g_list)
        self.g_slider_1.connect("value-changed", self.update_g_list)
        self.g_slider_2.connect("value-changed", self.update_g_list)
        self.g_slider_3.connect("value-changed", self.update_g_list)
        self.g_slider_4.connect("value-changed", self.update_g_list)
        self.g_slider_5.connect("value-changed", self.update_g_list)
        self.g_slider_6.connect("value-changed", self.update_g_list)
        self.g_slider_7.connect("value-changed", self.update_g_list)
        self.g_slider_8.connect("value-changed", self.update_g_list)
        self.g_slider_9.connect("value-changed", self.update_g_list)
        self.g_slider_10.connect("value-changed", self.update_g_list)
        
        hbox_g.add(self.g_slider_0)
        hbox_g.add(self.g_slider_1)
        hbox_g.add(self.g_slider_2)
        hbox_g.add(self.g_slider_3)
        hbox_g.add(self.g_slider_4)
        hbox_g.add(self.g_slider_5)
        hbox_g.add(self.g_slider_6)
        hbox_g.add(self.g_slider_7)
        hbox_g.add(self.g_slider_8)
        hbox_g.add(self.g_slider_9)
        hbox_g.add(self.g_slider_10)
        
        self.f_slider_0 = self.make_f_btn()
        self.f_slider_0.get_adjustment().configure (int(self.f_list[0]), 20, 20000, 1, 1, 1)
        self.f_slider_0.set_label(self.f_list[0])
        self.f_slider_1 = self.make_f_btn()
        self.f_slider_1.get_adjustment().configure (int(self.f_list[1]), 20, 20000, 1, 1, 1)
        self.f_slider_1.set_label(self.f_list[1])
        self.f_slider_2 = self.make_f_btn()
        self.f_slider_2.get_adjustment().configure (int(self.f_list[2]), 20, 20000, 1, 1, 1)
        self.f_slider_2.set_label(self.f_list[2])
        self.f_slider_3 = self.make_f_btn()
        self.f_slider_3.get_adjustment().configure (int(self.f_list[3]), 20, 20000, 1, 1, 1)
        self.f_slider_3.set_label(self.f_list[3])
        self.f_slider_4 = self.make_f_btn()
        self.f_slider_4.get_adjustment().configure (int(self.f_list[4]), 20, 20000, 1, 1, 1)
        self.f_slider_4.set_label(self.f_list[4])
        self.f_slider_5 = self.make_f_btn()
        self.f_slider_5.get_adjustment().configure (int(self.f_list[5]), 20, 20000, 1, 1, 1)
        self.f_slider_5.set_label(self.f_list[5])
        self.f_slider_6 = self.make_f_btn()
        self.f_slider_6.get_adjustment().configure (int(self.f_list[6]), 20, 20000, 1, 1, 1)
        self.f_slider_6.set_label(self.f_list[6])
        self.f_slider_7 = self.make_f_btn()
        self.f_slider_7.get_adjustment().configure (int(self.f_list[7]), 20, 20000, 1, 1, 1)
        self.f_slider_7.set_label(self.f_list[7])
        self.f_slider_8 = self.make_f_btn()
        self.f_slider_8.get_adjustment().configure (int(self.f_list[8]), 20, 20000, 1, 1, 1)
        self.f_slider_8.set_label(self.f_list[8])
        self.f_slider_9 = self.make_f_btn()
        self.f_slider_9.get_adjustment().configure (int(self.f_list[9]), 20, 20000, 1, 1, 1)
        self.f_slider_9.set_label(self.f_list[9])
        self.f_slider_0.connect("value-changed", self.update_f_list)
        self.f_slider_1.connect("value-changed", self.update_f_list)
        self.f_slider_2.connect("value-changed", self.update_f_list)
        self.f_slider_3.connect("value-changed", self.update_f_list)
        self.f_slider_4.connect("value-changed", self.update_f_list)
        self.f_slider_5.connect("value-changed", self.update_f_list)
        self.f_slider_6.connect("value-changed", self.update_f_list)
        self.f_slider_7.connect("value-changed", self.update_f_list)
        self.f_slider_8.connect("value-changed", self.update_f_list)
        self.f_slider_9.connect("value-changed", self.update_f_list)
        
        hbox_f.add(self.f_slider_0)
        hbox_f.add(self.f_slider_1)
        hbox_f.add(self.f_slider_2)
        hbox_f.add(self.f_slider_3)
        hbox_f.add(self.f_slider_4)
        hbox_f.add(self.f_slider_5)
        hbox_f.add(self.f_slider_6)
        hbox_f.add(self.f_slider_7)
        hbox_f.add(self.f_slider_8)
        hbox_f.add(self.f_slider_9)
        hbox_f.add(Gtk.Label(label=""))
        
        
        vbox.pack_start(self.lbl, False, False, 4)

        menubutton = Gtk.MenuButton()

        menumodel = Gio.Menu()
        menubutton.set_menu_model(menumodel)
        menumodel.append("Open AutoEQ", "app.Open")
        menumodel.append("Save", "app.Save")
        menumodel.append("Quit", "app.Quit")
        
        self.headerbar = Gtk.HeaderBar()
        self.headerbar.set_show_close_button(True)
        self.headerbar.add(menubutton)
        self.headerbar.set_title("EQ Maker")
        self.headerbar.set_subtitle("for pipewire")
        self.set_titlebar(self.headerbar)
        
    def update_q_list(self, *args):
        self.q_list[0] = f"{self.q_slider_0.get_value():.1f}"
        self.q_list[1] = f"{self.q_slider_1.get_value():.1f}"
        self.q_list[2] = f"{self.q_slider_2.get_value():.1f}"
        self.q_list[3] = f"{self.q_slider_3.get_value():.1f}"
        self.q_list[4] = f"{self.q_slider_4.get_value():.1f}"
        self.q_list[5] = f"{self.q_slider_5.get_value():.1f}"
        self.q_list[6] = f"{self.q_slider_6.get_value():.1f}"
        self.q_list[7] = f"{self.q_slider_7.get_value():.1f}"
        self.q_list[8] = f"{self.q_slider_8.get_value():.1f}"
        self.q_list[9] = f"{self.q_slider_9.get_value():.1f}"
        
    def update_g_list(self, *args):
        self.g_list[0] = f"{self.g_slider_0.get_value():.1f}"
        self.g_list[1] = f"{self.g_slider_1.get_value():.1f}"
        self.g_list[2] = f"{self.g_slider_2.get_value():.1f}"
        self.g_list[3] = f"{self.g_slider_3.get_value():.1f}"
        self.g_list[4] = f"{self.g_slider_4.get_value():.1f}"
        self.g_list[5] = f"{self.g_slider_5.get_value():.1f}"
        self.g_list[6] = f"{self.g_slider_6.get_value():.1f}"
        self.g_list[7] = f"{self.g_slider_7.get_value():.1f}"
        self.g_list[8] = f"{self.g_slider_8.get_value():.1f}"
        self.g_list[9] = f"{self.g_slider_9.get_value():.1f}"
        self.g_list[10] = f"{self.g_slider_10.get_value():.1f}"

    def update_f_list(self, *args):
        self.f_list[0] = f"{self.f_slider_0.get_value():.0f}"
        self.f_list[1] = f"{self.f_slider_1.get_value():.0f}"
        self.f_list[2] = f"{self.f_slider_2.get_value():.0f}"
        self.f_list[3] = f"{self.f_slider_3.get_value():.0f}"
        self.f_list[4] = f"{self.f_slider_4.get_value():.0f}"
        self.f_list[5] = f"{self.f_slider_5.get_value():.0f}"
        self.f_list[6] = f"{self.f_slider_6.get_value():.0f}"
        self.f_list[7] = f"{self.f_slider_7.get_value():.0f}"
        self.f_list[8] = f"{self.f_slider_8.get_value():.0f}"
        self.f_list[9] = f"{self.f_slider_9.get_value():.0f}"
        
    def make_q_btn(self, *args):
        btn = Gtk.ScaleButton()
        btn.get_adjustment().configure (1.0, 0, 8, 0.1, 0.1, 0.1)
        btn.set_tooltip_markup("<b>Q-Factor</b>")
        btn.set_value(1.0)
        btn.set_label("1.0")
        btn.connect("value-changed", lambda x, y: btn.set_label(f"{btn.get_value():.1f}"))
        btn.connect("value-changed", lambda x, y: self.lbl.set_markup(f"Q-Factor: <b>{btn.get_value():.1f}</b>"))
        return btn
        
    def make_g_btn(self, *args):
        sld = Gtk.Scale.new_with_range(1, -15.0, 15.0, 0.01)
        sld.set_tooltip_markup("<b>Gain</b>")
        sld.set_inverted(True)
        sld.set_value(0)
        return sld 
        
    def make_f_btn(self, *args):
        btn = Gtk.ScaleButton.new(1, 20, 20000, 0.1)
        btn.set_hexpand(True)
        btn.set_tooltip_markup("<b>Frequency</b>")
        btn.connect("value-changed", lambda x, y: btn.set_label(f"{btn.get_value():.0f}"))
        btn.connect("value-changed", lambda x, y: self.lbl.set_markup(f"Frequency: <b>{btn.get_value():.0f}Hz</b>"))
        return btn


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        self.window = ApplicationWindow(self)
        self.window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        new_action = Gio.SimpleAction.new("Save", None)
        new_action.connect("activate", self.save_callback)
        self.add_action(new_action)
        
        open_action = Gio.SimpleAction.new("Open", None)
        open_action.connect("activate", self.open_callback)
        self.add_action(open_action)

        quit_action = Gio.SimpleAction.new("Quit", None)
        quit_action.connect("activate", self.quit_callback)
        self.add_action(quit_action)

    def open_callback(self, action, parameter):        
        self.file_filter_text = Gtk.FileFilter()
        self.file_filter_text.set_name("Text Files")
        self.file_filter_text.add_pattern("*.txt")
        
        self.show_open_dialog()

    def show_open_dialog(self):
        self.dialog = Gtk.FileChooserNative.new("Open", self.window, Gtk.FileChooserAction.OPEN, "Open", "Cancel")
        self.dialog.add_filter(self.file_filter_text)
        self.dialog.set_transient_for(self.window)
        self.dialog.connect("response", self.on_open_dialog_response)
        self.dialog.show()

    def on_open_dialog_response(self, dialog, response_id):
        if response_id == Gtk.ResponseType.ACCEPT:
            filename = str(dialog.get_file().get_path())
            print(f"loading {filename}")
            if filename != "":
                with open(filename, "r") as f:
                    self.window.import_text = f.read()
                    self.fill_sliders()
                    name = filename.split('/')[-1].split(".")[0]
                    self.window.lbl.set_markup(f"AutoEQ File <b>{name}</b> loaded")
                    self.window.headerbar.set_subtitle(f'{name} (from AutoEQ)')
        dialog.destroy()
        
    def fill_sliders(self, *args):
        all_list = self.window.import_text.splitlines()
        self.window.g_slider_10.set_value(float(all_list[0].split(" ")[1].replace("-", "")))
        
        self.window.g_slider_0.set_value(float(all_list[1].split(" ")[8]))
        self.window.g_slider_1.set_value(float(all_list[2].split(" ")[8]))
        self.window.g_slider_2.set_value(float(all_list[3].split(" ")[8]))
        self.window.g_slider_3.set_value(float(all_list[4].split(" ")[8]))
        self.window.g_slider_4.set_value(float(all_list[5].split(" ")[8]))
        self.window.g_slider_5.set_value(float(all_list[6].split(" ")[8]))
        self.window.g_slider_6.set_value(float(all_list[7].split(" ")[8]))
        self.window.g_slider_7.set_value(float(all_list[8].split(" ")[8]))
        self.window.g_slider_8.set_value(float(all_list[9].split(" ")[8]))
        self.window.g_slider_9.set_value(float(all_list[10].split(" ")[8]))

        self.window.q_slider_0.set_value(float(all_list[1].split(" ")[11]))
        self.window.q_slider_1.set_value(float(all_list[2].split(" ")[11]))
        self.window.q_slider_2.set_value(float(all_list[3].split(" ")[11]))
        self.window.q_slider_3.set_value(float(all_list[4].split(" ")[11]))
        self.window.q_slider_4.set_value(float(all_list[5].split(" ")[11]))
        self.window.q_slider_5.set_value(float(all_list[6].split(" ")[11]))
        self.window.q_slider_6.set_value(float(all_list[7].split(" ")[11]))
        self.window.q_slider_7.set_value(float(all_list[8].split(" ")[11]))
        self.window.q_slider_8.set_value(float(all_list[9].split(" ")[11]))
        self.window.q_slider_9.set_value(float(all_list[10].split(" ")[11]))
        
        self.window.f_slider_0.set_value(float(all_list[1].split(" ")[5]))
        self.window.f_slider_1.set_value(float(all_list[2].split(" ")[5]))
        self.window.f_slider_2.set_value(float(all_list[3].split(" ")[5]))
        self.window.f_slider_3.set_value(float(all_list[4].split(" ")[5]))
        self.window.f_slider_4.set_value(float(all_list[5].split(" ")[5]))
        self.window.f_slider_5.set_value(float(all_list[6].split(" ")[5]))
        self.window.f_slider_6.set_value(float(all_list[7].split(" ")[5]))
        self.window.f_slider_7.set_value(float(all_list[8].split(" ")[5]))
        self.window.f_slider_8.set_value(float(all_list[9].split(" ")[5]))
        self.window.f_slider_9.set_value(float(all_list[10].split(" ")[5]))
        
    def quit_callback(self, action, parameter):
        print("You clicked quit, goodbye ...")
        self.quit()
        
    def save_callback(self, action, parameter):
        self.window.update_q_list()
        self.window.update_g_list()
        self.window.update_f_list()
        self.window.out_text = self.window.out_text.replace("val_1", self.window.g_list[0]) \
                            .replace("val_2", self.window.g_list[1]) \
                            .replace("val_3", self.window.g_list[2]) \
                            .replace("val_4", self.window.g_list[3]) \
                            .replace("val_5", self.window.g_list[4]) \
                            .replace("val_6", self.window.g_list[5]) \
                            .replace("val_7", self.window.g_list[6]) \
                            .replace("val_8", self.window.g_list[7]) \
                            .replace("val_9", self.window.g_list[8]) \
                            .replace("val_last", self.window.g_list[9]) \
                            .replace("q_factor_1", self.window.q_list[0]) \
                            .replace("q_factor_2", self.window.q_list[1]) \
                            .replace("q_factor_3", self.window.q_list[2]) \
                            .replace("q_factor_4", self.window.q_list[3]) \
                            .replace("q_factor_5", self.window.q_list[4]) \
                            .replace("q_factor_6", self.window.q_list[5]) \
                            .replace("q_factor_7", self.window.q_list[6]) \
                            .replace("q_factor_8", self.window.q_list[7]) \
                            .replace("q_factor_9", self.window.q_list[8]) \
                            .replace("q_factor_last", self.window.q_list[9]) \
                            .replace("freq_1", self.window.f_list[0]) \
                            .replace("freq_2", self.window.f_list[1]) \
                            .replace("freq_3", self.window.f_list[2]) \
                            .replace("freq_4", self.window.f_list[3]) \
                            .replace("freq_5", self.window.f_list[4]) \
                            .replace("freq_6", self.window.f_list[5]) \
                            .replace("freq_7", self.window.f_list[6]) \
                            .replace("freq_8", self.window.f_list[7]) \
                            .replace("freq_9", self.window.f_list[8]) \
                            .replace("freq_last", self.window.f_list[9])                            
                            
                            
        self.write_eq()
        #print(self.window.q_list)
        #print(self.window.g_list)
        #print(self.window.f_list)
        #print(self.window.out_text)
        
    def write_eq(self, *args):
                            
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

        output_string = output_string.replace("my_gain", self.window.g_list[10])
        
        with open("sink-eq10.conf", "w") as f:
            f.write(output_string)
            
        
        self.window.lbl.set_markup("<b>sink-eq10.conf</b> was saved in the script folder\nCopy the file <b>sink-eq10.conf</b> to the folder <b>~/.config/pipewire/pipewire.conf.d</b>")

application = Application()
exit_status = application.run(sys.argv)
sys.exit(exit_status)