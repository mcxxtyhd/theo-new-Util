from AllModels_Sqlalchemy.dataInit import agent


class connsql:

    def __init__(self):
        # 这是数据库连接
        # self.theo = agent('218.78.23.62', '1433', 'DAS_Instance', 'rdsuser',"E5!fG7%cD4^b")
        self.theo = agent('localhost', '1433', 'TYY_Back_Data', 'sa',"123")
        # self.theo = agent('192.168.11.201', '1433', 'DataEntryStoreDatabase', 'sa',"!QAZ2wsx")
        # self.theo = agent('localhost', '3306', 'testconnectspeed', 'root',"root")
        # 加密的key
        self.key = 71593504
        # 每次处理的数据数量
        self.perNum = 100