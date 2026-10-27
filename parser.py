import argparse

parser = argparse.ArgumentParser(
    description="Organizador de arquivos"
)

parser.add_argument(
    '--dir', '-d', type=str, required=True, help='Pasta para organizar'
)

parser.add_argument(
    '--output', '-o', type=str, help='Diretório de saída'
)

parser.add_argument(
    '--copy', '-c', action='store_true', help='Copiar os arquivos para o destino ao invés de mover'
)

args = parser.parse_args()

if __name__ == '__main__':
    print(args.dir)
    print(args.output)
    print(args.copy)
