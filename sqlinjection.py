import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 취약한 사용자 입력
username = input("Enter username: ")

# SQL 인젝션이 가능한 취약한 코드
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)

# 결과 출력
result = cursor.fetchall()
print(result)