import pandas as pd
import streamlit as st
import data
from dateutil.parser._parser import ParserError

# Funções
def calculate_points(vitorias, empates, derrotas):
    return (vitorias * 3) + empates + (derrotas * 0)

def insert_time_screen():
    # Inserir um time no banco de dados
    st.header("Inserir um Time")
    nome = st.text_input("Nome do Time")
    treinador = st.text_input("Sigla")
    vitorias = st.number_input("Vitórias", step=1)
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
        time_name, treinador, pontos, vitorias, derrotas,empates, partidas_jogadas,gols_marcados, gols_sofridos, campeonato_ano = selected_time

        # Campos de entrada para os novos valores
        new_treinador = st.text_input("Nova Sigla", treinador)
        new_vitorias = st.number_input("Novas Vitórias", vitorias,step=1)
        new_derrotas = st.number_input("Novas Derrotas", derrotas,step=1)
        new_empates = st.number_input("Novos Empates", empates,step=1)
        new_partidas_jogadas = new_derrotas + new_empates + new_vitorias
        new_gols_marcados = st.number_input("Novos Gols Marcados", gols_marcados,step=1)
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
# Função para mostrar a classificação dos times
def show_ranking():
    # Exibir dados da tabela Time
    st.header("Classificação dos Times")
    time_data = data.get_time_data()

    if time_data:
        # Criar coluna de Partidas Jogadas (J) a partir de Vitórias, Empates e Derrotas
        df = pd.DataFrame(time_data, columns=["Nome", "Sigla", "Pontos", "Vitórias", "Derrotas", "Empates", "Jogos","GolsMarcados", "GolsSofridos", "Saldo"])

        # Calcular Pontos (Pts)
        df["Pts"] = df.apply(lambda row: calculate_points(row["Vitórias"], row["Empates"], row["Derrotas"]), axis=1)

        # Reordenar as colunas
        df = df[["Nome", "Sigla", "Pontos", "Jogos", "Vitórias", "Derrotas", "Empates", "GolsMarcados", "GolsSofridos", "Saldo"]]

        # Rename the columns for better display
        df.columns = ["Nome", "Sigla", "Pts", "J", "V", "D", "E", "GP", "GC", "GS"]

        # Ordenar o DataFrame pelas colunas especificadas
        df = df.sort_values(by=["Pts", "V", "GS", "GP"], ascending=[False, False, False, False])

        # Resetar o índice para começar em 1
        df.index = df.index + 1

        st.dataframe(df)  # Não é necessário resetar o índice se você quer começar do 1

    else:
        st.write("Nenhum dado de time disponível.")


# Função de Login
def login():
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Nome de usuário")
    password = st.sidebar.text_input("Senha", type="password")
    return username, password

# Verificar credenciais
def authenticate(username, password):
    # Verificar se é o administrador (coloque suas próprias credenciais aqui)
    if username == "admin" and password == "admin":
        return "admin"
    # Verificar se é um usuário comum (coloque suas próprias credenciais aqui)
    elif username == "user" and password == "user":
        return "user"
    else:
        return None



def main_app():
    st.title("Campeonato Brasileiro 2023")

    # Realizar login
    username, password = login()
    role = authenticate(username, password)

    if role is None:
        st.error("Insira suas credenciais válidas e faça seu login.")
    else:
        # Menu lateral com botões para navegar nas funcionalidades
        option = st.sidebar.radio("Menu", ("Classificação", "Inserir Time", "Deletar Time", "Alterar Time"))

        if role == "admin":  # Somente o administrador tem acesso às funções de edição
            if option == "Inserir Time":
                insert_time_screen()
            elif option == "Deletar Time":
                delete_time_screen()
            elif option == "Alterar Time":
                update_time_screen()

        # As outras opções podem ser acessadas por ambos (usuários e administradores)
        if option == "Classificação":
            show_ranking()

if __name__ == "__main__":
    st.write("Executando o aplicativo...")
    main_app()
