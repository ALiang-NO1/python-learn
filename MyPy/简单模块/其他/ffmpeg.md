@[TOC]
### 1. 安装ffmpeg
    sudo add-apt-repository ppa:kirillshkrogalev/ffmpeg-next 
    sudo apt-get update 
    sudo apt-get install ffmpeg

### 2. 安装ffmpy
    pip install ffmpy==0.2.2  # 需要权限就添加sudo

### 3. ffmpy简单的命令,在系统环境下执行：
    # 获取video/vvvv.mp4的视频时间
    $ ffmpeg -i video/vvvv.mp4 2>&1| grep 'Duration'| cut -d ' '-f 4| sed s/,//# 生成缩略图， 其中out%d.png 表示生成多张图片%d表示占位符
    $ ffmpeg -i video/vvvv.mp4 -f image2 -vf fps=fps=1 out%d.png
    # 生成10*10的缩略图 fps=fps=1 表示每一帧抓取一次 -y 表示同意覆盖
    $ ffmpeg -i video/vvvv.mp4 -y -f image2 -vf "fps=fps=1,scale=180*75,tile=10x10" out%d.png
    # 切TS流 video/playlist.m3u8 video/cat_output%03d.ts  ts流的存储路径，他们要在同一个文件夹下
    $ ffmpeg -i video/vvvv.mp4  -c copy -map0-y -f segment -segment_list video/playlist.m3u8 -segment_time 1-bsf:v h264_mp4toannexb   video/cat_output%03d.ts

### 4. ffmpy的简单使用
[ffmpy文档](https://ffmpy3.readthedocs.io/en/latest/)

> 其实就是将ffmpeg命令直接放入到ffmpy中， 并在命令行中执行代码
> 
### 5. python 使用ffmpy 结合ffmpeg

```python
import os
import re
import logging
from django.conf import settings
from django.core.cache import cache
from ffmpy import FFmpeg
from course.constant import VIDEOSTATE
logger = logging.getLogger(__name__)

def cut_change(video_path, out_path, out_path2, out_path3, base_path, fps_r):
    """
    操作ffmpeg执行
    :param video_path: 处理输入流视频
    :param out_path: 合成缩略图 10×10
    :param out_path2: 封面图路径
    :param out_path3: 合成Ts流和 *.m3u8文件
    :param fps_r: 对视频帧截取速度
    """
    ff = FFmpeg(inputs={video_path: None},
                outputs={out_path: '-f image2 -vf fps=fps={},scale=180*75,tile=10x10'.format(fps_r),
                         out_path2: '-y -f mjpeg -ss 0 -t 0.001',
                         None: '-c copy -map 0 -y -f segment -segment_list {0} -segment_time 1  -bsf:v h264_mp4toannexb  {1}/cat_output%03d.ts'.format(
                             out_path3, base_path),
                         })
    print(ff.cmd)
    ff.run()


def execCmd(cmd):
    """
    执行计算命令时间
    """
    r = os.popen(cmd)
    text = r.read().strip()
    r.close()
    return text


# 获取完整的上传文件路径
def has_video(video_path):
    MEDIA_DIR = settings.MEDIA_ROOT
    FULL_PATH = os.path.join(MEDIA_DIR, video_path)
    flag = False
    if os.path.exists(FULL_PATH):
        flag = True
    return flag, FULL_PATH, MEDIA_DIR


def handle_video_cut(instance):
    video_path = instance.video.name
    video_name = os.path.splitext(video_path.split('/')[-1])[0][:5]
    flag, full_path, media_path = has_video(video_path)

    base_preview_path = os.path.join(media_path, 'video_trans/preview')
    base_poster_path = os.path.join(media_path, 'video_trans/poster')
    base_path = os.path.join(media_path, 'video_trans/video_change', str(instance.id))
    # 必须先创建路径， ffmpeg不会自己创建
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    if not os.path.exists(base_poster_path):
        os.makedirs(base_poster_path)
    if not os.path.exists(base_preview_path):
        os.makedirs(base_preview_path)
    preview_path = os.path.join(base_preview_path, video_name + '{}_out.png'.format(str(instance.id)))
    poster_path = os.path.join(base_poster_path, video_name + '{}_poster.jpeg'.format(str(instance.id)))
    video_change = os.path.join(base_path, 'playlist.m3u8')

    if not flag:
        logger.info('this video_path({}) is not exists'.format(full_path))
        return None
    cmd = "ffmpeg -i {} 2>&1 | grep 'Duration' | cut -d ' ' -f 4 | sed s/,//".format(full_path)
    text = execCmd(cmd)
    search_group = re.search('(\d+):(\d+):(\d+)', text)
    if search_group:
        time_hours = int(search_group.group(1))
        time_minutes = int(search_group.group(2))
        time_seconds = int(search_group.group(3))
        all_count_seconds = time_hours * 60 * 60 + time_minutes * 60 + time_seconds
        # print(all_count_seconds)
    else:
        logger.info('this video({}) is no time'.format(full_path))
        return None

    # 因无法精确分配100分压缩图片，存在误差， 以下函数会有错误但是并不会影响结果, 会有exception
    try:
        cut_change(full_path, preview_path, poster_path, video_change, base_path, r)
    except:
        pass
    # print('change video code success')
    logger.info('change video code success and clean cache')
```

  ### 5.编码格式的转换

有的mp4格式编码不同， ts流切出来的视频卡顿无法播放， 需要将mp4视频的编码格式转换成 H264, 因为ffmpeg有对应的编码解析器h264_mp4toannexb，其它的编码格式例如：MPEG1， MPEG2， MPEG4等等，目前没有发现ffmpeg相对应的编码解析器，所以建议把.mp4的视频转换成h264的编解码器

    # 比如一个视频的编码是MPEG4，想用H264编码，咋办？ 
    ffmpeg -i input.mp4 -strict -2 -vcodec h264 output.mp4  
    #input.mp4是指要转换视频的地址；output.mp4是转化后视频的存放路径
    # 相反也一样 
    ffmpeg -i input.mp4 -strict -2 -vcodec mpeg4 output.mp4
 
**转换前**
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019030116110494.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0OTcxMTc1,size_16,color_FFFFFF,t_70)
**转换后**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190301161007302.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0OTcxMTc1,size_16,color_FFFFFF,t_70)

