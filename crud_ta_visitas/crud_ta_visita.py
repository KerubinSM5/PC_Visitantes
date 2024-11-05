#CRUD executável de ta_visitas

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from util.db import SQL
#from c_projeto import IncluirProjeto

#from u_projeto import AlterarProjeto
#from d_projeto import ExcluirProjeto

class CRUDta_visita(tk.Tk):
    def __init__(self):
        super().__init__()
        # Criação de constantes
        self.PADX = 10
        self.PADY = 10

        self.title("CRUD - Tabela de Visitas")

        # Primeira linha - Título
        titulo = tk.Label(self, text="Cadastro de Projetos", font='Helvetica 16 bold', fg='blue')
        titulo.grid(row=0, column=0, columnspan=3, padx=self.PADX, pady=self.PADY)

        # Segunda linha - Parâmetro de consulta
        lb_nome = tk.Label(self, text="Nome do Projeto", font='Helvetica 12 bold', fg='blue')
        lb_nome.grid(row=1, column=0, padx=self.PADX, pady=self.PADY)

        self.nome_var = tk.StringVar()
        self.et_nome = ttk.Entry(self, textvariable=self.nome_var, font='Helvetica 16 bold', foreground='green')
        self.et_nome.grid(row=1, column=1, padx=self.PADX, pady=self.PADY)

        self.bt_consultar = tk.Button(self, text="Consultar", command=self.consultar, font='Helvetica 12 bold',
                                      fg='white', bg='blue')
        self.bt_consultar.grid(row=1, column=2, padx=self.PADX, pady=self.PADY)

        # Treeview para exibir os resultado da consulta no banco de dados
        style = ttk.Style()
        style.theme_use('clam')

        style.configure("Custom.Treeview", font=("Arial", 12), foreground="blue")
        self.tre_funcoes = ttk.Treeview(self, columns=("idt_visitantes", "nme_visitante", "rg_visitante", "dta_nascimento", "telefone","eml_visitante",
                                                       "pcd_visitante",), show="headings", style="Custom.Treeview",height=20)

        # Configurar as colunas
        self.tre_funcoes.heading("idt_visitantes", text="IDT do visitante")
        self.tre_funcoes.heading("nme_visitante", text="Nome do visitante")
        self.tre_funcoes.heading("rg_visitante", text="RG do visitante")
        self.tre_funcoes.heading("dta_nascimento", text="Data de nascimento")
        self.tre_funcoes.heading("telefone", text="Telefone") #telefone
        self.tre_funcoes.heading("eml_visitante", text="Email do visitante")#email
        self.tre_funcoes.heading("pcd_visitante", text="PCD?") #PCD
        # Ajustar a largura das colunas
        self.tre_funcoes.column("idt_visitantes", width=10)
        self.tre_funcoes.column("nme_visitante", width=150)
        self.tre_funcoes.column("rg_visitante", width=80)
        self.tre_funcoes.column("dta_nascimento", width=100)
        self.tre_funcoes.column("telefone", width=100)
        self.tre_funcoes.column("eml_visitante", width=100)
        self.tre_funcoes.column("pcd_visitante", width=20)
        self.tre_funcoes.grid(row=3, column=0, columnspan=5, padx=self.PADX, pady=self.PADY)

        super().geometry("1000x1000") #Tamanho geral da interface

        # Quarta linha com os botões de operações
        self.bt_incluir = tk.Button(self, text="Incluir", command=self.incluir, font='Helvetica 12 bold', fg='white',
                                    bg='blue')
        self.bt_incluir.grid(row=4, column=0, padx=self.PADX, pady=self.PADY)
        self.bt_alterar = tk.Button(self, text="Alterar", command=self.alterar, font='Helvetica 12 bold', fg='white',
                                    bg='blue')
        self.bt_alterar.grid(row=4, column=1, padx=self.PADX, pady=self.PADY)
        self.bt_excluir = tk.Button(self, text="Excluir", command=self.excluir, font='Helvetica 12 bold', fg='white',
                                    bg='blue')
        self.bt_excluir.grid(row=4, column=2, padx=self.PADX, pady=self.PADY)

        # Criando o objeto que irá acessar o banco de dados
        self.sql = SQL(esquema='bd_gestao_visitantes', pwd='81975907')

    def consultar(self):
        # Obter o termo de busca
        nome = self.nome_var.get()

        # Chamar a função da sua classe utilitária para buscar os registros
        cmd = ("select * from tb_visitantes where nme_visitante LIKE CONCAT('%', %s, '%') order by nme_visitante")
        funcoes = self.sql.get_list(cmd, [nome])

        self.limpar_tabela()
        for funcao in funcoes:
            self.tre_funcoes.insert("", tk.END, values=(funcao['idt_visitantes'], funcao['nme_visitante'], funcao['rg_visitante'], funcao['dta_nascimento']))

    def pegar_idt(self):
        selecao = self.tre_funcoes.selection()
        if selecao:
            linha = self.tre_funcoes.selection()[0]
            valores = self.tre_funcoes.item(linha, "values")
            return valores[0]
        else:
            return 0

    def limpar_tabela(self):
        for funcao in self.tre_funcoes.get_children():
            self.tre_funcoes.delete(funcao)

    def incluir(self):
        pass

    def alterar(self):
        pass

    def excluir(self):
        pass


if __name__ == '__main__':
    app = CRUDta_visita()
    app.mainloop()
