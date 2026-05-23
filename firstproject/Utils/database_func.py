from pathlib import Path
import sqlite3


BASE_PATH = Path(__file__).parent.parent
DATABASE_PATH = BASE_PATH / "Data" / "schedule.db"


conn = sqlite3.connect(DATABASE_PATH)

cursor = conn.cursor()


def Add_Schedule(
      title, content, date, time, priority, category
):
   cursor.execute("""
      INSERT INTO schedule(
                  title,
                  content, 
                  date, 
                  time, 
                  priority, 
                  category
                  )
       VALUES (?, ?, ?, ?, ?, ?) """,(
         title,
         content, 
         date, 
         time, 
         priority, 
         category
       ))
   
   conn.commit()

def load_schedule():
   cursor.execute("""SELECT * FROM schedule""")

   return cursor.fetchall()


def update_schedule(
    schedule_id,
    title,
    content,
    date,
    time,
    priority,
    category,
    completed
):

    cursor.execute("""
    UPDATE schedules

    SET
        title=?,
        content=?,
        date=?,
        time=?,
        priority=?,
        category=?,
        completed=?

    WHERE id=?
    """, (
        title,
        content,
        date,
        time,
        priority,
        category,
        completed,
        schedule_id
    ))

    conn.commit()


def delete_schedule(schedule_id):

    cursor.execute("""
    DELETE FROM schedules
    WHERE id=?
    """, (schedule_id,))

    conn.commit()