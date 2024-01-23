"""
Generates map resources for server to output path set below.
"""

from common.export import export
from common.utils import misc
import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

def process():
    output_path = script_directory + "/output"

    # Load manifest
    manifest = export.Manifest()
    manifest.import_manifest(misc.load_hjson_file(f"{script_directory}/common/export/profiles/base.hjson"))
    manifest.import_manifest(misc.load_hjson_file(f"{script_directory}/common/export/profiles/efmaps.hjson"))
    manifest.import_manifest(misc.load_hjson_file(f"{script_directory}/common/export/profiles/mod_resources.hjson"))

    # Additional directories to look for resources with hash as filename
    local_dirs = []

    export.run_export(manifest, output_path, local_dirs)

process()
