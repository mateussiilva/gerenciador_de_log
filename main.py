

import re

regex = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
PATTERN_HTML = re.compile(regex)

