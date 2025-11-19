import tkinter as tk  # Biblioteca para criar a interface gráfica


# -----------------------------------------------
# 1) FUNÇÃO PRINCIPAL — ADICIONAR TAREFAS
# -----------------------------------------------
def adicionar_tarefa():
    texto = entrada.get()  # Pega o texto digitado pelo usuário

    if texto.strip():  # Verifica se o usuário digitou algo
        # Cria um novo checkbox (tarefa)
        var = tk.BooleanVar()  # Variável que guarda se está marcado ou não
        check = tk.Checkbutton(frame_tarefas, text=texto, variable=var, font=("Arial", 12))
        check.pack(anchor="w")  # Coloca alinhado à esquerda

        entrada.delete(0, tk.END)  # Limpa o campo de digitação


# -----------------------------------------------
# 2) CRIANDO A JANELA PRINCIPAL
# -----------------------------------------------
root = tk.Tk()
root.title("Meu Checklist")
root.geometry("400x400")


# -----------------------------------------------
# 3) CAMPO ONDE DIGITA UMA TAREFA
# -----------------------------------------------
entrada = tk.Entry(root, width=30, font=("Arial", 12))
entrada.pack(pady=10)  # Espaçamento vertical


# -----------------------------------------------
# 4) BOTÃO PARA ADICIONAR A TAREFA
# -----------------------------------------------
botao_adicionar = tk.Button(root, text="Adicionar tarefa", command=adicionar_tarefa)
botao_adicionar.pack()


# -----------------------------------------------
# 5) FRAME (área) ONDE AS TAREFAS FICAM
# -----------------------------------------------
frame_tarefas = tk.Frame(root)
frame_tarefas.pack(pady=20)


# -----------------------------------------------
# 6) LOOP PRINCIPAL DA INTERFACE
# -----------------------------------------------
root.mainloop()
