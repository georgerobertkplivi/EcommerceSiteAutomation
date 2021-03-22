global url,username,password,baseURL,useremail,passw
baseURL= "http://admin-demo.nopcommerce.com"
useremail= "admin@yourstore.com"
passw= "admin"

class Configs:
    @staticmethod
    def getURL():
        url = baseURL
        return url

    @staticmethod
    def getUseremail():
        username = useremail
        return username

    @staticmethod
    def getPassword():
        password = passw
        return password