CREATE TABLE Campeonato (
    Ano INTEGER PRIMARY KEY,
    Nome TEXT
);

CREATE TABLE Time (
    Nome TEXT PRIMARY KEY,
    Treinador TEXT,
    Pontos INTEGER,
    PartidasJogadas INTEGER,
    Vitórias INTEGER,
    Derrotas INTEGER,
    Empates INTEGER
    GolsMarcados INTEGER,
    GolsSofridos INTEGER,
);

CREATE TABLE Partida (
    IdPartida INTEGER PRIMARY KEY,
    PlacarMandante INTEGER,
    PlacarVisitante INTEGER,
    Estadio TEXT,
    Data DATE,
    CampeonatoAno INTEGER,
    TimeMandante TEXT,
    TimeVisitante TEXT,
    FOREIGN KEY (CampeonatoAno) REFERENCES Campeonato(Ano),
    FOREIGN KEY (TimeMandante) REFERENCES Time(Nome),
    FOREIGN KEY (TimeVisitante) REFERENCES Time(Nome)
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
