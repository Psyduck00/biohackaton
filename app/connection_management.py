
from base import get_session
from base import get_log_session


class DBConncectionManager():
    def __int__(self):
        self.session = None

    def __enter__(self):
        self.session = get_session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        #
        self.session.close()


class LogDBConncectionManager():
    def __int__(self):
        self.session = None

    def __enter__(self):
        self.session = get_log_session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        #
        self.session.close()