from pathlib import Path
import sqlite3


BASE_PATH = Path(__file__).parent.parent
DATABASE_PATH = BASE_PATH / "Data" / "schedule.db"


conn = sqlite3.connect(DATABASE_PATH)

cursor = conn.cursor()



def load_schedule():
   cursor.execute("""SELECT * FROM schedules""")

   return cursor.fetchall()



def update_schedule( schedule_id, title, content, date, time, priority, category, completed
):

    cursor.execute("""
    UPDATE schedules

    SET
        title=?,content=?,date=?,time=?,priority=?,category=?,completed=?

    WHERE id=?
    """, (
        title, content, date, time, priority, category, completed, schedule_id
    ))

    conn.commit()

def create_schedule_db(title, content, date, time, priority, category, completed):
    cursor.execute("""
    INSERT INTO schedules (
        title, content, date, time, priority, category, completed
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, content, date, time, priority, category, completed))

    conn.commit()



def save_schedule(schedule_id, title, content, date, time, priority, category, completed):

    if schedule_id is None:
        
        create_schedule_db(title, content, date, time, priority, category, completed)
        

    else:
      
        update_schedule(schedule_id, title, content, date, time, priority, category, completed)
        






def delete_schedule(schedule_id):

    cursor.execute("""
    DELETE FROM schedules
    WHERE id=?
    """, (schedule_id,))

    conn.commit()