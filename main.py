

import re


texto = """
</TD>

</TR>

<TR>

<TH align=left> &nbsp; &nbsp;Porta:

</TH>

<TD class="td1" align=left> &nbsp; &nbsp;TCP/IP&nbsp; &nbsp;

</TD>
"""
PATTERN_HTML = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
REGEX = re.compile(PATTERN_HTML)
texto_limpo = re.sub(REGEX,"",texto)
print(texto_limpo)

