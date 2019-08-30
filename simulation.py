from gprMax.gprMax import api

import glob

for files in glob.glob("Documents/*.txt"):
    api(files, n=60, geometry_only=False)
