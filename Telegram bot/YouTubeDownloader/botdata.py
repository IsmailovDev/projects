import sqlite3
def ochirish(id = None ):
    conn = sqlite3.connect('botdata.db')

    c = conn.cursor()
    c.execute(f"""   
        delete from  botdata where rowid = {id}

    
    """)
    conn.commit()

    conn.close()
def show():
    conn = sqlite3.connect('botdata.db')

    c = conn.cursor()

      
    c.execute("""   
        select rowid ,* from botdata

    
    """)
    royxat = c.fetchall()

    for i in royxat:
        print(i)
    conn.commit()

    conn.close()
def qoshish(id = None, user_name = '' ,first_name = None, last_name = None):
    conn = sqlite3.connect('botdata.db')

    c = conn.cursor()
    c.execute("""   
        insert into botdata values(?,?,?,?)

    
    """,   (id , user_name, first_name, last_name ))
    conn.commit()

    conn.close()
def amal(id):
    conn = sqlite3.connect('botdata.db')

    c = conn.cursor()
    c.execute(f"""   
        select rowid , * from botdata where id = {id}

    
    """)
    a = c.fetchall()
    return a
    conn.commit()

    conn.close()
if amal(1468429008):
    print('salom')
else:
    print('xayr')    

show()

