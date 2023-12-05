import pandas as pd
import streamlit as st
import data
import requests
import plotly.express as px
from bs4 import BeautifulSoup

# calcular os pontos de cada time
def calculate_points(vitorias, empates, derrotas):
    return (vitorias * 3) + empates + (derrotas * 0)

'''
Função para inserir um time:
    inputs para coletar as informações do time;
    insere o time na tabela.
'''
def insert_time_screen():
    st.header("Inserir um Time")
    nome = st.text_input("Nome do Time")
    treinador = st.text_input("Sigla")
    vitorias = st.number_input("Vitórias",step=1)
    derrotas = st.number_input("Derrotas",step=1)
    empates = st.number_input("Empates",step=1)
    partidas_jogadas = vitorias + derrotas + empates
    gols_marcados = st.number_input("Gols Marcados",step=1)
    gols_sofridos = st.number_input("Gols Sofridos",step=1)
    saldo = gols_marcados - gols_sofridos
    campeonato_ano = saldo
    
    if st.button("Inserir"):
        pontos = calculate_points(vitorias, empates, derrotas)
        data.insert_time(nome, treinador,pontos, vitorias, derrotas, empates, partidas_jogadas,gols_marcados, gols_sofridos,campeonato_ano)
        st.success("Time inserido com sucesso!")

'''  
Função para deletar um time:
    resgata os times inseridos;
    seleciona o time a ser excluído;
    deleta o time da tabela.
'''
def delete_time_screen():
    st.header("Deletar um Time")

    time_data = data.get_time_data()

    selected_time = st.selectbox("Selecione o time a ser excluído:", time_data)

    if st.button("Excluir"):
        if selected_time:
            time_name = selected_time[0]  
            data.delete_time(time_name)  
            st.success(f"Time '{time_name}' excluído com sucesso!")

'''
Função para atualizar algum time:
    resgata os times inseridos;
    seleciona o time a ser atualizado;
    atualiza o time na tabela.
'''
def update_time_screen():
    st.header("Alterar um Time")

    time_data = data.get_time_data()

    selected_time = st.selectbox("Selecione o time a ser atualizado:", time_data)

    if selected_time:
        st.write("Atualize os campos abaixo:")

        time_name, treinador, pontos, vitorias, derrotas,empates, partidas_jogadas,gols_marcados, gols_sofridos, campeonato_ano = selected_time

        new_treinador = st.text_input("Nova Sigla", treinador)
        new_vitorias = st.number_input("Novas Vitórias", vitorias)
        new_derrotas = st.number_input("Novas Derrotas", derrotas)
        new_empates = st.number_input("Novos Empates", empates)
        new_partidas_jogadas = new_derrotas + new_empates + new_vitorias
        new_gols_marcados = st.number_input("Novos Gols Marcados", gols_marcados)
        new_gols_sofridos = st.number_input("Novos Gols Sofridos", float(gols_sofridos))
        new_campeonato_ano = new_gols_marcados - new_gols_sofridos

        if st.button("Atualizar"):
            print(f"Vitórias: {new_vitorias}, Empates: {new_empates}, Derrotas: {new_derrotas}")
            
            if new_partidas_jogadas == new_vitorias + new_empates + new_derrotas:
                new_pontos = calculate_points(new_vitorias, new_empates, new_derrotas)
                print(f"Novos Pontos: {new_pontos}")
                
                data.update_time(time_name, new_treinador, new_pontos, new_vitorias, new_derrotas, new_empates, new_partidas_jogadas,  new_gols_marcados,new_gols_sofridos,  new_campeonato_ano)
                st.success(f"Dados do time '{time_name}' atualizados com sucesso!")
            else:
                st.error("A soma de vitórias, empates e derrotas não coincide com o número de partidas jogadas.")

