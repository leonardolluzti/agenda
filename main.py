import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    menu = '0'
    while menu != '6':
        print ("=================================")
        print ("| 1 - Mostra Agenda             |")
        print ("| 2 - Buscar Contato na Agenda  |")
        print ("| 3 - Inserir Contato na Agenda |")
        print ("| 4 - Editar Contato na Agenda  |")
        print ("| 5 - Excluir Contato na Agenda |")
        print ("| 6 - Sair da Agenda            |")
        print ("=================================")
        menu = input("Digite uma opção: ")
        if menu == '1': 
            agenda.listar()
        elif menu == '2': 
            nome = input("Digite um nome: ")
            agenda.buscar(nome)            
        elif menu == '3': 
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda.inserir(nome, telefone)
        elif menu == '4': 
            agenda.listar()
            id = input("Digite o id: ")
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda.editar(nome, telefone, id)
        elif menu == '5': 
            agenda.listar()
            id = input("Digite o id do contato que deseja excluir: ")
            agenda.excluir(id)
        elif menu == '6': 
            agenda.fechar()
            print ("Saiu da Agenda!")