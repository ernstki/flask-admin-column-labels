# Flask-Admin column descriptions from column comments in the database

This demo app shows how to dynamically add column descriptions and
properly-capitalized labels from the column `COMMENT`s in a MySQL database.

The `flask_admin.contrib.sqla.ModelView`'s `column_labels` property is updated
inside the `__init__` for the `TestView` class (see
[`views.py#L9`](./blob/master/views.py#L9)).

Because SQLite [doesn't seem to support][1] column `COMMENT`s in SQL, this
demo requires a running MySQL server. Set your credentials for the server in
`app.py`.

## Installation

```bash
git clone https://github.com/ernstki/flask-admin-column-labels 
cd flask-admin-column-labels

# (optional, create a virtual environment)
virtualenv venv && source venv/bin/activate

# fetch dependencies; add '--user' if not using a virtualenv
pip install -r requirements.txt

# launch app w/ optional port number (default: 5000)
python run.py  # 8080
```

## Additional configuration

The `CREATE TABLE` statement for the test database `foobar` used in the
included `app.py` looks like this:

```sql
CREATE TABLE `test` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'The unique ID for the record',
  `name` varchar(45) DEFAULT NULL COMMENT 'The name',
  `description` varchar(200) DEFAULT NULL COMMENT 'A longer description',
  PRIMARY KEY (`id`)
);
```

The `TableComment` model assumes a view is present on the server called
`v_table_comments`. You could modify the source and replace this with
a SQLAlchemy `Base` model built on top of the MySQL
`information_schema.TABLES` table, too, but in my particular case, I had the
view available, so it was easier.

The `CREATE VIEW` statement looks like this:

```sql
CREATE VIEW `v_table_comments` AS
    SELECT 
        `information_schema`.`TABLES`.`TABLE_NAME` AS `table_name`,
        `information_schema`.`TABLES`.`TABLE_COMMENT` AS `comment`
    FROM
        `information_schema`.`TABLES`
    WHERE
        (`information_schema`.`TABLES`.`TABLE_SCHEMA` = DATABASE());
```

## Additional goodies

The `ColumnProperty` model has a property called `proper_name` that will try
to properly title-case lower-case table names (joined by underscores), and
allows you to override the auto-capitalization by including something like

```
Proper name: ENCODE ID
```

anywhere in the column's comment. You can specify an arbitrary list of words
that should always be in ALL CAPS at the top of
[`models.py`](./blob/master/models.py).

[1]: https://www.sqlite.org/lang.html
