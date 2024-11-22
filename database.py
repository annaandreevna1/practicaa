import sqlalchemy as sqla
import database
 
CONNECTION_STRING = "mysql+pymysql://is61-3:agt2ge8r@192.168.3.111/aaa"
 
class Database():
    def __init__(self, ):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connection = self.engine.connect()

 
    def translate_to_dict(self, result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())    
        return result
    
    def get_patients(self):
        query = sqla.text("SELECT * FROM patients")
        result_raw = self.connection.execute(query).all()
        return self.translate_to_dict(result_raw)
    
    def del_patients(self,id):
        query = sqla.text("DELETE FROM patients WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()      
 
    def add_patients(self, name, firstname, otchestvo, day_births, gender, address, phone_number, date_of_receipt, time_of_receipt):
        query = sqla.text("""
            INSERT INTO aaa.patients 
            (name, firstname, otchestvo, day_births, gender, address, phone_number, date_of_receipt, time_of_receipt)
            VALUES (:name, :firstname, :otchestvo, :day_births, :gender, :address, :phone_number, :date_of_receipt, :time_of_receipt)
        """)
        query = query.bindparams(
            sqla.bindparam("name", name),
            sqla.bindparam("firstname", firstname),
            sqla.bindparam("otchestvo", otchestvo),
            sqla.bindparam("day_births", day_births),
            sqla.bindparam("gender", gender),
            sqla.bindparam("address", address),
            sqla.bindparam("phone_number", phone_number),
            sqla.bindparam("date_of_receipt", date_of_receipt),
            sqla.bindparam("time_of_receipt", time_of_receipt)
        )
    
        self.connection.execute(query)
        self.connection.commit() 
 
    def edit_patients(self, name, id):
        query = sqla.text("UPDATE patients SET name = :name WHERE id = :id")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
    
if __name__ == "__main__":
    db = Database()
    print(db.get_patients())
    db.close()