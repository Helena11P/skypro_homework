from sqlalchemy import create_engine
from sqlalchemy.sql import text


class QA_table:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def select(self):
        return self.db.execute("select * from products").fetchall()

    def insert(self, art, product, category):
        insert_to_table = text(
            "insert into products (\"art\", \"product\", \"category\") values (:add_art, :add_product, :add_category)")
        return self.db.execute(
            insert_to_table, add_art=art, add_product=product, add_category=category)

    def delete(self, art):
        delete_line = text("delete from products where art = :my_art")
        self.db.execute(delete_line, my_art=art)

    def update(self, new_product, my_art):
        update_value = text(
            "update products set product = :updated_name where art = :art")
        self.db.execute(update_value, updated_name=new_product, art=my_art)
