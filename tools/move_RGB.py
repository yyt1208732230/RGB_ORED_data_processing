import os
import shutil
import csv
from moviepy.editor import VideoFileClip

# 指定要遍历的目录路径和目标目录路径
source_path = None
target_path = 'G://Real Road RGB Dataset//RGB Driving Conditions'
plist = ['P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27']
# plist = ['P04', 'P05']

csv_headers = ["trial", "condition", "camera", "filename", "frames", "resolution", "fps", "size", "duration", "Driver Group", "Comment"]

with open(target_path + "/video_info.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(csv_headers)

    for pName in plist:
        source_path = 'G://Real Road AIR Dataset//' + pName + '//5.RGBs//clip/'

        # 遍历目录下的所有文件和文件夹
        for root, dirs, files in os.walk(source_path):
            # 遍历文件列表
            for file_name in files:
                # 如果文件名以 ".mp4" 结尾
                if file_name.endswith('.mp4'):
                    # 提取视频名称和视频类型
                    video_name, video_type = os.path.splitext(file_name)
                    # 提取视频名称中的关键字
                    video_keywords = video_name.split('-')
                    # 构建目标文件夹路径
                    target_folder = os.path.join(target_path, video_keywords[-1], video_keywords[0])
                    # 创建目标文件夹
                    os.makedirs(target_folder, exist_ok=True)
                    # 构建目标文件路径
                    target_file = os.path.join(target_folder, file_name)
                    # 拷贝视频文件到目标路径
                    try:
                        shutil.copy(os.path.join(root, file_name), target_file)
                        print(f"{file_name} 拷贝成功")

                        # 获取视频信息
                        video_path = os.path.join(target_folder, file_name)
                        video_clip = VideoFileClip(video_path)
                        frames = int(video_clip.fps * video_clip.duration)
                        resolution = f"{video_clip.w}x{video_clip.h}"
                        size = os.path.getsize(video_path)
                        duration = video_clip.duration
                        
                        # 写入CSV文件
                        video_info = [video_keywords[0], video_keywords[-1], video_keywords[1], file_name, frames, resolution, video_clip.fps, size, duration, "", ""]
                        csv_writer.writerow(video_info)

                    except Exception as e:
                        print(f"{file_name} 拷贝失败: {str(e)}")
