import pickle as pk
import json


class Livro:
    def __init__(self, titulo: str, autor: str, data_publicacao: str):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao


class Serializacao:
    def serializar_com_pickle(self, objeto, arquivo):
        with open(arquivo, 'wb') as arquivo:
            pk.dump(objeto, arquivo)

    def serializar_com_json(self, objeto, arquivo):
        with open(arquivo, 'w') as arquivo:
            json.dump(objeto, arquivo, indent=4, default=lambda o: o.__dict__)

    def desserializar_com_pickle(self, arquivo):
        with open(arquivo, 'rb') as arquivo:
            return pk.load(arquivo)

    def desserializar_com_json(self, arquivo):
        with open(arquivo, 'r') as arquivo:
            return json.load(arquivo)


def main():
    matematica = Livro('Matemática aplicada', 'Luiz Roberto', '10/03/2004')
    engajamento = Livro('Engajamento Cultural', 'Joshua Chatraw', '04/08/2021')
    mil_novecentos_e_oitenta_e_quatro = Livro('1984', 'George Orwell', '12/07/1945')

    livros = [matematica, engajamento, mil_novecentos_e_oitenta_e_quatro]

    minha_serializacao = Serializacao()

    for livro in livros:
        minha_serializacao.serializar_com_pickle(livro, f'{livro.titulo}.pkl')
        minha_serializacao.serializar_com_json(livro, f'{livro.titulo}.json')

    for livro in livros:
        print(livro.titulo)
        livro_pickle = minha_serializacao.desserializar_com_pickle(f'{livro.titulo}.pkl')
        livro_json = minha_serializacao.desserializar_com_json(f'{livro.titulo}.json')

        print(livro_pickle)
        print(livro_json)


if __name__ == '__main__':
    main()
