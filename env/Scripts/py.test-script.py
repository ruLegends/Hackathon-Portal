#!c:\dev\python\djangoconf\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest==2.6.0','console_scripts','py.test'
__requires__ = 'pytest==2.6.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pytest==2.6.0', 'console_scripts', 'py.test')()
    )
