import sys

import os

INTERP = os.path.expanduser("/var/www/u1172195/data/flaskenv/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from hello import application
from werkzeug.debug import DebuggedApplication 
application = DebuggedApplication(application, evalex=True)
application.debug=True


