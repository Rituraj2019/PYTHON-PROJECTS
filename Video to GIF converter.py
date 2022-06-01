from moviepy.editor import*
print('Welcome')

filename=input("Enter video file name: ")
clip=VideoFileClip("filename.mp4")
clip.write_gif("newfile.gif")