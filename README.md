wifi_icon
=========

Simple python script that provide a Gtk tray icon indicating the strength of the wifi signal on Linux Kernel based operating system.

Dependencies
------------

| Generic Name      | Void Linux                  | Arch Linux                 | Debian                 |
|-------------------|-----------------------------|----------------------------|------------------------|
| [Python 3][py]    | [python3][pyvoid]           | [python][pyarch]           | [python3][pydeb]       |
| [PyGObject][pygo] | [python3-gobject][pygovoid] | [python-gobject][pygoarch] | [python3-gi][pygodeb]  |
| [Gtk 3][gtk]      | [gtk+3-devel][gtkvoid]      | [gtk3][gtkarch]            | [libgtk-3-dev][gtkdeb] |
| [iw][iw]          | [iw][iwvoid]                | [iw][iwarch]               | [iw][iwdeb]            |

[py]: https://www.python.org/
[pygo]: https://pygobject.readthedocs.io
[gtk]: https://www.gtk.org/
[iw]: https://wireless.wiki.kernel.org/en/users/Documentation/iw

[pyvoid]: https://github.com/void-linux/void-packages/tree/master/srcpkgs/python3
[pygovoid]: https://github.com/void-linux/void-packages/tree/master/srcpkgs/python3-gobject
[gtkvoid]: https://github.com/void-linux/void-packages/tree/master/srcpkgs/gtk+3
[iwvoid]: https://github.com/void-linux/void-packages/tree/master/srcpkgs/iw

[pyarch]: https://www.archlinux.org/packages/extra/x86_64/python/
[pygoarch]: https://www.archlinux.org/packages/extra/x86_64/python-gobject/
[gtkarch]: https://www.archlinux.org/packages/extra/x86_64/gtk3/
[iwarch]: https://www.archlinux.org/packages/core/x86_64/iw/

[pydeb]: https://packages.debian.org/stable/python3
[pygodeb]: https://packages.debian.org/stable/python3-gi
[gtkdeb]: https://packages.debian.org/stable/libgtk-3-dev
[iwdeb]: https://packages.debian.org/stable/iw

Usage
-----

First, edit the file `config.ini.sample` and rename it `config.ini`

Then you can launch the script via
```
python3 wifi_icon.py
```

License
-------

The icons are coming from the [Google Material Icon Library](https://material.io/tools/icons), under the *Apache License Version 2.0* available in `icons/LICENSE`.

The source code is under the *Unlicense* available in `UNLICENSE`.
