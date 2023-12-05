import sqlite3

'''
Função para importar o banco de dados:
    Conecta ao banco de dados ou cria um se não existir;
    abre o arquivo sql para executar o script
    atualiza as alterações e fecha o banco de dados quando acabar as operações
'''
def import_sqlite_database():
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    with open('data/database.sql', 'r') as script_file:
        script = script_file.read()
        cursor.executescript(script)

    conn.commit()
    conn.close()

'''
Função para inserir um time no banco de dados:
    Conecta com o BD;
    Executa a função de INSERT para inserir os dados
    Fecha o BD
'''
def insert_time(nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Time (Nome, GolsSofridos, GolsMarcados, Pontos, Vitórias, Derrotas, PartidasJogadas, Empates, Treinador, CampeonatoAno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano))

    conn.commit()
    conn.close()

'''
Função para deletar um time no banco de dados:
    Conecta com o BD;
    Executa a função de DELETE para deletar os dados
    Fecha o BD
'''
def delete_time(time_name):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Time WHERE Nome = ?", (time_name,))
    
    conn.commit()
    conn.close()

'''
Função para atualizar um time no banco de dados:
    Conecta com o BD;
    Executa a função de UPDATE para atualizar os dados
    Fecha o BD
'''
def update_time(time_name, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Time SET GolsSofridos=?, GolsMarcados=?, Pontos=?, Vitórias=?, Derrotas=?, PartidasJogadas=?, Empates=?, Treinador=?, CampeonatoAno=? WHERE Nome=?",(gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano, time_name))

    conn.commit()
    conn.close()

'''
Função para obter os dados de um time no banco de dados:
    Conecta com o BD;
    Executa a função de SELECT para deletar os dados
    Fecha o BD
'''
def get_time_data():
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Time")
    time_data = cursor.fetchall()

    conn.close()

    return time_data

'''
Função para inserir um jogador no banco de dados:
    Conecta com o BD;
    Executa a função de INSERT para inserir os dados
    Fecha o BD
'''
def insert_jogador(nome, cartoes_amarelos, nacionalidade, cartoes_vermelhos, faltas_cometidas, gols, time_nome):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Jogador (Nome, CartoesAmarelos, Nacionalidade, CartoesVermelhos, FaltasCometidas, Gols, TimeNome) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (nome, cartoes_amarelos, nacionalidade, cartoes_vermelhos, faltas_cometidas, gols, time_nome))

    conn.commit()
    conn.close()

'''
Função para deletar um jogador no banco de dados:
    Conecta com o BD;
    Executa a função de DELETE para deletar os dados
    Fecha o BD
'''
def delete_jogador(nome_jogador):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Jogador WHERE Nome = ?", (nome_jogador,))
    
    conn.commit()
    conn.close()

'''
Função para atualizar um jogador no banco de dados:
    Conecta com o BD;
    Executa a função de UPDATE para atualizar os dados
    Fecha o BD
'''
def update_jogador(nome, cartoes_amarelos, nacionalidade, cartoes_vermelhos, faltas_cometidas, gols, time_nome):
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Jogador SET CartoesAmarelos=?, Nacionalidade=?, CartoesVermelhos=?, FaltasCometidas=?, Gols=?, TimeNome=? WHERE Nome=?",
                   (cartoes_amarelos, nacionalidade, cartoes_vermelhos, faltas_cometidas, gols, time_nome, nome))

    conn.commit()
    conn.close()

'''
Função para obter os dados de um jogador no banco de dados:
    Conecta com o BD;
    Executa a função de SELECT para deletar os dados
    Fecha o BD
'''
def get_jogador_data():
    conn = sqlite3.connect('data/campeonato.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Nome, CartoesAmarelos, Nacionalidade, CartoesVermelhos, FaltasCometidas, Gols, TimeNome FROM Jogador")
    jogador_data = cursor.fetchall()

    conn.close()

    return jogador_data
