from urllib.request import urlopen, Request


class Coletor:
    def __init__(self, url, info_headers):
        self.__url = url
        self.__info_headers = info_headers
        self.__req = Request(url=self.__url, headers=self.__info_headers)
        self.__url_open = urlopen(self.__req)
        self.__texto_html_string = str(self.__url_open.read())

    @property
    def texto_html_string(self) -> str:
        """
        :return: texto html da url em string.
        """
        return self.__texto_html_string

    @property
    def texto_html_lista(self):
        """
        :return: uma lista com todas as tags em formato de string do html lido
        """
        lista_html = self.texto_html_string.split('\\n')
        return lista_html


class Filtro:
    def __init__(self, texto_html: str, lista_html: list):
        self.__texto_html = texto_html
        self.__lista_html = lista_html

    def filtrar_info(self, tag_a_pesquisar, id):
        """
        :param tag_a_pesqueisar: Pesquisa a partir de uma tag informada como parâmetro
        :return: value da tag.
        """
        lista_interesse = self.__pegar_lista_interesse(tag_a_pesquisar)
        for tag in lista_interesse:
            if id in tag:
                return tag[len(tag_a_pesquisar):len(tag_a_pesquisar) + 4]

    def __pegar_lista_interesse(self, tag_a_pesquisar):
        lista_interesse = []
        string = ''
        for char in self.__texto_html:
            string += char
            if char == '<':
                if tag_a_pesquisar in string:
                    lista_interesse.append(string)
                string = ''
        return lista_interesse


if __name__ == '__main__':
    url = 'https://www.melhorcambio.com/dolar-hoje'
    headers = {'User-Agent': 'Chrome/80.0.3987.132 (Windows 10)'}
    coletor = Coletor(url, headers)
    texto_html = coletor.texto_html_string
    lista_html = coletor.texto_html_lista
    filtro = Filtro(texto_html, lista_html)
    tag = 'input type="text" value="'
    dolar_hoje = filtro.filtrar_info(tag, 'comercial')
    print(f'Dólar hoje: {dolar_hoje}')
