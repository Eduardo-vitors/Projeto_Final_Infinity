# Programação De um sistema de controle de acesso para Empresa Wayne Enterprises
#Autor: EDUARDO VITOR (KEDU)
#JULHO 2024

# Biblioteca do Tkinter 
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
# Importando as configurações que a tela vai ter 
import config_tela as conf
# importando o Banco de dados para usar.
from banco_dados import SistemaDeGerenciamento


class AppMenu:
    def __init__(self,jan):
        # Inicia o Banco de dados.
        self.sistema = SistemaDeGerenciamento()
        self.usuario_tipo = None
        #Gerenciamento de telas, Onde decidi o nome da tela, o tamanho e a posição que ela estará
        self.janela = jan
        self.janela.title('Wayne Enterprises')
        self.janela.geometry('1000x600+300+100')
        self.janela.config(bg=conf.corBgTela,padx=5,pady=5)

        # Frame para a página do  login
        self.frmLogin = tk.Frame(self.janela,width=100)
        self.frmLogin.pack(side='top', padx=300, pady=3)
        self.telaLogin()

    # Método para exibir tela de login
    def telaLogin(self):
        self.imgLogo = tk.PhotoImage(file=conf.imgLogo2).subsample(2,2)
        lbLogo = tk.Label(self.frmLogin, image=self.imgLogo)
        lbLogo.pack()

        self.frmLogin.config(bg='grey')  # Alterando o background do frame para cinza

        # Frame interno para centralizar os widgets
        frmInterno = tk.Frame(self.frmLogin, bg='grey')
        frmInterno.pack(expand=True)
        # O Titulo da página
        lbTitulo = tk.Label(frmInterno, text='Login', padx=20, font=conf.fonteTitulo, bg='grey')
        lbTitulo.pack(pady=20)
        # Aonde os usuários irão digitar
        lbNomeUsuario = tk.Label(frmInterno, text='Nome:', font=conf.fonte2, bg='grey')
        lbNomeUsuario.pack(pady=10)
        self.entNomeUsuario = tk.Entry(frmInterno, width=30, font=conf.fonte2, bg='grey')
        self.entNomeUsuario.pack(pady=10)

        lbsenhaUsuario = tk.Label(frmInterno, text='Senha:', font=conf.fonte2, bg='grey')
        lbsenhaUsuario.pack(pady=10)
        self.entsenhaUsuario = tk.Entry(frmInterno, width=30, font=conf.fonte2, bg='grey')
        self.entsenhaUsuario.pack(pady=10)
        # Botão para ir para página seguinte
        btLogin = tk.Button(frmInterno, text='Login', command=self.tratarLogin,
                            width=10, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btLogin.pack(pady=10)
        
    # Método para tratar o login do usuário
    def tratarLogin(self):
        usuario_senha = self.entsenhaUsuario.get()
        nome = self.entNomeUsuario.get()
        self.usuario_tipo = self.sistema.autenticar_usuario(usuario_senha, nome)
        if self.usuario_tipo:
            self.mostrarMenu()
        else:
            msg.showwarning('Erro', 'Usuário não encontrado!')
    # metodo para aparecer o menu
    def mostrarMenu(self):
        self.frmLogin.pack_forget() 
             # Frame do Menu ----------------------------------
        self.frmMenu = tk.Frame(self.janela,width=180)
        self.frmMenu.pack(side='left',padx=3,pady=3)
        # logotipo
        if self.usuario_tipo == 'admin':
            self.imgLogo = tk.PhotoImage(file=conf.imgLogo3).subsample(2,2)
            lbLogo = tk.Label(self.frmMenu, image=self.imgLogo)
            lbLogo.pack()
        else:
            self.imgLogo = tk.PhotoImage(file=conf.imgLogo).subsample(2,2)
            lbLogo = tk.Label(self.frmMenu, image=self.imgLogo)
            lbLogo.pack()
        # titulo
        lbTitulo = tk.Label(self.frmMenu,text='Menu',padx=20,font=conf.fonteTitulo)
        lbTitulo.pack(pady=10)

        # opção "Incluir funcionarios" do menu
        btIncluir = tk.Button(self.frmMenu,text='Incluir Usuários',command=self.telaIncUsuario,
                            width=conf.btLargura,font=conf.fonte2,bg=conf.corBgBotao,fg=conf.corFonteBotao)
        btIncluir.pack(pady=10)

        # opção "incluir recursos" do menu
        btExcluir = tk.Button(self.frmMenu,text='Incluir Recursos',command=self.telaIncRecurso,
                            width=conf.btLargura,font=conf.fonte2,bg=conf.corBgBotao,fg=conf.corFonteBotao)
        btExcluir.pack(pady=10)

        # opção "Consultar recursos" do menu
        btConTodos = tk.Button(self.frmMenu,text='Consultar Recursos',command=self.telaConRecursos,
                            width=conf.btLargura,font=conf.fonte2,bg=conf.corBgBotao,fg=conf.corFonteBotao)
        btConTodos.pack(pady=10)
           # opção "Consultar recursos" do menu
        btsaida = tk.Button(self.frmMenu,text='Logout',command=self.reiniciar,
                            width=conf.btLargura,font=conf.fonte2,bg=conf.corBgBotao,fg=conf.corFonteBotao)
        btsaida.pack(pady=10)
        # opção de encerramento da app
        btFim = tk.Button(self.frmMenu,text='Encerrar',command=self.encerramento,
                            width=conf.btLargura,font=conf.fonte2,bg=conf.corBgBotao,fg=conf.corFonteBotao)
        btFim.pack(pady=10)
   
        # Frame do Conteúdo 
        self.frmConteudo = tk.Frame(self.janela,width=900,height=552,
                                    bg='white') 
        self.frmConteudo.pack(side='right',padx=6,pady=3)
    # limpar o Frame para poder ocorrer a substituição de informação na tela
    def limparFrame(self,frame):
        for elemento in frame.winfo_children():
            elemento.destroy()
    # A tela de conteúdo sobre incluir usuário
    def telaIncUsuario(self):
        # só deixa o Administrador e o gerente entrar nessa área
        if self.usuario_tipo == 'funcionario':
            msg.showwarning('Erro', 'Apenas administradores e gerentes podem incluir usuários!')
            return
        self.limparFrame(self.frmConteudo)
        # Titulo da página
        lbTituloTela = tk.Label(self.frmConteudo, text='Inclusão de Usuário', font=conf.fonteTitulo)
        lbTituloTela.place(x=120, y=10)
        # Lugar onde usuário irá digitar
        lbNomeUsuario = tk.Label(self.frmConteudo, text='Nome:', font=conf.fonte2)
        lbNomeUsuario.place(x=10, y=100)
        entNomeUsuario = tk.Entry(self.frmConteudo, width=30, font=conf.fonte2)
        entNomeUsuario.place(x=120, y=100)

        lbsenha = tk.Label(self.frmConteudo, text='Senha:', font=conf.fonte2)
        lbsenha.place(x=10, y=150)
        entsenha = tk.Entry(self.frmConteudo, width=30, font=conf.fonte2)
        entsenha.place(x=120, y=150)
        # Aonde ocorre a escolha do Tipo 
        lbTipoUsuario = tk.Label(self.frmConteudo, text='Tipo:', font=conf.fonte2)
        lbTipoUsuario.place(x=10, y=200)
        entTipoUsuario = tk.StringVar()
        tpFuncionario = tk.Radiobutton(self.frmConteudo, text='Funcionário', variable=entTipoUsuario, value='funcionario')
        tpFuncionario.place(x=120, y=200)
        tpGerente = tk.Radiobutton(self.frmConteudo, text='Gerente', variable=entTipoUsuario, value='gerente')
        tpGerente.place(x=240, y=200)
        tpAdmin = tk.Radiobutton(self.frmConteudo, text='Admininstrador', variable=entTipoUsuario, value='admin')
        tpAdmin.place(x=360, y=200)
        # Aonde ocorre o salvamentos de Dados para poder passar para o Banco de Dados e a renicialização das variaveis.
        def funTrataIncluirUsuario():
            nome = entNomeUsuario.get()
            senha = entsenha.get()
            tipo = entTipoUsuario.get()
            if nome and tipo and senha:
                self.sistema.adicionar_usuario(nome,senha,tipo)
                msg.showinfo('Sucesso', 'Usuário adicionado com sucesso')
                entNomeUsuario.delete(0, tk.END)
                entsenha.delete(0, tk.END)
                entTipoUsuario.set('')
            else:
                msg.showwarning('Erro', 'Preencha todos os campos!')
        #Botão paa confirmar a inclusão de um usuario novo e a visualização a partir das funções que está no "command"
        btIncluirUsuario = tk.Button(self.frmConteudo, text='Incluir', command=funTrataIncluirUsuario,
                                     width=20, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btIncluirUsuario.place(x=100, y=250)

        btMostrarUsuario = tk.Button(self.frmConteudo, text='Visualizar Lista', command=self.listaFuncionario,
                                     width=20, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btMostrarUsuario.place(x=300, y=250)
    # listar funcionarios e a comunicação com o Banco de Dados, só os administradores podem entrar  
    def listaFuncionario(self):
            if self.usuario_tipo != 'admin':
                msg.showwarning('Erro', 'Apenas administradores podem incluir recursos!')
                return
            self.limparFrame(self.frmConteudo)
            lbTituloTela2 = tk.Label(self.frmConteudo, text='Consulta de Funcionários', font=conf.fonteTitulo)
            lbTituloTela2.place(x=110, y=10)

            colunas2 = ('id', 'nome', 'senha', 'tipo')
            quadro2 = ttk.Treeview(self.frmConteudo, columns=colunas2, show='headings', height=18)
            quadro2.column('id', anchor=tk.CENTER, width=50)
            quadro2.heading('id', text='Id')
            quadro2.column('nome', anchor='w', width=150)
            quadro2.heading('nome', text='Nome do Funcionário')
            quadro2.column('senha', anchor=tk.CENTER, width=150)
            quadro2.heading('senha', text='Senha')
            quadro2.column('tipo',anchor=tk.CENTER, width=150)
            quadro2.heading('tipo', text='Tipo')
            # carrega os dados do Banco de dados e depois organizar na tabela.
            def carregar_dados1():
                nonlocal quadro2
                for rec in self.sistema.listar_funcionario():
                    if rec[3] =='admin':
                        quadro2.insert('', tk.END, values=(rec[0],rec[1],rec[2],'Administrador', ''))
                    else:
                        quadro2.insert('', tk.END, values=(*rec, ''))

            carregar_dados1()
            # Retornar para a página de inclusão de usuários novos
            btreturn = tk.Button(self.frmConteudo, text='Retornar', command=self.telaIncUsuario,
                                  width=15, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
            btreturn.place(x=388, y=460)

            quadro2.place(x=30, y=70)
     # Método para exibir tela de inclusão de recurso
    def telaIncRecurso(self):
        if self.usuario_tipo != 'admin':
            msg.showwarning('Erro', 'Apenas administradores podem incluir recursos!')
            return

        self.limparFrame(self.frmConteudo)
        lbTituloTela = tk.Label(self.frmConteudo, text='Inclusão de Recurso', font=conf.fonteTitulo)
        lbTituloTela.place(x=120, y=10)

        lbNomeRecurso = tk.Label(self.frmConteudo, text='Nome:', font=conf.fonte2)
        lbNomeRecurso.place(x=10, y=100)
        entNomeRecurso = tk.Entry(self.frmConteudo, width=30, font=conf.fonte2)
        entNomeRecurso.place(x=120, y=100)

        lbTipoRecurso = tk.Label(self.frmConteudo, text='Tipo:', font=conf.fonte2)
        lbTipoRecurso.place(x=10, y=150)
        entTipoRecurso = tk.StringVar()
        tpEquipamento = tk.Radiobutton(self.frmConteudo, text='Equipamento', variable=entTipoRecurso, value='equipamento')
        tpEquipamento.place(x=120, y=150)
        tpVeiculo = tk.Radiobutton(self.frmConteudo, text='Veículo', variable=entTipoRecurso, value='veiculo')
        tpVeiculo.place(x=240, y=150)
        tpDispositivo = tk.Radiobutton(self.frmConteudo, text='Dispositivo de Segurança', variable=entTipoRecurso, value='dispositivo')
        tpDispositivo.place(x=360, y=150)
        # Aonde ocorre o salvamentos de Dados para poder passar para o Banco de Dados e a renicialização das variaveis.
        def funTrataIncluirRecurso():
            nome = entNomeRecurso.get()
            tipo = entTipoRecurso.get()
            if nome and tipo:
                self.sistema.adicionar_recurso(nome, tipo)
                msg.showinfo('Sucesso', 'Recurso adicionado com sucesso')
                entNomeRecurso.delete(0, tk.END)
                entTipoRecurso.set('')
            else:
                msg.showwarning('Erro', 'Preencha todos os campos!')
        # Botão para incluir Recursos
        btIncluirRecurso = tk.Button(self.frmConteudo, text='Incluir', command=funTrataIncluirRecurso,
                                     width=20, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btIncluirRecurso.place(x=200, y=200)

    # Método para exibir tela de consulta de recursos
    def telaConRecursos(self):
        self.limparFrame(self.frmConteudo)
        lbTituloTela = tk.Label(self.frmConteudo, text='Consulta de Recursos', font=conf.fonteTitulo)
        lbTituloTela.place(x=120, y=10)
        # organiza a tabela 
        colunas = ('id', 'nome', 'tipo')
        quadro = ttk.Treeview(self.frmConteudo, columns=colunas, show='headings', height=18)
        quadro.column('id', anchor=tk.CENTER, width=50)
        quadro.heading('id', text='Id')
        quadro.column('nome', anchor='w', width=150)
        quadro.heading('nome', text='Nome do Recurso')
        quadro.column('tipo', anchor=tk.CENTER, width=150)
        quadro.heading('tipo', text='Tipo')
        # carrega os dados do Banco de dados e depois organizar na tabela.
        def carregar_dados2():
            nonlocal quadro
            for rec in self.sistema.listar_recursos():
                quadro.insert('', tk.END, values=(*rec, ''))

        carregar_dados2()
        # Aonde se comunica com o banco de dados para remover Recursos só o administrador pode usar
        def remover_recurso():
            if self.usuario_tipo != 'admin':
                msg.showwarning('Erro', 'Apenas administradores podem remover recursos!')
                return
            item_selecionado = quadro.focus()
            if item_selecionado:
                recurso_id = quadro.item(item_selecionado, 'values')[0]
                self.sistema.remover_recurso(recurso_id)
                quadro.delete(item_selecionado)
        # Aonde se comunica com o banco de dados para atualizar Recursos só o administrador pode usar
        def tela_atualiza_recurso():
            if self.usuario_tipo != 'admin':
                msg.showwarning('Erro', 'Apenas administradores podem atualizar recursos!')
                return
            item_selecionado = quadro.focus()
            if item_selecionado:
                recurso_id = quadro.item(item_selecionado, 'values')[0]
                self.telaAtualizaRecurso(recurso_id)
        #Botões para Remover e Atualizar
        btRemover = tk.Button(self.frmConteudo, text='Remover', command=remover_recurso,
                              width=15, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btRemover.place(x=400, y=70)

        btAtualizar = tk.Button(self.frmConteudo, text='Atualizar', command=tela_atualiza_recurso,
                                width=15, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btAtualizar.place(x=400, y=120)

        quadro.place(x=30, y=70)

    # Método para exibir tela de atualização de um recurso específico
    def telaAtualizaRecurso(self, recurso_id):
        self.limparFrame(self.frmConteudo)
        lbTituloTela = tk.Label(self.frmConteudo, text='Atualização de Recurso', font=conf.fonteTitulo)
        lbTituloTela.place(x=120, y=10)

        lbNomeRecurso = tk.Label(self.frmConteudo, text='Nome:', font=conf.fonte2)
        lbNomeRecurso.place(x=10, y=100)
        entNomeRecurso = tk.Entry(self.frmConteudo, width=30, font=conf.fonte2)
        entNomeRecurso.place(x=120, y=100)

        lbTipoRecurso = tk.Label(self.frmConteudo, text='Tipo:', font=conf.fonte2)
        lbTipoRecurso.place(x=10, y=150)
        entTipoRecurso = tk.StringVar()
        tpEquipamento = tk.Radiobutton(self.frmConteudo, text='Equipamento', variable=entTipoRecurso, value='equipamento')
        tpEquipamento.place(x=120, y=150)
        tpVeiculo = tk.Radiobutton(self.frmConteudo, text='Veículo', variable=entTipoRecurso, value='veiculo')
        tpVeiculo.place(x=240, y=150)
        tpDispositivo = tk.Radiobutton(self.frmConteudo, text='Dispositivo De Segurança', variable=entTipoRecurso, value='dispositivo')
        tpDispositivo.place(x=360, y=150)
        #Aonde pega as informações para atualizar no banco de dados
        def funTrataAtualizar():
            nome = entNomeRecurso.get()
            tipo = entTipoRecurso.get()
            if nome and tipo:
                self.sistema.atualizar_recurso(recurso_id, nome, tipo)
                msg.showinfo('Sucesso', 'Recurso atualizado com sucesso')
            else:
                msg.showwarning('Erro', 'Preencha todos os campos!')

        btAtualizarRecurso = tk.Button(self.frmConteudo, text='Atualizar', command=funTrataAtualizar,
                                       width=20, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btAtualizarRecurso.place(x=100, y=200)
        #Botão que retornar para a tabela de Recursos
        btreturn = tk.Button(self.frmConteudo, text='Retornar', command=self.telaConRecursos,
                                  width=20, font=conf.fonte2, bg=conf.corBgBotao, fg=conf.corFonteBotao)
        btreturn.place(x=300, y=200)

    #Renicia para o Login
    def reiniciar(self):
         self.janela.destroy()
         
         janela = tk.Tk()
         app = AppMenu(janela)
         janela.mainloop()   

      # Método para encerrar a aplicação
    def encerramento(self):
        self.janela.destroy()
        
if __name__ == "__main__":
    janela = tk.Tk()
    app = AppMenu(janela)
    janela.mainloop()
