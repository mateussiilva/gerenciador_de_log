from bs4 import BeautifulSoup


with open("jet.html", 'r') as arquivo:
    conteudo = arquivo.read()

# Criar o objeto BeautifulSoup
soup = BeautifulSoup(conteudo, 'html.parser')

# Remover scripts
for script in soup(['script', 'style']):
    script.extract()

# Obter o texto limpo
texto_limpo = soup.get_text
