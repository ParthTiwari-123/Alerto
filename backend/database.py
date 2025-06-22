import sqlite3 as sq3
from datetime import datetime, timezone


# Connect to DB
conn = sq3.connect("instance/alerts.db")
cursor = conn.cursor()

# 📄 View all alerts
def show_all_alerts():
    cursor.execute("SELECT * FROM Alert")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# ➕ Insert a new alert manually
def insert_alert(name, status, notes, lat, lon, contact):
    timestamp = datetime.now(timezone.utc).isoformat()
    cursor.execute("""
        INSERT INTO Alert (name, timestamp, status, notes, lat, lon, contact)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, timestamp, status, notes, lat, lon, contact))
    conn.commit()
    print("✅ New alert inserted.")

# ✅ Example usage
if __name__ == "__main__":
    print("📍 Showing existing alerts:\n")
    show_all_alerts()

    print("\n🚨 Inserting new alert...\n")
    insert_alert("Priya Mehta", "Manually Triggered", "Pressed emergency button", 28.6211, 77.3672, "+911234567891")

    print("\n📍 Updated alerts:\n")
    show_all_alerts()
    
    conn.close()