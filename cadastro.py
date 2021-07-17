from pessoa import Pessoa

pessoas = []


class CadastroPessoa(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def incluir():
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        pessoas.append(CadastroPessoa(nome, idade))
        return pessoas

    def remover(nome):
        if len(pessoas) == 0:
            print('Não há registros em Pessoas.')
        else:
            for idx, pessoa in enumerate(pessoas):
                if str(nome) == str(pessoa.nome):
                    del(pessoas[idx])
                    print(f'Registro {nome} removido.')
                else:
                    print(f'Registro {nome} não encontrada.')

    def consultar(nome):
        if len(pessoas) == 0:
            print('Não há registros em Pessoas.')
        else:
            for pessoa in pessoas:
                if str(nome) == str(pessoa.nome):
                    print(f'{nome} se encontra nos registros.')
                else:
                    print(f'{nome} não consta nos registros.')

    def atualizar(nome):
        if len(pessoas) == 0:
            print('Não há registros em Pessoas.')
        else:
            for idx, pessoa in enumerate(pessoas):
                if str(nome) == str(pessoa.nome):
                    nome_aux = input('Nome: ')
                    idade = int(input('Idade: '))
                    p_aux = CadastroPessoa(nome_aux, idade)
                    pessoas[idx] = p_aux
                else:
                    print(f'{nome} não consta nos registros.')

    def listar():
        for pessoa in pessoas:
            print(f'Nome: {pessoa.nome.title()} Idade: {pessoa.idade}')


def main():
    p1 = CadastroPessoa.incluir()
    CadastroPessoa.listar()

    CadastroPessoa.atualizar('sergio')

    CadastroPessoa.remover('sergio')
    # CadastroPessoa.listar()
    CadastroPessoa.listar()


if __name__ == '__main__':
    main()
