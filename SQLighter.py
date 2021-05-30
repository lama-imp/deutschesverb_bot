import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def find_verb(self, text):
        item = (text,)
        return self.cursor.execute(
            'SELECT verb FROM verben WHERE verb = ?', item
        ).fetchone()

    def give_answer(self, text):
        item = (text,)
        return self.cursor.execute(
            'SELECT * FROM verben WHERE verb = ?', item
        ).fetchone()

    def close(self):
        self.connection.close()
