#!/usr/bin/env python

from __future__ import print_function

import os
import traceback

from gimpfu import *

def export_path_selections(image, directory, name_pattern):

    try:
        if not image.filename:
            image_name = 'img'
        else:
            image_name, _ = os.path.splitext(os.path.basename(image.filename))

        for path in image.vectors:
            filename = name_pattern.format(
                image_name = image_name,
                path_name = path.name,
            )
            pdb.gimp_image_select_item(image, CHANNEL_OP_REPLACE, path)
            pdb.gimp_edit_copy_visible(image)
            sub_image = pdb.gimp_edit_paste_as_new()
            save_path = os.path.join(directory, filename)
            pdb.gimp_file_save(sub_image, sub_image.active_layer, save_path, save_path)
            pdb.gimp_image_delete(sub_image)

    except Exception as e:
        pdb.gimp_message(e.args[0])
        print(traceback.format_exc())

register(
    proc_name  = 'export_path_selectiosn',
    blurb      = 'Export all path selections',
    help       = '',
    author     = 'aconz2',
    copyright  = '',
    date       = '2021',
    menu       = '<Image>/File/Export',
    label      = 'Export path selection',
    imagetypes = '*',
    params     = [
        (PF_IMAGE,      'image',        'Input image', None),
        (PF_DIRNAME,    'directory',    'Directory',   '.'),
        (PF_STRING,     'name_pattern', 'Layer name',  '{image_name}-{path_name}.png'),
    ],
    results    = [],
    function   = export_path_selections,
)

main()
