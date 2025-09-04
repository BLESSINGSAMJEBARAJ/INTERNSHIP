import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        sql = """
              CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age TEXT,
    doj TEXT,
    email TEXT UNIQUE,
    gender TEXT,
    contact TEXT UNIQUE,
    address TEXT

); """
        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, name, age, doj, email, gender, contact, address):
        self.cursor.execute(
            "SELECT * FROM employees WHERE name=? AND age=? AND doj=? AND email=? AND gender=? AND contact=? AND address=?",

        (name, age, doj, email, gender, contact, address))
        existing_entry = self.cursor.fetchone()

        if existing_entry:
            print("Duplicate entry detected. No insertion performed.")
            return False

        try:
            self.cursor.execute(
                "INSERT INTO employees (name, age, doj, email, gender, contact, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (name, age, doj, email, gender, contact, address)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Duplicate email or contact. Not inserted.")
            return False

    def fetch(self):
        self.cursor.execute("select * from employees")
        row = self.cursor.fetchall()
        return row

    def remove(self, id):
        print(f"Trying to delete ID: {id}")
        self.cursor.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, age, doj, email, gender, contact, address):
        # Check if another employee already has the same details
        self.cursor.execute("""
                            SELECT *
                            FROM employees
                            WHERE name = ?
                              AND age = ?
                              AND doj = ?
                              AND email = ?
                              AND gender = ?
                              AND contact = ?
                              AND address = ?
                              AND id != ?
                            """, (name, age, doj, email, gender, contact, address, id))

        existing_entry = self.cursor.fetchone()

        if existing_entry:
            print("Duplicate update blocked.")
            return False  # Don't update if duplicate exists

        # If no duplicate, proceed with update
        self.cursor.execute("""
                            UPDATE employees
                            SET name=?,
                                age=?,
                                doj=?,
                                email=?,
                                gender=?,
                                contact=?,
                                address=?
                            WHERE id = ?
                            """, (name, age, doj, email, gender, contact, address, id))
        self.conn.commit()
        return True

        # Check if email or contact already exists (excluding the current employee)
        cursor = db.connection.cursor()  # Ensure you have a connection object
        cursor.execute("SELECT emp_id FROM employees WHERE (email=? OR contact=?) AND emp_id != ?",
                       (email, contact, emp_id))
        existing_employee = cursor.fetchone()  # Fetch one record

        if existing_employee:
            messagebox.showerror("Duplicate Entry", "Another employee with this email or contact already exists.")
            return
        # Update successful

    def sort_by(self, column_name):
        if column_name not in ["name", "age", "doj", "gender"]:
            raise ValueError("Invalid column for sorting")
        self.cursor.execute(f"SELECT * FROM employees ORDER BY {column_name} ASC")
        return self.cursor.fetchall()

