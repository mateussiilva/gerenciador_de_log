

import re 


p = re.compile(r"||&nbsp;")

texto = '<TD class="td1" align=left> &nbsp; &nbsp;VJ-1604W (ValueJet)&nbsp; &nbsp;'
resultado = re.sub(p,"",texto)
print(resultado)