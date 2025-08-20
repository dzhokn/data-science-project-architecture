import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    # Simply adds the parent directory to the sys.path. This way we can import modules from `src` directory.
    sys.path.append(module_path)