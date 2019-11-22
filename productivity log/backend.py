import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , earnings integer , exercise text , study text , diet text ,coding text)")
    conn.commit()
    conn.close()

def insert(date , earnings , exercise , study , diet , coding):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , earnings , exercise , study , diet , coding))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , earnings='' , exercise='' , study='' , diet='' , coding=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR earnings=? OR exercise=? OR study=? OR diet=? OR coding=?" , (date , earnings , exercise , study , diet , coding))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
