from apip import *
app.__call__()	
def iternet_count():
        app.bytes = []
        ...   
        for i in app.list_serail_code:
            for x in range(len(app.list_serail_code)):
                app.list_serail_code[x]=','.join(str(i))
        print(app.list_serail_code)
        with open("./application.txt","rb") as f:
            list_9 = f.read().split(".")
        with open("./application-2.txt","rb") as f:
            list_10 = f.read().split(".")
        with open("./application-3.txt","rb") as f:
            list_11 = f.read().split(".")        
        N = set(app.data1)
        S = set(app.data2)
        L = set(app.data3)
        for i in app.list_serail_code:
            string = f"""
for x in itert.product({str(i)}):
    app.bytes.append(''.join(x))
    if len(app.bytes) <=6 :
        for x in self.bytes :
            with open("./application.txt","a") as f:
                print(None,x)
                f.write(x+".")
self.rash(app.bytes)
            """
            exec(string)
iternet_count()
)
iternet_count()
") as f:
                print(None,x)
                f.write(x+".")
self.rash(app.bytes)
            """
            exec(string)
iternet_count()
)
iternet_count()
