import format_files as ff
from pathlib import Path
from parser import args
import shutil


def validar_formato(formato):
    for tipo, formatos in ff.FORMATS.items():
        if formato in formatos:
            return tipo
    return -1


def criar_diretorio(dir, nome):
    nova_pasta = Path(str(dir.resolve()) + '/' + nome)
    nova_pasta.mkdir(exist_ok=True)
    return nova_pasta


def organizar(entrada, saida=None):
    for item in entrada.iterdir():
        if not item.is_file():
            continue
        
        item_dividido = item.name.split('.')
        formato = item_dividido[-1]

        tipo = validar_formato(formato)

        if tipo == -1:
            continue
        
        pasta_destino = criar_diretorio(entrada if saida is None else saida, tipo)
        
        if args.copy:
            shutil.copy(item, str(pasta_destino.resolve()) + '/' + item.name)
        else:
            item.replace(str(pasta_destino.resolve()) + '/' + item.name)


def main():
    pasta_entrada = Path(args.dir)
    pasta_saida = None
    if args.output is not None:
        pasta_saida = Path(args.output)

    if not (pasta_entrada.is_dir()):
        print('erro: diretório de entrada inválidas')
        return

    if pasta_entrada.resolve() == Path().resolve():
        print('erro: pasta de entrada não deve ser igual a pasta do programa')
        return

    if pasta_saida is not None and pasta_saida.resolve() == Path().resolve():
        print('erro: pasta de entrada não deve ser igual a pasta do programa')
        return

    if not pasta_saida.is_dir():
        print('erro: diretório de saida inválidas')
        return


    organizar(pasta_entrada, pasta_saida)



if __name__ == '__main__':
    main()
