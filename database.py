import sqlalchemy as sqla
import database

CONNECTION_STRING = "mysql+pymysql://is61-3:agt2ge8r@192.168.3.111/aaa"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connaction = self.engine.connect()

    def translate_to_dict(self, result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())    
        return result
    
    def get_patients(self):
        query = sqla.text("SELECT * FROM patients")
        result_raw = self.connaction.execute(query).all()
        return self.translate_to_dict(result_raw)
    
    def del_patients(self,id):
        query = sqla.text("DELETE FROM patients WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        self.connaction.execute(query)
        self.connaction.commit()      

    def add_patients(self, name):
        query = sqla.text("INSERT INTO patients (name) VALUES (:name) ")
        query = query.bindparams(sqla.bindparam("name", name))
        self.connaction.execute(query)
        self.connaction.commit() 

    def edit_patients(self, name, id):
        query = sqla.text("UPDATE patients SET name = :name WHERE id = :id")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("id", id))
        self.connaction.execute(query)
        self.connaction.commit()


   
  
    
if __name__ == "__main__":
    db = Database()
    print(db.get_patients())