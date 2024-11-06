import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(key='Nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(key='Idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'), sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','Cartoes', key='aceitaCartao'),sg.Radio('Não','Cartoes',key='naoAceitaCartao')],
            [sg.Button("Enviar")],
            [sg.Output(size=(50,10), key='Output')]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário", layout)
        
        
    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.read()  
            
            if self.button == sg.WIN_CLOSED:
                break
            
            nome = self.values['Nome']
            idade = self.values['Idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            
            if not nome or not idade:
                sg.popup_error('Por favor, preencha todos os campos antes de enviar.')
                continue  # Se faltar algum campo, não processa os dados e continua aguardando

            # Limpar a área de saída antes de mostrar os dados
            self.janela['Output'].update('')
            

            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não Aceita Cartão: {nao_aceita_cartao}')
        
        self.janela.close()
        
tela = TelaPython()
tela.Iniciar()