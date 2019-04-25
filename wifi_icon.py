"""
    Simple python script providing a Gtk tray icon indicating wifi signal strength
"""

import os
import configparser
import sys
from subprocess import check_output
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

ICONS = [
    "./icons/baseline_signal_wifi_0_bar_white_18dp.png",
    "./icons/baseline_signal_wifi_1_bar_white_18dp.png",
    "./icons/baseline_signal_wifi_2_bar_white_18dp.png",
    "./icons/baseline_signal_wifi_3_bar_white_18dp.png",
    "./icons/baseline_signal_wifi_4_bar_white_18dp.png"
]

def parse_iw(ifname):
    """
        Parse the result of the `iw` command and return a tuple (ssid, frequency)
    """
    output = check_output(["iw", ifname, "info"]).decode("UTF-8")
    lines = output.split("\n")
    ssid = ""
    freq = ""
    for line in lines:
        if len(line.split("ssid")) > 1:
            ssid = line.split("ssid")[1]
        if len(line.split("channel")) > 1:
            freq = line.split("(")[1].split(")")[0]
    return (ssid, freq)

def update():
    """
        Called by Gtk each second to update the tray icon and tooltip
    """
    with open("/proc/net/wireless", "r") as wireless_file:
        stats = wireless_file.read()
        wireless_file.close()
    ifstatus_lines = stats.split("\n")
    if len(ifstatus_lines) <= 3:
        TRAYICON.set_from_file(ICONS[0])
        TRAYICON.set_tooltip_text("No Wifi")
        return True
    ifstatus = ifstatus_lines[2]
    ifstatus_splited = ifstatus.split(" ")
    ifstatus_splited = list(filter(lambda x: x != '', ifstatus_splited))
    ifname = ifstatus_splited[0][:-1]
    ifstrengh = ifstatus_splited[2][:-1]
    ifstrengh_percent = (float(ifstrengh) / MAXIUM_LEVEL) * 100.0

    ssid, freq = parse_iw(ifname)
    TRAYICON.set_tooltip_text("{} on {} ({}) at {}% ({}/{})"
			                  .format(ifname, ssid, freq, round(ifstrengh_percent, 2),
                                      ifstrengh, MAXIUM_LEVEL))

    icon_id = int(round(ifstrengh_percent/25, 0))
    if icon_id >= 5:
        icon_id = 4
    if icon_id < 0:
        icon_id = 0
    TRAYICON.set_from_file(ICONS[icon_id])
    return True

def config_error():
    """
        Called when config.ini file is missing required entry
    """
    print("Please check your \"config.ini\" file.")
    print("If it is not present, see \"config.ini.sample\".")
    sys.exit(1)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    CONFIG = configparser.ConfigParser()
    CONFIG.read("config.ini")
    if "wifiicon" not in CONFIG:
        config_error()
    elif "MaximumLevel" not in CONFIG["wifiicon"]:
        config_error()
    MAXIUM_LEVEL = float(CONFIG["wifiicon"]["MaximumLevel"])
    TRAYICON = Gtk.StatusIcon()
    TRAYICON.set_from_file(ICONS[0])
    TRAYICON.set_visible(True)
    GObject.timeout_add(1000, update)
    Gtk.main()
