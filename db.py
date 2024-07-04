# add_user.py

from werkzeug.security import generate_password_hash
from app import app, db,User,Signatures
import csv
def add_records():
    with app.app_context():
        with open("APT_SIGNS.csv",'r') as csv_file:
            reader = list(csv.reader(csv_file))
            reader = reader[1:]
            for r in reader:
                rec = Signatures(name=r[0],type=r[1],apt=r[2],signature=r[3])
                db.session.add(rec)
                db.session.commit()
        print("Records added")

if __name__ == '__main__':
    add_records()
