# RGB_ORED_data_processing

  1. 拼接和过滤：所有RGB视频的拼接由人工进行，同时会进行视频质量的检查。
    实验室人员使用剪映软件将Sync时间前的大部分多余片段删除，并将被运动相机自动分开保存的视频片段拼接起来，保存成MP4视频文件。（命名格式为PXX-XX.mp4）
  2. 记录Sync时间点：实验人员使用剪映软件将上一步的MP4文件切割出包含Sync的片段并保存成MP3音频格式，更改.env, 修改正确地址后运行test_marktime.py进行可视化的人工频谱通量所在时间点的筛选。如图，实验员找到pattern后，手动记录每个机位视频的Sync时间（秒），并记录在ORED_Dataset/PXX/5.RGBs/clip/mark_timestamp.xlsx Excel文件内。供视频切割使用。（视频寻帧每个视频人工处理一次）
![[Image]](https://github.com/yyt1208732230/RGB_ORED_data_processing/blob/master/findSync.png)

角度输出的4组参数分别为：最大频谱通量值(前三倒序)；最大频谱通量值所在帧(前三倒序)；最大频谱通量值所在时间(前三倒序)；音频文件总帧数；
·Cam1_clipboard_far.MP4.mp3 - [18.221619 19.830189 22.338984] [523 265 522] [12.14403628  6.15328798 12.12081633] 858·

  3. 切割视频片段（按工况）：在确认timedivisionGPS时间戳文件和mark_timestamp.xlsx的Sync时间点文件无误后，运行video_division.py。脚本会根据时间戳和Sync时间点位置自动切割当前试次下的所有机位的视频，并保存成视频片段。保存至ORED_Dataset/PXX/5.RGBs/clip/路径。（视频切割每个试次人工处理一次）