# Mostra os times e suas estatísticas na tabela de classificação
def show_ranking():
    st.header("Classificação dos Times")
    time_data = data.get_time_data()

    if time_data:
        df = pd.DataFrame(time_data, columns=["Nome", "Sigla", "Pontos", "Vitórias", "Derrotas", "Empates", "Jogos","GolsMarcados", "GolsSofridos", "Saldo"])
        df["GolsSofridos"] = pd.to_numeric(df["GolsSofridos"], errors="coerce").astype(int)

        df["Pts"] = df.apply(lambda row: calculate_points(row["Vitórias"], row["Empates"], row["Derrotas"]), axis=1)

        df = df[["Nome", "Sigla", "Pontos", "Jogos", "Vitórias", "Derrotas", "Empates", "GolsMarcados", "GolsSofridos", "Saldo"]]

        df.columns = ["Nome", "Sigla", "Pontos", "Jogos", "Vitórias", "Derrotas", "Empates", "Gols Pró", "Gols Contra", "Saldo"]

        df = df.sort_values(by=["Pontos", "Vitórias", "Gols Contra", "Gols Pró"], ascending=[False, False, False, False])

        df.index = df.index + 1

        st.dataframe(df)  
    else:
        st.write("Nenhum dado de time disponível.")

'''
Função para inserir um jogador:
    inputs para coletar as informações do jogador;
    insere o jogador na tabela.
'''
def insert_jogador_screen():
    st.header("Inserir um Jogador")
    nome_jogador = st.text_input("Nome do Jogador")
    cartoes_amarelos = st.number_input("Cartões Amarelos", step=1)
    nacionalidade = st.text_input("Nacionalidade")
    cartoes_vermelhos = st.number_input("Cartões Vermelhos", step=1)
    faltas_cometidas = st.number_input("Faltas Cometidas", step=1)
    gols = st.number_input("Gols", step=1)
    time_nome = st.text_input("Nome do Time")

    if st.button("Inserir"):
        data.insert_jogador(nome_jogador, cartoes_amarelos, nacionalidade, cartoes_vermelhos, faltas_cometidas, gols, time_nome)
        st.success("Jogador inserido com sucesso!")

'''
Função para atualizar algum jogador:
    resgata os jogadores inseridos;
    seleciona o jogador a ser atualizado;
    atualiza o jogador na tabela.
'''
def update_jogador_screen():
    st.header("Alterar um Jogador")

    jogador_data = data.get_jogador_data()

    selected_jogador = st.selectbox("Selecione o jogador a ser atualizado:", jogador_data)

    if selected_jogador:
        st.write("Atualize os campos abaixo:")

        nome_jogador, cartoes_amarelos, nacionalidade, cartoes_vermelhos, faltas_cometidas, gols, time_nome = selected_jogador

        new_cartoes_amarelos = st.number_input("Novos Cartões Amarelos", cartoes_amarelos)
        new_nacionalidade = st.text_input("Nova Nacionalidade", nacionalidade)
        new_cartoes_vermelhos = st.number_input("Novos Cartões Vermelhos", cartoes_vermelhos)
        new_faltas_cometidas = st.number_input("Novas Faltas Cometidas", faltas_cometidas)
        new_gols = st.number_input("Novos Gols", gols)
        new_time_nome = st.text_input("Nome do Novo Time", time_nome)

        if st.button("Atualizar"):
            data.update_jogador(nome_jogador, new_cartoes_amarelos, new_nacionalidade, new_cartoes_vermelhos, new_faltas_cometidas, new_gols, new_time_nome)
            st.success(f"Dados do jogador '{nome_jogador}' atualizados com sucesso!")

'''  
Função para deletar um jogador:
    resgata os jogadores inseridos;
    seleciona o jogador a ser excluído;
    deleta o jogador da tabela.
'''
def delete_jogador_screen():
    st.header("Deletar um Jogador")
    
    jogador_data = data.get_jogador_data()
    
    selected_jogador = st.selectbox("Selecione o jogador a ser excluído:", jogador_data)
    
    if st.button("Excluir"):
        if selected_jogador:
            nome_jogador = selected_jogador[0]  
            data.delete_jogador(nome_jogador)  
            st.success(f"Jogador '{nome_jogador}' excluído com sucesso!")
            
