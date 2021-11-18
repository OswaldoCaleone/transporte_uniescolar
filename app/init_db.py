import sqlite3

banco = sqlite3.connect('cadastro_1.db')

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoas (nome, cpf) VALUES (?, ?)",
            
            )

cursor.execute("INSERT INTO pessoas (nome, cpf) VALUES (?, ?)",
           
            )

banco.commit()

banco.close()



