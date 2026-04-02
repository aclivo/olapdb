from olapdb import connect


class TestConnection:
    def test_connect(self):
        connection = connect()
        assert connection is not None
