import database as db
import Alunos as alunos

def incluir(alunos):
    sql = "INSERT INTO alunos (nome, cpf, data_nasc) VALUES (%s,%s,%s)"
    values = (alunos.nome, alunos.cpf, alunos.data)
    db.cursor.execute(sql, values)
    db.cnn.commit()

def status():
    db.cursor.execute("SELECT * FROM alunos")
    list = []
    for i in db.cursor.fetchall():
        list.append(alunos.Alunos(i[0],i[1],i[2],i[3]))
    return list

def update(nome, cpf, data, id):
    sql = ("UPDATE alunos SET nome = %s, cpf=%s, data_nasc=%s WHERE id = %s")
    values = (nome, cpf, data, id)
    db.cursor.execute(sql, values)
    db.cnn.commit()

def delete(id):
    sql = ("DELETE FROM alunos WHERE id = %s")
    db.cursor.execute(sql, (id,))
    db.cnn.commit()
