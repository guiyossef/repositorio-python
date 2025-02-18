import customtkinter
import mysql.connector
from mysql.connector import Error

# Configurações de aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Função para simular o login e enviar os dados ao banco de dados
def clique():
    email = entry_email.get()  # Obtém o valor do campo email
    senha = entry_senha.get()  # Obtém o valor do campo senha

    # Verifica se os campos não estão vazios
    if email and senha:
        try:
            # Tenta conectar ao banco de dados
            db = mysql.connector.connect(
                host="localhost",
                user="root",   # Alterar conforme o seu usuário MySQL
                passwd="",     # Colocar a senha, se houver
                database="logindb"
            )

            # Verifica se a conexão foi bem-sucedida
            if db.is_connected():
                cursor = db.cursor()

                # Insere os dados do login no banco de dados
                insert_query = "INSERT INTO login (login_email, login_senha) VALUES (%s, %s)"
                cursor.execute(insert_query, (email, senha))
                db.commit()  # Salva a transação no banco de dados

                label_resultado.configure(text=f"Dados enviados para o banco de dados!\nEmail: {email}")
                
                # Fecha o cursor e a conexão com o banco
                cursor.close()
                db.close()
        except Error as e:
            label_resultado.configure(text=f"Erro ao conectar ao banco de dados: {e}")
    else:
        label_resultado.configure(text="Erro: Campos de email e senha devem ser preenchidos!")

# Função para limpar o texto de placeholder
def limpar_placeholder(entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")

# Função para restaurar o texto de placeholder se o campo estiver vazio
def restaurar_placeholder(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)

# Criação da janela principal
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Tela de Login")

# Título
texto_titulo = customtkinter.CTkLabel(janela, text="Login", font=("Arial", 24))
texto_titulo.pack(padx=10, pady=20)

# Texto de placeholder
email_placeholder = "Digite seu email"
senha_placeholder = "Digite sua senha"

# Campo de email
entry_email = customtkinter.CTkEntry(janela, width=300)
entry_email.insert(0, email_placeholder)  # Insere o texto de exemplo como placeholder
entry_email.pack(padx=10, pady=10)

# Adiciona evento de clique para limpar o texto
entry_email.bind("<FocusIn>", lambda event: limpar_placeholder(entry_email, email_placeholder))
entry_email.bind("<FocusOut>", lambda event: restaurar_placeholder(entry_email, email_placeholder))

# Campo de senha
entry_senha = customtkinter.CTkEntry(janela, show="*", width=300)
entry_senha.insert(0, senha_placeholder)  # Insere o texto de exemplo como placeholder
entry_senha.pack(padx=10, pady=10)

# Adiciona evento de clique para limpar o texto
entry_senha.bind("<FocusIn>", lambda event: limpar_placeholder(entry_senha, senha_placeholder))
entry_senha.bind("<FocusOut>", lambda event: restaurar_placeholder(entry_senha, senha_placeholder))

# Botão de login
botao_login = customtkinter.CTkButton(janela, text="Login", command=clique)
botao_login.pack(padx=10, pady=20)

# Label para mostrar o resultado do login
label_resultado = customtkinter.CTkLabel(janela, text="", font=("Arial", 14), text_color="white")
label_resultado.pack(padx=10, pady=10)

# Inicia a janela
janela.mainloop()