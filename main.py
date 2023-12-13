# Code in PT-BR (Portuguese)
import hashlib
import os

# Lista de códigos MD5 para os arquivos .rpf
codigos_md5 = {
    'x64a.rpf': '683610e269ba60c5fcc7a9f6d1a8bfd5',
    'x64b.rpf': '70af24cd4fe2c8ee58edb902f018a558',
    'x64c.rpf': '2a0f6f1c35ad567fe8e56b9c9cc4e4c6',
    'x64d.rpf': 'c8757b052ab5079c7749bcce02538b2e',
    'x64e.rpf': 'e5416c0b0000dad4014e0c5e9b878ff9',
    'x64f.rpf': '5c6fc965d56ae6d422cd6cbe5a65a3a5',
    'x64g.rpf': '1d8a64b337c3e07dffec0f53530cdb8e',
    'x64h.rpf': 'fe657d9282df303b080c3a2f6771c9ea',
    'x64i.rpf': 'bb271d313467465d62c75e208236487b',
    'x64j.rpf': '143deee4c7699b9f07ef21d43ae0915b',
    'x64k.rpf': 'da2c88b4ca69c99a86868a9433084a9d',
    'x64l.rpf': 'f4307b005a3e90192f235959621781d1',
    'x64m.rpf': 'a1304d84875747aa7405465d37d3c6fb',
    'x64n.rpf': 'c48a14fe1c301360a16e8b0c5472fd1d',
    'x64o.rpf': '6715a4eabbbc8868f15630bf917db49a',
    'x64p.rpf': '6ad56befada1db7cccd9cea7834c825b',
    'x64q.rpf': 'ff6d09527d7fdc005d3fa78435e09c8a',
    'x64r.rpf': '1465c9da5cc17b68f14915b6c1d815bc',
    'x64s.rpf': '2c6e61201eb4f60d5c3c1e9ae6d67a32',
    'x64t.rpf': '4c15a54a4c9573d7a0bcfa4689d9d1ed',
    'x64u.rpf': '2c9cff0cc5f99ad2218e4c4de39881b7',
    'x64v.rpf': 'db647120263d0282b6f6c555f6112a1c',
    'x64w.rpf': '46a4abe50bfc78c30c0173d888cf2c4a'
}

def calcular_md5_arquivo(caminho_arquivo):
    hash_md5 = hashlib.md5()
    with open(caminho_arquivo, 'rb') as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b''):
            hash_md5.update(bloco)
    return hash_md5.hexdigest()

def verificar_arquivos_gta_v(diretorio_jogo):
    for arquivo, codigo_md5 in codigos_md5.items():
        caminho_arquivo = os.path.join(diretorio_jogo, arquivo)
        if os.path.exists(caminho_arquivo):
            hash_arquivo = calcular_md5_arquivo(caminho_arquivo)
            if hash_arquivo == codigo_md5:
                print(f'O arquivo {arquivo} é válido.')
            else:
                print(f'O arquivo {arquivo} está corrompido.')
        else:
            print(f'O arquivo {arquivo} não foi encontrado.')

if _name_ == "_main_":
    diretorio_jogo = input("Informe o caminho para a pasta do GTA V: ")
    verificar_arquivos_gta_v(diretorio_jogo)
