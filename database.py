import sqlite3


class DBHelper  :
    def __init__(self, dbname="databases.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS events(name text, description text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_evitem_name(self, eventn_text):
        stmt = "INSERT INTO events(name) VALUES(?)"
        args = (eventn_text, )
        # more bindings supllied problem
        self.conn.execute(stmt, args)
        self.conn.commit()

    def add_evitem_description(self, eventd_text):
        # stmt = "INSERT INTO events(description) VALUES(?)"
        # stmt = "SELECT last_insert_rowid()"
        # self.conn.execute(stmt)
        # stmt = "INSERT INTO events(description) VALUES(?)"
        stmt = "UPDATE events SET description = (?) where rowid = last_insert_rowid()"
        args = (eventd_text, )
        # more bindings supllied problem
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, eventn_text):
        # stmt = "DELETE FROM items WHERE description = (?)"
        stmt = "DELETE FROM events WHERE name = (?)"
        args = (eventn_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_evitem_name(self):
        # stmt = "SELECT description FROM items"
        stmt = "SELECT name FROM events"
        return [x[0] for x in self.conn.execute(stmt)]
        # stmt = "SELECT * FROM events"
        # self.conn.execute(stmt)
        # rows = self.conn.fetchall()
        # for row in rows:
        #     return (f"{row[0]} {row[1]} {row[2]}")
    def get_evitem_description(self):
        # stmt = "SELECT description FROM items"
        stmt = "SELECT description FROM events"
        return [x[0] for x in self.conn.execute(stmt)]
