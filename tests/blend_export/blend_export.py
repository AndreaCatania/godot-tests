# blender --background --python .\blend_export.py
import bpy
import posixpath
import shutil
import os

directory = "blend"
export_types = ["gltf", "obj", "fbx"]
for export_type in export_types:
    shutil.rmtree(export_type, ignore_errors=True)
    posixpath.os.mkdir(export_type, mode=0o777)
for filename in os.listdir(directory):
    if filename.endswith(".blend"):
        for export_type in export_types:
            print(filename)
            bpy.ops.wm.open_mainfile(filepath="blend/" + filename)
            strip_file_name = filename.rsplit(".blend", 1)[0]
            if export_type == "gltf":
                bpy.ops.export_scene.gltf(
                    filepath=export_type + "/" + strip_file_name + ".gltf",
                    export_format="GLTF_SEPARATE",
                    export_copyright="The MIT License (MIT) Copyright (c) 2020 Godot Engine",
                )
            elif export_type == "fbx":
                bpy.ops.export_scene.fbx(filepath=export_type + "/" + strip_file_name + "." + export_type)
            elif export_type == "obj":
                bpy.ops.export_scene.obj(filepath=export_type + "/" + strip_file_name + "." + export_type)