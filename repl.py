import sys
import re

from src import hacker_rank as hr , mianshi as ms , miscellaneous as misc, search as sr, sort

print("\nSOURCE MODULES: \n")
for mod in dir(sys.modules[__name__]):
    if (
        re.search("__\w", mod) is None and
        re.search("^(help|sys|re)$", mod) is None
    ):
        print(mod)

