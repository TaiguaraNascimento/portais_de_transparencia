

import re


texto = "<html><body></body></html>"

print(re.findall('^<?body>$', texto))
