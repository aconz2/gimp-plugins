# GIMP Plugins

## Installation

The `.py` files go in the plug-ins folder, which you can view in `Edit>Preferences>Folders>Plug-ins`.

If you're on Linux you might do something like

```bash
ln -s $(readlink -f export_path_selections.py) ~/.config/GIMP/2.10/plug-ins/
```

The files must be executable for GIMP to pick them up.

## `export_path_selections.py`

Exports each path to a separate PNG file with naming template `{image_name}-{path_name}.png`.

For non-rectangular paths, the outside bits will be all alpha.

This is the same operation as if you did `Path to Selection`, `Copy`, `Paste as new image`, `Export`.
