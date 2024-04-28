import pydf
#import os

# Verificar se um arquivo se um arquivo existe
# print(os.path.exists('texto.py'))
# print(os.path.exists('Manipulação de Arquivos/teste.txt'))

# Verificar se um arquivo se um diretorio existe
# print(os.path.exists('python'))
# print(os.path.exists('Manipulação de Arquivos/nova_pasta'))

# Exemplos de caminhos

# print(os.path.exists('Manipulação de Arquivos/nova_pasta/texto.py'))

# Criando arquivos
# os.mknod('python.py')

# Criando um diretorio
# os.mkdir("python")

# os.mknod("Bernardo/Manipulação de Arquivos/nova_pasta/python")
# O diretorio acima foi feito apenas como expemplo, utilize seus próprio diretorio

# Apagando arquivos
# os.remove('texto.py')

# Apagando diretorios - não consegue remover um diretorio se tiver arquivos dentro
# os.rmdir('nova_pasta') - Lembrar de colocar o caminho de onde a pasta está localizada

# Utilizando os.rename()
"""os.mknod("bernardo.py")
os.makedirs("pasta_nova")
os.mknod("./pasta_nova/teste.txt")"""

# os.rename("texto.py", "bernardo.psd")
# os.rename("nova_pasta", "documentos") - renomeando o diretorio


pdf = pydf.generate_pdf('<h1>this is html</h1>')

with open('bernardo.pdf', 'wb') as f:
    f.write(pdf)
