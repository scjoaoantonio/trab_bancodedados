import sqlite3

def import_sqlite_database():
    # conectar a um bd ou criar um do zero se nao existir nenhum
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    # abrir o arquivo sql e executar o script
    with open('data/database.sql', 'r') as script_file:
        script = script_file.read()
        cursor.executescript(script)

    # Commit as alterações e feche a conexão com o banco de dados
    conn.commit()
    conn.close()

def insert_time(nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Time (Nome, GolsSofridos, GolsMarcados, Pontos, Vitórias, Derrotas, PartidasJogadas, Empates, Treinador, CampeonatoAno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano))

    conn.commit()
    conn.close()

def delete_time(time_name):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Time WHERE Nome = ?", (time_name,))
    
    conn.commit()
    conn.close()

def update_time(time_name, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Time SET GolsSofridos=?, GolsMarcados=?, Pontos=?, Vitórias=?, Derrotas=?, PartidasJogadas=?, Empates=?, Treinador=?, CampeonatoAno=? WHERE Nome=?",
                   (gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano, time_name))

    conn.commit()
    conn.close()

def get_time_data():
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Time")
    time_data = cursor.fetchall()

    conn.close()

    return time_data


def insert_time(nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Time (Nome, GolsSofridos, GolsMarcados, Pontos, Vitórias, Derrotas, PartidasJogadas, Empates, Treinador, CampeonatoAno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano))

    conn.commit()
    conn.close()

def update_time(time_name, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Time SET GolsSofridos=?, GolsMarcados=?, Pontos=?, Vitórias=?, Derrotas=?, PartidasJogadas=?, Empates=?, Treinador=?, CampeonatoAno=? WHERE Nome=?",
                   (gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano, time_name))

    conn.commit()
    conn.close()

def get_time_data():
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Time")
    time_data = cursor.fetchall()

    conn.close()

    return time_data
