CREATE TABLE Campeonato (
    Ano INTEGER PRIMARY KEY,
    Nome TEXT
);

CREATE TABLE Time (
    Nome TEXT PRIMARY KEY,
    GolsSofridos INTEGER,
    GolsMarcados INTEGER,
    Pontos INTEGER,
    Vitórias INTEGER,
    Derrotas INTEGER,
    PartidasJogadas INTEGER,
    Empates INTEGER,
    Treinador TEXT,
    CampeonatoAno INTEGER,
    FOREIGN KEY (CampeonatoAno) REFERENCES Campeonato (Ano)
);

CREATE TABLE Partida (
    IdPartida INTEGER PRIMARY KEY,
    PlacarMandante INTEGER,
    PlacarVisitante INTEGER,
    Estadio TEXT,
    Data DATE,
    CampeonatoAno INTEGER,
    FOREIGN KEY (CampeonatoAno) REFERENCES Campeonato (Ano)
);

CREATE TABLE Jogador (
    Bid INTEGER PRIMARY KEY,
    Nome TEXT,
    CartoesAmarelos INTEGER,
    Nacionalidade TEXT,
    CartoesVermelhos INTEGER,
    FaltasCometidas INTEGER,
    Gols INTEGER,
    TimeNome TEXT,
    FOREIGN KEY (TimeNome) REFERENCES Time (Nome)
);
