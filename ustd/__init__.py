"""
Basic
"""
__version__ = '0.0.0'
__author__ = 'Jon Crall'
__author_email__ = 'erotemic@gmail.com'
__url__ = 'None'

__mkinit__ = """
mkinit /home/joncrall/code/ustd/ustd/__init__.py
"""


"""
The stdx module contains extensions for the Python standard library.

The chosen utilities were distilled from ubelt, which should be seen as a
superset of this project.

This is unrelated to the rust project with the same name, or any transmissible
illness with a similar acronym.
"""
__version__ = '1.0.0'
__author__ = 'Jon Crall'
__author_email__ = 'erotemic@gmail.com'
__url__ = 'github.com/Erotemic/stdx'

__mkinit__ = """
mkinit /home/joncrall/code/stdx/stdx/__init__.py
"""

from .util_cache import Cacher  # direct / stamp API

# from .util_cmd import cmd
from .util_cmd import Command

from .util_dict import AutoDict
from .util_dict import UDict
from .util_dict import UDict as dict

from .util_futures import Executor
from .util_futures import JobPool

from .util_hash import Hasher

from .util_func import Function
from .util_func import Function as Func

from .util_format import urepr
from .util_format import urepr as repr

from .util_import import Module

from .util_indexable import Indexable

from .util_list import UList
from .util_list import USet
from .util_list import UList as list
from .util_list import USet as set

from .util_path import Path

from .util_time import Time, Timer

from .orderedset import OrderedSet
from .orderedset import OrderedSet as oset

from .progiter import ProgIter




"""
Notes:
    ub.Path.trylink  # try some sort of link


    class Module:
        import_module_from_name = import_module_from_name
        import_module_from_path = import_module_from_path
        modname_to_modpath = modname_to_modpath
        modpath_to_modname = modpath_to_modname
        split_modpath = split_modpath

    ub.Path.trylink  # try some sort of link

"""
# from .util_colors import (NO_COLOR, color_text, highlight_code,)
# from .util_const import (NoParam,)
# from .util_dict import (AutoDict, AutoOrderedDict, SetDict, UDict, ddict,
#                         dict_diff, dict_hist, dict_isect, dict_subset,
#                         dict_union, dzip, find_duplicates, group_items,
#                         invert_dict, map_keys, map_vals, map_values,
#                         named_product, odict, sdict, sorted_keys,
#                         sorted_vals, sorted_values, udict, varied_values,)
# from .util_deprecate import (schedule_deprecation,)
# from .util_download import (download, grabdata,)
# from .util_download_manager import (DownloadManager,)
# from .util_func import (compatible, identity, inject_method,)
# from .util_format import (FormatterExtensions, repr2, urepr,)
# from .util_futures import (Executor, JobPool,)
# from .util_io import (delete, touch,)
# from .util_links import (symlink,)
# from .util_list import (allsame, argmax, argmin, argsort, argunique,
                             # boolmask, chunks, compress, flatten, iter_window,
                             # iterable, peek, take, unique, unique_flags,)
# from .util_hash import (hash_data, hash_file,)
# from .util_import import (import_module_from_name,
#                                import_module_from_path, modname_to_modpath,
#                                modpath_to_modname, split_modpath,)
# from .util_indexable import (IndexableWalker, indexable_allclose,)
# from .util_memoize import (memoize, memoize_method, memoize_property,)
# from .util_mixins import (NiceRepr,)
# from .util_path import (Path, TempDir, augpath, ensuredir, expandpath,
#                              shrinkuser, userhome,)
# from .util_platform import (DARWIN, LINUX, POSIX, WIN32, find_exe,
#                                  find_path, platform_cache_dir,
#                                  platform_config_dir, platform_data_dir,)
# from .util_str import (codeblock, hzcat, indent, paragraph,)
# from .util_stream import (CaptureStdout, CaptureStream, TeeStringIO,)
# from .util_time import (Timer, timeparse, timestamp,)
# from .util_zip import (split_archive, zopen,)
# from .orderedset import (OrderedSet, oset,)
# from .progiter import (ProgIter,)

