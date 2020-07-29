from flask import Flask, render_template
# pip install -t <directory> flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = '<path>' ใช้ connect sqlite
# เอา path ได้จากเว็บ https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/ 

db = SQLAlchemy(app) # สร้างตัวแปล dbเพื่อเข้าถึงclass ของSQLALCHEMY

class User(db.Model):# สร้าง table ที่ชื่อ User
    """สร้าง column เพื่อเก็บ data """
    '''
    ถ้า db.Column แล้วแดง ให้เพิ่มโค้ด
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint-flask"
    ]
    ลงใน setting.json 
    
    '''
    id = db.Column(db.Integer, primary_key=True)# primary_key=True การต้องให้เป็น primarykey
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    #  unique=True  ที่ให้ข้อมูลห้ามซ้ำกัน unique=False ซ้ำกันได้
    #  nullable=True ข้อมูลเป็นค่าว่างได้ ไม่ต้องกรอกข้อมูลก็ได้   
    # nullable=False ข้อมูลห้ามเป็นค่าว่าง ต้องกรอกข้้อมล 

    def __repr__(self):# เป็น function พิเศษ ใช้ในการแสดงผลชื่อ object  ให้เป็น string
        return '<User %r>' % self.username #% self.password หรือ email ก็ได้


""" 
    วิธีสร้าง test.db ไปที่ terminal ใน program vs พิมพ์ python 
    >>> from app ##ใช้ชื่อที่เราสร้างอันนี้เราสร้างชื่อ app.py## import db
        db.create_all()

    หลังจากสร้างเสร็จ add ข้อมูลใน table 
    ตัวอย่าง
    >>> from app import User #ถ้าทำใน terminal ต้องimport class User ก่อน
    >>> admin = User(username="Peerapon Buaget", password="12341234", email="bassbuget@gmail.com")
    >>> db.session.add(admin)# คำสั่งในการแอดลง table แต่จะยังไม่ขึ้นในตาราง
    >>> db.session.commit()#คำสั่งให้ค่าที่แอดไปขึ้นในตาราง

    วิธีลบข้องมูลใน table 
    >>> db.session.delete(admin# ตัวที่เราสร้างมาเก็บ object)

    วิธีดึงข้อมูล
    # User.query.all() แสดงข้อมูลใน table ทุกตัว
    # User.query.filter_by(username="Bass Buager").first() #จะแสดงแต่ตัวที่เราค้นหา
    # User.query.get(id)  # แสดง ข้อมูลแต่ละบุคคล(by id)

"""

@app.route('/')
def home():
    """ดึงข้อมูลออกจาก database ทั้งหมด"""

    people = User.query.all()
    return render_template("home.html", people=people)# render file html และสามารถส่งค่าเข้าไปได้

@app.route('/post-details/<int:id>')#<int:id> คือการสร้าง id มารับค่า int 
def post_details(id):# อย่าลืมใส่ argument
    # แสดง ข้อมูลแต่ละบุคคล(by id)
    person = User.query.get(id)
    return render_template("post-details.html", person=person)

# สำหรับ test
@app.route('/test')
def home_test():
    name = "Bass"
    return render_template("home-test.html", name=name)# render file html และสามารถส่งค่าเข้าไปได้


@app.route('/about')
def about():
    return "Hello, Aboutpage!!!"

@app.route('/script')
def test_script():
    return render_template("test-script.html")

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True) คือการเปิดให้ เห็นerror ได้ง่ายต่อการแก้บัค 