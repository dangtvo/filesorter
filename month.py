import sys
import datetime
from os import listdir, makedirs, rename
from os.path import isfile, join, getctime, exists
from time import ctime


if len(sys.argv) != 2:
    raise ValueError('Please provide the path to the directory to sort.')

location = sys.argv[1]

unsorted = [f for f in listdir(location) if f != 'sorted']

for file in unsorted:
    path = join(location,file)
    print( 'Processing ' + path)
    created = datetime.datetime.fromtimestamp(getctime(path))
    dirname = created.strftime("%b %Y")
    dirpath = join(location, 'sorted', dirname)

    if not exists( dirpath ) :
        makedirs( dirpath )

    rename( path, join( dirpath, file))



