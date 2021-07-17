from piloto import Piloto

pilotos = []


class CadastroPiloto(Piloto):
    def __init__(self, nome, idade, prof):
        super().__init__(nome, idade, prof)

    def incluir():
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        prof = float(input('Proficiência: '))
        p = CadastroPiloto(nome, idade, prof)
        pilotos.append(p)
        return p

    def remover(nome):
        status = False
        if len(pilotos) == 0:
            print('Não há registros em Pessoas.')
        else:
            for idx, piloto in enumerate(pilotos):
                if str(nome) == str(piloto.nome):
                    del(pilotos[idx])
                    print(f'Piloto {nome} removido.')
                    status = True
                else:
                    print(f'Piloto {nome} não encontrado.')
        return status

    def consultar(nome):
        if len(pilotos) == 0:
            print('Não há registros em Pilotos.')
        else:
            for piloto in pilotos:
                if str(nome) == str(piloto.nome):
                    print(f'Piloto {nome} se encontra nos registros.')
                    return piloto
                else:
                    print(f'Piloto {nome} não consta nos registros.')

    def atualizar(nome):
        if len(pilotos) == 0:
            print('Não há registros em Pilotos.')
        else:
            for idx, piloto in enumerate(pilotos):
                if str(nome) == str(piloto.nome):
                    print(
                        f'Piloto {nome} encontrado em nossos registros.\nVamos atualizar os dados: ')
                    nome_aux = input('Nome: ')
                    idade_aux = int(input('Idade: '))
                    prof_aux = float(input('Proficiência: '))
                    p_aux = CadastroPiloto(nome_aux, idade_aux, prof_aux)
                    pilotos[idx] = p_aux
                    print('Piloto atualizado.')
            else:
                print(f'Piloto {nome} não consta nos registros.')


def main():
    pil1 = CadastroPiloto.incluir()
    print(pil1.__dict__)

    pil2 = CadastroPiloto.incluir()
    print(pil2.__dict__)

    CadastroPiloto.consultar('sergio')

    CadastroPiloto.atualizar('gabriel')
    CadastroPiloto.remover('sergio')

    print(pilotos.__repr__())


if __name__ == '__main__':
    main()
