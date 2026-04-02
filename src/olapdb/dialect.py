import olapdb
from sqlalchemy.engine import default


class OlapDBDialect(default.DefaultDialect):
    name = "olapdb"
    driver = "olapdb"
    default_paramstyle = "qmark"
    supports_statement_cache = True

    @classmethod
    def dbapi(cls):
        return olapdb

    @classmethod
    def import_dbapi(cls):
        return olapdb

    def create_connect_args(self, url):
        return ([], {})
