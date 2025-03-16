import os
import sqlite3

db_name = "school.db"
db_full_path = os.path.join(os.getcwd(), db_name)


class Model:
    def __init__(self):
        self.table_name = self.generate_table_name()
        self.conn = sqlite3.connect(db_full_path)
        self.curr = self.conn.cursor()

    def generate_table_name(self):
        """
        Generate table name based on the file directory, file name
        """
        return self.format_name(os.getcwd().split("/")[-1] + "_" + __name__)

    def format_name(self, name: str):
        """
        Format the given name and return only alphabets and _.
        """
        new_name = ""
        for ch in name:
            if ch.isalpha() or ch == "_":
                new_name += ch
                continue

            if ch == " " or ch == "-":
                new_name += "_"

        return new_name

    def sql_execute(self, sql_cmd, return_value=None):
        """
        Execute the given sql command and optionaly return value if needed.
        """
        self.curr.execute(sql_cmd)
        self.conn.commit()

        # by default, return nothing
        if not return_value:
            return

        # if the return_value is a number, return that many results
        if isinstance(return_value, int):
            return self.curr.fetchmany(return_value)

        # the return_value can be 'one' or 'all' too
        if return_value == "one":
            return self.curr.fetchone()
        if return_value == "all":
            return self.curr.fetchall()

    def create_field(self, name):
        pass

    def create_table_if_needed(self):
        """
        Create the table in the db if it does not already exists.
        """
        self.table_creation_sql = f"CREATE TABLE IF NOT EXISTS {self.table_name}("

        self.sql_execute(self.table_creation_sql)

    def __del__(self):
        """
        Make sure to commit and close the sql connection on object deletion.
        """
        print("Destructor")
        self.conn.commit()
        self.conn.close()
