import MySQLdb, configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FabricaConexao():

    def conectar(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')

        user = config['DATABASE']['user']
        passwd = config['DATABASE']['passwd']
        db = config['DATABASE']['db']
        host = config['DATABASE']['host']
        port = int(config['DATABASE']['port'])

        engine = create_engine(f'mysql://{user}:{passwd}@{host}:{port}/{db}')

        return engine

    def criar_sessao(self):
        conexao = self.conectar()

        Session = sessionmaker()
        Session.configure(bind=conexao)
        session = Session()

        return session