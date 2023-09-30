from crud import CRUD

registro = CRUD('db.db', 'admin', 'admin')

registro.criar('ana', 10)