class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def __str__(self):
        return f'Nome: {self.nome} - Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


def __str__(self):
    return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

def __str__(self):
    return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas        #Chamando o construtor da list e passando os programas
        #super().__init__(programas)    
    
    def __getitem__(self, item)-> None:
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em p�nico', 1999, 1000)
demolidor = Serie('Demolidor', 2015, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

minha_lista = [atlanta, vingadores, tmep, demolidor]
playlist_fim_de_semana = Playlist('Play fim de semana', minha_lista)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)