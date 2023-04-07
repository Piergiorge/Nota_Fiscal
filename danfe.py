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
        'lista_produtos': [(produtos,)],
    }
   
