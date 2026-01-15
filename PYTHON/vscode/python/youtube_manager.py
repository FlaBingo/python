# import json


# def load_data():
#     try:
#         with open("yt_db.txt", "r") as file:
#             show = json.load(file)
#             return show
#     except FileNotFoundError:
#         return []
    
# def show_vid(vid):
#     for index, video in enumerate(vid, start=1):
#         print(f"{index}. {video['name']}, Duration: {video['time']} ")
    
# def save_data_helper(vid):
#     with open("yt_db.txt", "w") as file:
#         json.dump(vid, file)
    
# def add_vid(vid):
#     title = input("Enter the title: ")
#     time = input("Enter the time: ")
#     vid.append({"title":title, "time": time})
#     save_data_helper(vid)
    
# def remove():
#     pass


# def main():
#     vid = load_data()
#     while True:
#         print(f"1. Show all the Videos")
#         print(f"2. Add the new video")
#         print(f"3. Remove existing video")
#         print(f"4. update the existing video")
#         print(f"5. exit...")
#         choice = int(input("Enter the number:"))
#         match choice:
#             case 1:
#                 show_vid(vid)
#             case 2:
#                 add_vid(vid)
#             case 3:
#                 remove(vid)
#             case 4:
#                 update(vid)
#             case 5:
#                 break
#             case _:
#                 print("Invalid input...")
                
    

# if __name__ == "__main__":
#     main()

# # with open("yt_db.txt", "w") as f:
# #     f.write("Hello world!")


# import json
# I copied it 

# def load_data():
#     try:
#         with open('youtube.txt', 'r') as file:
#             test = json.load(file)
#             # print(type(test))
#             return test
#     except FileNotFoundError:
#         return []
    
# def save_data_helper(videos):
#     with open('youtube.txt', 'w') as file:
#         json.dump(videos, file)

# def list_all_videos(videos):
#     print("\n")
#     print("*" * 70)
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. {video['name']}, Duration: {video['time']} ")
#     print("*" * 70)

# def add_video(videos):
#     name = input("Enter video name: ")
#     time = input("Enter video time: ")
#     videos.append({'name': name, 'time': time})
#     save_data_helper(videos)

# def update_video(videos):
#     list_all_videos(videos)
#     index = int(input("Enter the video number to update"))
#     if 1 <= index <= len(videos):
#         name = input("Enter the new video name")
#         time = input("Enter the new video time")
#         videos[index-1] = {'name':name, 'time': time}
#         save_data_helper(videos)
#     else:
#         print("Invalid index selected")


# def delete_video(videos):
#     list_all_videos(videos)
#     index = int(input("Enter the video number to be deleted"))
    
#     if 1<= index <= len(videos):
#         del videos[index-1]
#         save_data_helper(videos)
#     else:
#         print("Invalid video index selected")


# def main():
#     videos = load_data()
#     while True:
#         print("\n Youtube Manager | choose an option ")
#         print("1. List all youtube videos ")
#         print("2. Add a youtube video ")
#         print("3. Update a youtube video details ")
#         print("4. Delete a youtube video ")
#         print("5. Exit the app ")
#         choice = input("Enter your choice: ")
#         # print(videos)

#         match choice:
#             case '1':
#                 list_all_videos(videos)
#             case '2':
#                 add_video(videos)
#             case '3':
#                 update_video(videos)
#             case '4':
#                 delete_video(videos)
#             case '5':
#                 break
#             case _:
#                 print("Invalid Choice")

# if __name__ ==  "__main__":
#     main() 

