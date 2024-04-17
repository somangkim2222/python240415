import sqlite3

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            price REAL)''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cur.execute('''INSERT INTO products (name, price) 
                            VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cur.execute('''UPDATE products 
                            SET price = ? 
                            WHERE id = ?''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cur.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cur.execute('''SELECT * FROM products''')
        rows = self.cur.fetchall()
        return rows

# 샘플 데이터 준비
sample_data = [
    ("Laptop", 1200.00),
    ("Smartphone", 800.00),
    ("Tablet", 500.00),
    ("Headphones", 100.00),
    ("Smartwatch", 300.00),
    ("Camera", 700.00),
    ("Speaker", 150.00),
    ("Printer", 250.00),
    ("Router", 80.00),
    ("Monitor", 400.00)
]

# 데이터베이스 연결
db = ProductDatabase("products.db")

# 샘플 데이터 삽입
for product in sample_data:
    db.insert_product(*product)

# 모든 제품 조회
all_products = db.select_all_products()
print("All Products:")
for product in all_products:
    print(product)

# 제품 가격 업데이트
db.update_product_price(1, 1300.00)

# 모든 제품 다시 조회
all_products = db.select_all_products()
print("\nAfter Price Update:")
for product in all_products:
    print(product)

# 제품 삭제
db.delete_product(3)

# 모든 제품 다시 조회
all_products = db.select_all_products()
print("\nAfter Deletion:")
for product in all_products:
    print(product)

# 데이터베이스 연결 종료
db.conn.close()
