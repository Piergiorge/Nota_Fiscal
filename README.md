# Nota_Fiscal

ler_arquivo_xml(nome_arquivo)
Função que lê um arquivo XML e retorna um dicionário com o conteúdo do arquivo.

Argumentos:
nome_arquivo: string com o nome do arquivo XML a ser lido.
Retorno:
documento: dicionário com o conteúdo do arquivo XML.
ler_xml_danfe(documento)
Função que lê um arquivo XML de uma DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) e retorna um dicionário com as informações relevantes.

Argumentos:
documento: dicionário com o conteúdo do arquivo XML da DANFE.
Retorno:
resposta: dicionário com as seguintes informações:
valor_total: valor total da nota fiscal;
cnpj_vendeu: CNPJ da empresa que vendeu;
nome_vendeu: nome da empresa que vendeu;
cpf_comprou: CPF do comprador;
nome_comprou: nome do comprador;
lista_produtos: lista com os produtos da nota fiscal, onde cada produto é uma tupla contendo o nome e valor.
ler_xml_servico(documento)
Função que lê um arquivo XML de uma nota fiscal de serviço e retorna um dicionário com as informações relevantes.

Argumentos:
documento: dicionário com o conteúdo do arquivo XML da nota fiscal de serviço.
Retorno:
resposta: dicionário com as seguintes informações:
valor_total: valor total da nota fiscal;
cnpj_vendeu: CNPJ da empresa que prestou o serviço;
nome_vendeu: nome da empresa que prestou o serviço;
cpf_comprou: CPF do tomador do serviço;
nome_comprou: nome do tomador do serviço;
lista_produtos: lista com a descrição do serviço, que é um único item.
