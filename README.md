# Documentação para o código XML
Este código é composto por três funções que permitem ler arquivos XML de dois tipos diferentes: NFe (Nota Fiscal Eletrônica) e NFSe (Nota Fiscal de Serviços Eletrônicos). O módulo `xmltodict` é utilizado para converter o arquivo XML em um dicionário Python, facilitando o acesso aos elementos do arquivo.

## Função `ler_arquivo_xml(nome_arquivo)`
Esta função recebe como argumento o nome do arquivo XML a ser lido e retorna um dicionário Python contendo os elementos do arquivo.

## Argumentos
* `nome_arquivo`: nome do arquivo XML a ser lido.
## Retorno
Dicionário Python com os elementos do arquivo XML.

## Função `ler_xml_danfe(documento)`
Esta função recebe como argumento o dicionário Python retornado pela função `ler_arquivo_xml()` referente a um arquivo XML de NFe (Nota Fiscal Eletrônica) e retorna um dicionário contendo informações da nota fiscal.

## Argumentos
* `documento`: dicionário Python retornado pela função `ler_arquivo_xml()` referente a um arquivo XML de NFe.
## Retorno
Dicionário contendo as seguintes informações da nota fiscal:
* `valor_total`: valor total da nota fiscal;
* `cnpj_vendeu`: CNPJ do emissor da nota fiscal;
* `nome_vendeu`: nome do emissor da nota fiscal;
* `cpf_comprou`: CPF do destinatário da nota fiscal;
* `nome_comprou`: nome do destinatário da nota fiscal;
* `lista_produtos`: lista contendo os produtos da nota fiscal, cada um representado por um tupla contendo o nome do produto e o valor.

## Função `ler_xml_servico(documento)`
Esta função recebe como argumento o dicionário Python retornado pela função `ler_arquivo_xml()` referente a um arquivo XML de NFSe (Nota Fiscal de Serviços Eletrônicos) e retorna um dicionário contendo informações da nota fiscal.

## Argumentos
* `documento`: dicionário Python retornado pela função `ler_arquivo_xml()` referente a um arquivo XML de NFSe.
## Retorno
Dicionário contendo as seguintes informações da nota fiscal:

* `valor_total`: valor total da nota fiscal;
* `cnpj_vendeu`: CNPJ do prestador de serviços da nota fiscal;
* `nome_vendeu`: nome do prestador de serviços da nota fiscal;
* `cpf_comprou`: CPF do tomador de serviços da nota fiscal;
* `nome_comprou`: nome do tomador de serviços da nota fiscal;
* `lista_produtos`: lista contendo a descrição do serviço da nota fiscal, representado por uma tupla contendo a descrição do serviço.
