import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )               

''')
def list_vids():
    cursor.execute("SELECT * FROM   videos")
    for row in cursor.fetchall():
        print(row)
        
def add_vid(name, time):
    cursor.execute("INSERT INTO videos(name, time)VALUES (?,?)", (name,time))
    conn.commit()

def update_vid(vid_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, vid_id))
    conn.commit()
    
def delete_vid(vid_id):
    cursor.execute("DELETE FROM videos where id = ?", (vid_id))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_vids()
        elif choice =='2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_vid(name,time)
        elif choice == '3':
            vid_id = input("enter your id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_vid(vid_id, name,time)
        elif choice == '4':
            vid_id = input("enter your id to delete: ")
            delete_vid(vid_id)
        elif choice=='5':
            break
        else:
            print("INVALID CHOICE...")

    
    conn.close()
if __name__== "__main__":
    main()