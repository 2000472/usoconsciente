import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

'''
cur.execute("insert into dicas (titulo, conteudo1, conteudo2, conteudo3, conteudo4, conteudo5, conteudo6, conteudo7, conteudo8, conteudo9, conteudo10, conteudo11, conteudo12, conteudo13, conteudo14, conteudo15, conteudo16, conteudo17, conteudo18, conteudo19, conteudo20fonte, fontelink) values (?, ?, ?, ?)",
            ('First Post',
            'Content for the first post',
            'Fonte 1',
            'Link Fonte 1'))

cur.execute("insert into dicas (titulo, conteudo, fonte, fontelink) values (?, ?, ?, ?)",
            ('Second Post',
            'Content for the second post',
            'Fonte 2',
            'Link Fonte 2'))
'''

connection.commit()
connection.close()
