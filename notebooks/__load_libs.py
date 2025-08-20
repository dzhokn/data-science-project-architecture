import sys
import os

def add_parent_dir_to_sys_path():
    """
    This method adds the parent directory to the `sys.path`. It is needed in Jupyter notebooks in order to import modules from `src` directory.

    NB: Keep in minde you have to execute this function before importing any local libraries.

    Example:
    ```
    import __load_libs
    from src.df_io import from_csv, to_csv
    ```
    """
    module_path = os.path.abspath(os.path.join('..'))
    if module_path not in sys.path:
        # Simply adds the parent directory to the sys.path. This way we can import modules from `src` directory.
        sys.path.append(module_path)

add_parent_dir_to_sys_path()