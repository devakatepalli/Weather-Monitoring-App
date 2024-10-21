import sqlite3

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS daily_summaries
                 (city TEXT, date TEXT, avg_temp REAL, max_temp REAL, min_temp REAL, dominant_condition TEXT)''')
    conn.commit()
    conn.close()

def save_daily_summary(daily_summary):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    for city, summary in daily_summary.items():
        c.execute('''INSERT INTO daily_summaries (city, date, avg_temp, max_temp, min_temp, dominant_condition) 
                     VALUES (?, ?, ?, ?, ?, ?)''', 
                  (city, "today's_date", summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()
