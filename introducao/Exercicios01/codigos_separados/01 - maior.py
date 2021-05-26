def maior(a, b):
    """
    Retorna o maior número entre 'a' e 'b'.
    @author: Pierre Vieira
    """
    return a if a > b else b  # Retorne 'a' se 'a' maior que 'b', senão retorne 'b'


if __name__ == '__main__':
    print(f'teste (a > b): {maior(5, 2)}')
    print(f'teste (a < b): {maior(8, 5)}')
    print(f'teste (a = b): {maior(3, 3)}')
