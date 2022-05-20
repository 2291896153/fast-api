from fastapi import FastAPI
import pymysql
import pandas

app = FastAPI()
db = pymysql.connect(host='192.168.3.250',
                     port=30102,
                     user='root',
                     password='123456',
                     database='cost')
sql = "SELECT * FROM kube_pod_info"


@app.get("/list_pod")
async def list_pod():
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return {results}


# if __name__ == '__main__':
#     list_pod()
