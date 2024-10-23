from QA_table import QA_table

db = QA_table("postgresql://postgres:psql@localhost:5432/QA")


def test_insert():
    art = "A13"
    product = "Штаны"
    category = "Одежда"

    select_table_before = db.select()

    db.insert(art, product, category)

    select_table_after = db.select()

    db.delete(art)

    assert len(select_table_after) == len(select_table_before) + 1
    assert select_table_after[-1]["product"] == product


def test_update():
    art = "A13"
    product = "Штаны"
    category = "Одежда"
    new_product = "Джинсы"

    db.insert(art, product, category)
    select_table_before = db.select()

    db.update(new_product, art)

    select_table_after = db.select()

    db.delete(art)

    assert len(select_table_before) == len(select_table_after)
    assert select_table_after[-1]["product"] == new_product


def test_delete():
    art = "A13"
    product = "Штаны"
    category = "Одежда"

    db.insert(art, product, category)
    select_table_before = db.select()

    db.delete(art)

    select_table_after = db.select()

    assert len(select_table_after) == len(select_table_before) - 1
    assert select_table_after[-1]["art"] != art
