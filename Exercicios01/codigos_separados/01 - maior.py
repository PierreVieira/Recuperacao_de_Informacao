def maior(a, b):
    """
    Retorna o maior número entre 'a' e 'b'.
    @author: Pierre Vieira
    """
    if a > b:
        return a
    return b


if __name__ == '__main__':
    a, b = map(int, input('Informe dois valores em sequência: ').split())
    print(f'O maior valor entre {a} e {b} é {maior(a, b)}')
