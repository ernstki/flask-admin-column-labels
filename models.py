from sqlalchemy import Column, String, BigInteger, Integer, text
from sqlalchemy.ext.declarative import declarative_base

_NO_CAPS = ['a', 'an', 'the', 'or', 'but', 'and', 'for', 'of']
_ALL_CAPS = ['id', 'dna', 'rna', 'ebv']  # ...is cruise control for cool!

Base = declarative_base()


class TableComment(Base):
    """
    A view with the table comments for all tables in the 'databank' database,
    derived from the MySQL 'information_schema', usually not readable by
    "normal" users.
    """
    __tablename__ = 'v_table_comments'

    table_name = Column(String(64), primary_key=True)
    comment = Column(String(2048))


class ColumnProperty(Base):
    __tablename__ = 'v_column_properties'

    parent_table = Column(String(64), primary_key=True)
    name = Column(String(64), primary_key=True)
    position = Column(BigInteger, server_default=text("'0'"))
    default = Column(String)
    nullable = Column(String(3))
    max_length = Column(BigInteger)
    type = Column(String)
    key = Column(String(3))
    extra = Column(String(27))
    comment = Column(String(1024))
    _proper_name = None

    @property
    def proper_name(self):
        if self._proper_name:
            return self._proper_name

        import re
        m = re.search(r'[Pp]roper [Nn]ame: ([ \w]+)', self.comment)

        if m:
            self._proper_name = m.group(1)
            return self._proper_name

        def fixcase(word):
            if word in _ALL_CAPS:
                return word.upper()
            return word.capitalize() if word not in _NO_CAPS else word

        words = map(fixcase, self.name.split('_'))
        self._proper_name = ' '.join(words)
        return self._proper_name


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    description = Column(String(45))