'''  
Função para obter os dados da artilharia do campeonato:
    faz um webscrapping na página selecionada;
    seleciona os dados resgatados
    exibe esses dados (ranking dos artilheiros + gols feitos)
'''
def obter_dados_artilharia():
    url = 'https://ge.globo.com/futebol/brasileirao-serie-a/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        artilharia_section = soup.find('section', class_='artilharia-wrapper')

        if artilharia_section:
            jogadores = artilharia_section.find_all('div', class_='jogador')

            st.header("Artilharia")

            for jogador in jogadores:
                nome = jogador.find('div', class_='jogador-nome').text
                clube_escudo = jogador.find('div', class_='jogador-escudo').img['alt']
                gols = jogador.find('div', class_='jogador-gols').text

                st.write(f"{nome} ({clube_escudo}) - {gols} gols")

        else:
            st.warning("Seção de artilharia não encontrada na página.")

    else:
        st.error(f"Falha ao obter a página. Status Code: {response.status_code}")

'''  
Função para obter os dados do campeonato:
    faz um webscrapping na página recebida;
    seleciona os dados resgatados
    exibe esses dados (time fair play + time mais agressivo)
'''
def extrair_dados_estatisticas(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        tabela = soup.find('table', class_='Table')

        if tabela:
            cabecalho = tabela.find('thead')
            colunas = [th.text.strip() for th in cabecalho.find_all('th')]

            linhas = tabela.find('tbody').find_all('tr')
            dados = []

            for linha in linhas:
                valores = [td.text.strip() for td in linha.find_all('td')]
                dados.append(dict(zip(colunas, valores)))

            time_maior_soma = max(dados, key=lambda x: int(x.get('PTS', 0)), default={})
            time_menor_soma = min(dados, key=lambda x: int(x.get('PTS', 0)), default={})

            st.write(f"Time mais agressivo: {time_maior_soma.get('Hora', 'Nome não encontrado')}")
            st.write(f"Time Fair Play: {time_menor_soma.get('Hora', 'Nome não encontrado')}")

            st.header("Dados da Tabela de Estatísticas")
            for i, dado in enumerate(dados, 1):
                st.subheader(f"Time {i}")
                st.write(dado)

        else:
            st.warning("Nenhuma tabela de estatísticas encontrada na página.")

    else:
        st.error(f"Falha ao obter a página. Status Code: {response.status_code}")

'''
Função para montar o dashboard com os dados inseridos no banco de dados:
    resgata os dados do BD;
    exibe esses dados em gráficos;
'''
def dashboard_page():
    st.title("Índices e Tabelas")

    time_data = data.get_time_data()

    if time_data:
        df = pd.DataFrame(time_data, columns=["Nome", "Sigla", "Pontos", "Vitórias", "Derrotas", "Empates", "Jogos","GolsMarcados", "GolsSofridos", "Saldo"])

        df["GolsMarcados"] = pd.to_numeric(df["GolsMarcados"], errors="coerce")
        df["GolsSofridos"] = pd.to_numeric(df["GolsSofridos"], errors="coerce")

        df["GolsPró/GolsTotais"] = df.apply(lambda row: row["GolsMarcados"] / (row["GolsMarcados"] + row["GolsSofridos"]) if row["GolsMarcados"] + row["GolsSofridos"] != 0 else 0, axis=1)
        df["GolsContra/GolsTotais"] = df.apply(lambda row: row["GolsSofridos"] / (row["GolsMarcados"] + row["GolsSofridos"]) if row["GolsMarcados"] + row["GolsSofridos"] != 0 else 0, axis=1)
        df["Vitórias/Jogos"] = df.apply(lambda row: row["Vitórias"] / row["Jogos"] if row["Jogos"] != 0 else 0, axis=1)
        df["Derrotas/Jogos"] = df.apply(lambda row: row["Derrotas"] / row["Jogos"] if row["Jogos"] != 0 else 0, axis=1)
        df["Empates/Jogos"] = df.apply(lambda row: row["Empates"] / row["Jogos"] if row["Jogos"] != 0 else 0, axis=1)
        df["Marcados/Sofridos"] = df.apply(lambda row: row["GolsMarcados"] / row["GolsSofridos"] if row["GolsSofridos"] != 0 else 0, axis=1)

        st.subheader("Top 5 Times por Índice:")
        st.write("1. Marcados/Totais")
        st.dataframe(df.nlargest(5, "GolsPró/GolsTotais")[["Nome", "GolsPró/GolsTotais"]])

        st.write("2. Gols Contra/Totais")
        st.dataframe(df.nlargest(5, "GolsContra/GolsTotais")[["Nome", "GolsContra/GolsTotais"]])

        st.write("3. Vitórias/Jogos")
        st.dataframe(df.nlargest(5, "Vitórias/Jogos")[["Nome", "Vitórias/Jogos"]])

        st.write("4. Derrotas/Jogos")
        st.dataframe(df.nlargest(5, "Derrotas/Jogos")[["Nome", "Derrotas/Jogos"]])

        st.write("5. Empates/Jogos")
        st.dataframe(df.nlargest(5, "Empates/Jogos")[["Nome", "Empates/Jogos"]])
        
        st.write("6. Marcados/Sofridos")
        st.dataframe(df.nlargest(5, "Marcados/Sofridos")[["Nome", "Marcados/Sofridos"]])

        st.subheader("Gráficos de dispersão para Variáveis Numéricas:")
        scatter_columns = ["Pontos", "Vitórias", "Derrotas", "Empates", "GolsMarcados", "GolsSofridos", "Saldo"]
        for column in scatter_columns:
            st.write(f"Gráfico de dispersão para {column}")
            scatter_fig = px.scatter(df, x="Nome", y=column, title=f"Gráfico de dispersão para {column}")
            st.plotly_chart(scatter_fig)

    else:
        st.write("Nenhum dado de time disponível.")

# Formulário de login
def login():
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Nome de usuário")
    password = st.sidebar.text_input("Senha", type="password")
    return username, password

# Autenticação do login
def authenticate(username, password):
    if username == "admin" and password == "admin":
        return "admin"
    elif username == "user" and password == "user":
        return "user"
    else:
        return None
'''
Função principal:
    Faz o login e autenticação;
    Mostra as telas de acordo com a permissão do usuário;
    Chama as funções de acordo com a tela selecionada.
'''
def main_app():
    st.title("Campeonato Brasileiro 2023")

    username, password = login()
    role = authenticate(username, password)

    if role is None:
        st.error("Insira suas credenciais válidas e faça seu login.")
    else:
        if role == "admin":
            option = st.sidebar.radio("Menu", ("Classificação", "Inserir Time", "Deletar Time", "Alterar Time", "Dashboard Time","Inserir Jogador","Alterar Jogador","Deletar Jogador","Artilharia Dados","Agressivo ou Fair Play"))
        if role == "user":
            option = st.sidebar.radio("Menu", ("Classificação","Dashboard Time","Artilharia Dados","Agressivo ou Fair Play"))

        if role == "admin": 
            if option == "Inserir Time":
                insert_time_screen()
            elif option == "Deletar Time":
                delete_time_screen()
            elif option == "Alterar Time":
                update_time_screen()
            elif option == "Dashboard Time":
                dashboard_page()
            elif option == "Inserir Jogador":
                insert_jogador_screen()
            elif option == "Alterar Jogador":
                update_jogador_screen()
            elif option == "Deletar Jogador":
                delete_jogador_screen()
            elif option == "Artilharia Dados":
                obter_dados_artilharia()
            elif option == "Agressivo ou Fair Play":
                url_da_pagina = 'https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/vista/cartoes'
                extrair_dados_estatisticas(url_da_pagina)

        if role == "user":
            if option == "Dashboard Time":
                dashboard_page()
            elif option == "Artilharia Dados":
                obter_dados_artilharia()
            elif option == "Agressivo ou Fair Play":
                url_da_pagina = 'https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/vista/cartoes'
                extrair_dados_estatisticas(url_da_pagina)


        if option == "Classificação":
            show_ranking()

