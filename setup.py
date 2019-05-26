from distutils.core import setup
import py2exe, glob, os

origIsSystemDLL = py2exe.build_exe.isSystemDLL 
def isSystemDLL(pathname):
   
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
            return 0
    return origIsSystemDLL(pathname) 

py2exe.build_exe.isSystemDLL = isSystemDLL 
opts = {
    "py2exe": {
        'includes':['board',
                   'config',
                   'evaluator',
                   'minimax',
                   'player',
                   'ui'],
    }
}

setup (
    windows=['othello.pyw'],
    options=opts,
    data_files = [
        ("res", glob.glob("res\\*.bmp"))
    ],
)
