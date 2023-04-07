import xmltodict
import os

def ler_arquivo_xml(nome_arquivo):
    with open(nome_arquivo, 'rb', encoding='utf-8') as arquivo:
        documento = xmltodict.parse(arquivo)
    return documento

def ler_xml_danfe(documento):
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']
    produtos = dic_notafiscal['det']
    lista_produtos = [(produto['prod']['xProd'], produto['prod']['vProd']) for produto in produtos]

    resposta = {
        'valor_total': valor_total,
        'cnpj_vendeu': cnpj_vendeu,
        'nome_vendeu': nome_vendeu,
        'cpf_comprou': cpf_comprou,
        'nome_comprou': nome_comprou,
        'lista_produtos': lista_produtos,
    }
    return resposta


def ler_xml_servico(documento):
    dic_notafiscal = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    valor_total = dic_notafiscal['Servico']['Valores']['ValorServicos']
    cnpj_vendeu = dic_notafiscal['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendeu = dic_notafiscal['PrestadorServico']['RazaoSocial']
    cpf_comprou = dic_notafiscal['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprou = dic_notafiscal['TomadorServico']['RazaoSocial']
    produtos = dic_notafiscal['Servico']['Discriminacao']
    resposta = {
        'valor_total': valor_total,
        'cnpj_vendeu': cnpj_vendeu,
        'nome_vendeu': nome_vendeu,
        'cpf_comprou': cpf_comprou,
        'nome_comprou': nome_comprou,
        'lista_produtos' = [(prod['prod']['xProd'], prod['prod']['vProd']) for prod in produtos]
    }
    return resposta
   
lista_arquivos = os.listdir("NFs Finais") # lista os nomes dos arquivos de uma pasta

for arquivo in lista_arquivos: # para cada arquivo
    if 'xml' in arquivo: # se tem xml no nome do arquivo
        if 'DANFE' in arquivo: # se tem DANFE no nome do arquivo
            print(ler_xml_danfe(f'NFs Finais/{arquivo}')) # rodar o leitor de XML de DANFE para esse arquivo
        else:
            print(ler_xml_servico(f'NFs Finais/{arquivo}'))
