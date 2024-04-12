from moviepy.editor import VideoFileClip, concatenate_videoclips

# 视频文件路径
video_path1 = 'D:/3dgs/from_yinuo/WeChat_20240412104413.mp4'
video_path2 = 'D:/3dgs/from_yinuo/WeChat_20240412104438.mp4'

# 加载视频文件
clip1 = VideoFileClip(video_path1)
clip2 = VideoFileClip(video_path2)

# 合并视频
final_clip = concatenate_videoclips([clip1, clip2])

# 输出合并后的视频文件
output_path = 'D:/3dgs/from_yinuo/merged_video.mp4'
final_clip.write_videofile(output_path, codec='libx264')
