import pandas as pd
import streamlit as st
import data

# Funções
def insert_time_screen():
    # Inserir um time no banco de dados
    st.header("Inserir um Time")
    nome = st.text_input("Nome do Time")
    gols_sofridos = st.number_input("Gols Sofridos")
    gols_marcados = st.number_input("Gols Marcados")
    pontos = st.number_input("Pontos")
    vitorias = st.number_input("Vitórias")
    derrotas = st.number_input("Derrotas")
    partidas_jogadas = st.number_input("Partidas Jogadas")
    empates = st.number_input("Empates")
    treinador = st.text_input("Treinador")
    campeonato_ano = st.number_input("Ano do Campeonato")

    if st.button("Inserir"):
        if nome:
            data.insert_time(nome, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano)
            st.success("Time inserido com sucesso!")


# Função para tela de exclusão de time
def delete_time_screen():
    st.header("Deletar um Time")
    
    # Puxar a lista de times do banco de dados
    time_data = data.get_time_data()
    
    # input para selecionar o time a ser excluído
    selected_time = st.selectbox("Selecione o time a ser excluído:", time_data)
    
    if st.button("Excluir"):
        if selected_time:
            time_name = selected_time[0]  # O nome do time está na primeira coluna
            data.delete_time(time_name)  # Chame a função para excluir o time no banco de dados
            st.success(f"Time '{time_name}' excluído com sucesso!")

# Função para deletar um time no banco de dados
def delete_time(time_name):
    data.delete_time(time_name)

# Função para atualizar um time
def update_time_screen():
    st.header("Alterar um Time")
    
    # puxar a lista de times do banco de dados
    time_data = data.get_time_data()
    
   # input para selecionar o time a ser atualizado
    selected_time = st.selectbox("Selecione o time a ser atualizado:", time_data)
    
    if selected_time:
        st.write("Atualize os campos abaixo:")
        
        # Recuperar os dados do time selecionado
        time_name, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano = selected_time

        # Campos de entrada para os novos valores
        new_gols_sofridos = st.number_input("Novos Gols Sofridos", gols_sofridos)
        new_gols_marcados = st.number_input("Novos Gols Marcados", gols_marcados)
        new_pontos = st.number_input("Novos Pontos", pontos)
        new_vitorias = st.number_input("Novas Vitórias", vitorias)
        new_derrotas = st.number_input("Novas Derrotas", derrotas)
        new_partidas_jogadas = st.number_input("Novas Partidas Jogadas", partidas_jogadas)
        new_empates = st.number_input("Novos Empates", empates)
        new_treinador = st.text_input("Novo Treinador", treinador)
        new_campeonato_ano = st.number_input("Novo Ano do Campeonato", campeonato_ano)

        if st.button("Atualizar"):
            data.update_time(time_name, new_gols_sofridos, new_gols_marcados, new_pontos, new_vitorias, new_derrotas, new_partidas_jogadas, new_empates, new_treinador, new_campeonato_ano)
            st.success(f"Dados do time '{time_name}' atualizados com sucesso!")

# Função para atualizar dados de um time no banco de dados
def update_time(time_name, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano):
    data.update_time(time_name, gols_sofridos, gols_marcados, pontos, vitorias, derrotas, partidas_jogadas, empates, treinador, campeonato_ano)

def change_campeonato_screen():
    st.header("Trocar de Campeonato")
    # ........................

# Função para mostrar a classificação dos times
def show_ranking():
    # Exibir dados da tabela Time
    st.header("Classificação dos Times")
    time_data = data.get_time_data()

    if time_data:
        df = pd.DataFrame(time_data, columns=["Nome", "GolsSofridos", "GolsMarcados", "Pontos", "Vitórias", "Derrotas", "PartidasJogadas", "Empates", "Treinador", "CampeonatoAno"])
        st.dataframe(df)
    else:
        st.write("Nenhum dado de time disponível.")

def main_app():
    st.title("Campeonato Brasileiro 2023")

    # Menu
    menu_option = st.sidebar.selectbox("Menu", ["Classificação", "Inserir Time", "Deletar Time", "Alterar Time", "Trocar de Campeonato"])

    if menu_option == "Classificação":
        show_ranking()
    elif menu_option == "Inserir Time":
        insert_time_screen()
    elif menu_option == "Deletar Time":
        delete_time_screen()
    elif menu_option == "Alterar Time":
        update_time_screen()
    elif menu_option == "Trocar de Campeonato":
        change_campeonato_screen()

if __name__ == "__main__":
    st.write("Executando o aplicativo...")
    main_app()
