# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.

# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/

# Ative seu ambiente virtual
# pip install pypdf2b


from pathlib import Path
# PARA TRABALHAR COM CAMINHO. 

from PyPDF2 import PdfReader, PdfWriter, PdfMerger
# PDFReader --> PARA LEITURA DE ARQUIVO PDF. 
# PDFWriter --> PARA ESCRITA DE ARQUIVO PDF.

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240517.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
# IMPORTANTE: AO EXECUTAR O METODO PARA IMAGENS, EXISTE UMA LIMITACAO POR PARTE DO PyPDF.
# imagem0 = page0.images[0]

# print(page0.extract_text()) # EXTRAINDO O TEXTO DA PAGINA 1.

# EXTRAINDO IMAGENS - Abaixo:
# IMPORTANTE: AO EXECUTAR O METODO PARA IMAGENS, EXISTE UMA LIMITACAO POR PARTE DO PyPDF.

# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
# # COM ARQUIVO ABERTO, NA PASTA NOVA EU VOU PEGAR O NOME DA IMAGEM E SALVAR COMO WB = WRITE BYTES. fp = Nomenclatura qualquer. 
#     fp.write(imagem0.data)


# --------------------------

# ABAIXO, EU PEGO O MEU ARQUIVO PDF E SEPARO AS PAGINAS.

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)  # type: ignore

# --------------------------

# ABAIXO, EU PEGO AS PAGINAS QUE ESTAVAM SEPARADAS E JUNTO EM 1 PAGINA.
# IMPORTANTE = Propositalmente, as paginas na variavel file, foram colocadas invertidas. 

files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',

]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()