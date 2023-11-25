import configparser
config = configparser.RawConfigParser()
config.read(r"C:\Users\hp\Desktop\IT\Testing\Frameworks\Hybrid_framework\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def get_Application_URL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_Username():
        username1 = config.get('common info', 'username')
        return username1

    @staticmethod
    def get_Password():
        password1 = config.get('common info', 'password')
        return password1












