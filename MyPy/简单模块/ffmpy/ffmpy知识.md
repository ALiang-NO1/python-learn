## 格式转换
最简单的用法示例是将媒体从一种格式转换为另一种格式（在这种情况下，是从MPEG传输流转换为MP4），并保留所有其他属性：
```
>>> from ffmpy3 import FFmpeg
... ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.mp4': None}
... )
>>> ff.cmd
'ffmpeg -i input.ts output.mp4'
>>> ff.run()
```

## 转码
如果同时我们想使用不同的编解码器重新编码视频和音频，则必须指定其他输出选项：
```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.mp4': '-c:a mp2 -c:v mpeg2video'}
... )
>>> ff.cmd
'ffmpeg -i input.ts -c:a mp2 -c:v mpeg2video output.mp4'
>>> ff.run()
```

## 解复用
一个更复杂的用法示例是将MPEG传输流多路分解为单独的基本（音频和视频）流，并将其保存在保留编解码器的MP4容器中（请注意，列表在此处用于选项的方式）：
```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={
...         'video.mp4': ['-map', '0:0', '-c:a', 'copy', '-f', 'mp4'],
...         'audio.mp4': ['-map', '0:1', '-c:a', 'copy', '-f', 'mp4']
...     }
... )
>>> ff.cmd
'ffmpeg -i input.ts -map 0:1 -c:a copy -f mp4 audio.mp4 -map 0:0 -c:a copy -f mp4 video.mp4'
>>> ff.run()
```
**注意**：_不可能将选项的表达式格式混合在一起，即，不可能有包含带空格的字符串的列表（这是Complex Command Lines的一个例外）。例如，_
如：
```
>>> from subprocess import PIPE
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={
...         'video.mp4': ['-map 0:0', '-c:a copy', '-f mp4'],
...         'audio.mp4': ['-map 0:1', '-c:a copy', '-f mp4']
...     }
... )
>>> ff.cmd
'ffmpeg -hide_banner -i input.ts "-map 0:1" "-c:a copy" "-f mp4" audio.mp4 "-map 0:0" "-c:a copy" "-f mp4" video.mp4'
>>>
>>> ff.run(stderr=PIPE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/ay/projects/personal/ffmpy3/ffmpy3.py", line 104, in run
    raise FFRuntimeError(self.cmd, ff_command.returncode, out[0], out[1])
ffmpy3.FFRuntimeError: `ffmpeg -hide_banner -i input.ts "-map 0:1" "-c:a copy" "-f mp4" audio.mp4 "-map 0:0" "-c:a copy" "-f mp4" video.mp4` exited with status 1

STDOUT:

STDERR:
Unrecognized option 'map 0:1'.
Error splitting the argument list: Option not found
```

## 多路复用
要通过重新编码将视频和音频多路复用回MPEG传输流，请执行以下操作：
```
>>> ff = FFmpeg(
...     inputs={'video.mp4': None, 'audio.mp3': None},
...     outputs={'output.ts': '-c:v h264 -c:a ac3'}
... )
>>> ff.cmd
'ffmpeg -i audio.mp4 -i video.mp4 -c:v h264 -c:a ac3 output.ts'
>>> ff.run()
```
在某些情况下，必须保留输入和输出的顺序（例如，使用FFmpeg -map选项时）
在这些情况下，无法使用常规的Python词典，因为它不保留顺序。而是使用OrderedDict。
例如，我们想将一个视频和两个音频流多路复用到一个MPEG传输流中，从而使用不同的编解码器对两个音频流进行重新编码。
在这里，我们使用OrderedDict保留输入的顺序，以便它们与输出选项中流的顺序匹配：
```
>>> from collections import OrderedDict
>>> inputs = OrderedDict([('video.mp4', None), ('audio_1.mp3', None), ('audio_2.mp3', None)])
>>> outputs = {'output.ts', '-map 0 -c:v h264 -map 1 -c:a:0 ac3 -map 2 -c:a:1 mp2'}
>>> ff = FFmpeg(inputs=inputs, outputs=outputs)
>>> ff.cmd
'ffmpeg -i video.mp4 -i audio_1.mp3 -i audio_2.mp3 -map 0 -c:v h264 -map 1 -c:a:0 ac3 -map 2 -c:a:1 mp2 output.ts'
>>> ff.run()
```

## 使用 pip 协议
ffmpy3可以从读取输入STDIN或将输出写入STDOUT。这可以通过使用FFmpeg管道协议来实现。
以下示例从包含RGB格式的原始视频帧的文件中读取数据，并将其传递给ffmpy3on STDIN；ffmpy3反过来将编码原始帧数据
与H.264和输出传递到MP4容器包装它STDOUT（请注意，您必须重定向STDOUT使用过程中管道的subprocess.PIPE作为stdout值，否则输出会迷路）：
```
>>> import subprocess
>>> ff = FFmpeg(
...     inputs={'pipe:0': '-f rawvideo -pix_fmt rgb24 -s:v 640x480'},
...     outputs={'pipe:1': '-c:v h264 -f mp4'}
... )
>>> ff.cmd
'ffmpeg -f rawvideo -pix_fmt rgb24 -s:v 640x480 -i pipe:0 -c:v h264 -f mp4 pipe:1'
>>> stdout, stderr = ff.run(input_data=open('rawvideo', 'rb').read(), stdout=subprocess.PIPE)
```

## 异步执行
在某些情况下，可能不希望FFmpeg在等待结果时运行或阻塞，也不会在自己的应用程序中引入多线程。在这种情况下，asyncio可以使用异步执行。
```
>>> ff = ffmpy3.FFmpeg(
...     inputs={'input.mp4': None},
...     outputs={'output.avi': None}
... )
>>> ff.run_async()
>>> await ff.wait()
```
FFmpeg也可以在没有多线程或阻塞的情况下处理输出。以下代码段从FFmpeg的progress输出中替换CR为LF，并STDERR在FFmpeg处理输入视频时将其回显。
```
>>> import asyncio
>>> import sys
>>> ff = ffmpy3.FFmpeg(
...     inputs={'input.mp4': None},
...     outputs={'output.avi': None},
... )
>>> await ff.run_async(stderr=asyncio.subprocess.PIPE)
>>> line_buf = bytearray()
>>> while True:
>>>     in_buf = (await my_stderr.read(128)).replace(b'\r', b'\n')
>>>     if not in_buf:
>>>         break
>>>     line_buf.extend(in_buf)
>>>     while b'\n' in line_buf:
>>>         line, _, line_buf = line_buf.partition(b'\n')
>>>         print(str(line), file=sys.stderr)
>>> await ff.wait()
```

## 复杂的命令行
FFmpeg命令行选项可能会变得非常复杂，例如使用filter时。因此，了解使用构建命令行的一些规则很重要ffmpy3。
如果选项包含引号，则必须在选项列表中将其指定为单独的项目，且不带引号。但是，如果将单个字符串用作选项，则必须在字符串中保留带引号的选项的引号：
```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.ts': ['-vf', 'adif=0:-1:0, scale=iw/2:-1']}
... )
>>> ff.cmd
'ffmpeg -i input.ts -vf "adif=0:-1:0, scale=iw/2:-1" output.ts'
>>>
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.ts': '-vf "adif=0:-1:0, scale=iw/2:-1"'}
... )
>>> ff.cmd
'ffmpeg -i input.ts -vf "adif=0:-1:0, scale=iw/2:-1" output.ts'
```

甚至更复杂的示例是将时间码刻录到视频中的命令行
```
ffmpeg -i input.ts -vf "drawtext=fontfile=/Library/Fonts/Verdana.ttf: timecode='09\:57\:00\:00': r=25: x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000000@1" -an output.ts```
```

在ffmpy3它可以通过以下方式来表达：
```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.ts': ['-vf', "drawtext=fontfile=/Library/Fonts/Verdana.ttf: timecode='09\:57\:00\:00': r=25: x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000000@1", '-an']}
... )
>>> ff.cmd
'ffmpeg -i input.ts -vf "drawtext=fontfile=/Library/Fonts/Verdana.ttf: timecode=\'09\:57\:00\:00\': r=25: x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000000@1" -an output.ts'
```

通过将输出选项作为单个字符串传递，同时保留引号，可以编译同一命令行：
```
>>> ff = FFmpeg(
...     inputs={'input.ts': None},
...     outputs={'output.ts': ["-vf \"drawtext=fontfile=/Library/Fonts/Verdana.ttf: timecode='09\:57\:00\:00': r=25: x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000000@1\" -an"}
... )
>>> ff.cmd
'ffmpeg -i input.ts -vf "drawtext=fontfile=/Library/Fonts/Verdana.ttf: timecode=\'09\:57\:00\:00\': r=25: x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000000@1" -an output.ts'
```

## 异常
### ffmpy3.FFExecutableNotFoundError
**在找不到FFmpeg / FFprobe可执行文件时引发。**

### ffmpy3.FFRuntimeError（cmd，exit_code，stdout = b''，stderr = b'' ）
**在FFmpeg / FFprobe命令行执行返回非零退出代码时引发。**
 - cmd（power命令） 该命令用于启动可执行文件，并带有所有命令行选项。

 - exit_code（整型） 可执行文件的结果退出代码。

 - stdout（字节）   stdout的内容（仅在同步执行时）。

 - stderr（字节）   stderr的内容（仅在同步执行时）。

## 类
### ffmpy3.FFmpeg（可执行文件='ffmpeg'，global_options =无，输入=无，输出=无）
 - 各种FFmpeg相关应用程序（ffmpeg，ffprobe）的包装器。
 - 从传递的参数（可执行路径，选项，输入和输出）编译FFmpeg命令行。
 - inputs和outputs是包含输入/输出作为键以及它们各自的选项作为值的字典。
 - 一个字典值（选项集）必须是一个用空格分隔的字符串，或者是一个或多个不包含空格的字符串（即，选项的每个部分都是列表的单独项，是调用split()选项字符串的结果）。
 - 如果值是列表，则不能混合使用，即不能包含带空格的项目。复杂的FFmpeg命令行包含引号是一个例外：引号部分必须是一个字符串，即使它包含空格（有关更多信息，请参见示例）。

参数：	
 - 可执行文件（str）– ffmpeg可执行文件的路径；默认情况下，该ffmpeg命令将在中搜索 PATH，但可以用ffmpeg可执行文件的绝对路径覆盖
 - global_options（iterable）–传递给ffmpeg可执行文件的全局选项（例如-y，-v等等）；可以指定为列表/元组/字符串集，也可以指定为一个以空格分隔的字符串；默认情况下，不传递全局选项
 - input（dict）–一种字典，将一个或多个输入参数指定为键，并将其对应选项（以字符串列表或单个以空格分隔的字符串）作为值
 - 输出（dict）–一个字典，将一个或多个输出参数指定为键，并将其对应选项（作为字符串列表或单个以空格分隔的字符串）作为值
 - run（input_data = None，stdout = None，stderr = None）-执行FFmpeg命令行。


参数：	
 - input_data（字节）– FFmpeg以字节形式处理（音频，视频等）的输入数据（例如，以二进制模式读取文件的结果）
 - stdout –将FFmpeg重定向stdout到的位置。默认值为None，表示不重定向。
 - stderr –将FFmpeg重定向stderr到的位置。默认值为None，表示不重定向。
异常：
 - FFExecutableNotFoundError –传递的可执行路径无效。
 - FFRuntimeError –进程退出并出现错误。
返回值：一个包含stdout和stderr来自过程的2元组。

### run_async（input_data = None，stdout = None，stderr = None ）异步执行FFmpeg命令行。

input_data在管道情况下可以包含FFmpeg的输入

stdout并stderr指定将流程的stdout和重定向到stderr的位置。默认情况下，不进行任何重定向，这意味着所有输出都将进入运行中的shell（此模式通常仅应用于调试目的）。

如果将FFmpegpipe协议用于输出，则stdout必须通过传递subprocess.PIPE作为 stdout参数将其重定向到管道。

请注意，父进程负责读取stdout / stderr的任何输出。即使不使用输出，也应这样做，因为否则该过程可能会死锁。
这可以通过等待asyncio.subprocess.Process.communicate()返回的内容 来完成，也可以asyncio.subprocess.Process根据需要手动从流中读取。

返回对创建供父程序使用的子进程的引用。

参数：	
 - input_data（字节）– FFmpeg以字节形式处理（音频，视频等）的输入数据（例如，以二进制模式读取文件的结果）
 - stdout –将FFmpeg重定向stdout到的位置。默认值为None，表示不重定向。
 - stderr –将FFmpeg重定向stderr到的位置。默认值为None，表示不重定向。
异常：FFExecutableNotFoundError –传递的可执行路径无效。
返回类型：asyncio.subprocess.Process

### wait（）
异步等待过程完成执行。
 - 异常：FFRuntimeError –进程退出并出现错误。
 - 返回值：	如果该过程成功完成，则为0；如果尚未开始，则为None
 - 返回类型：	整型或无

###  ffmpy3.FFprobe（可执行文件='ffprobe'，global_options =''，输入=无）
从传递的参数（可执行路径，选项，输入）中编译FFprobe命令行。FFprobe可执行文件默认情况下取自，PATH但可以用绝对路径覆盖。
参数：	
 - 可执行文件（str）– ffprobe可执行文件的绝对路径
 - global_options（iterable）–传递给ffprobe可执行文件的全局选项；可以指定为字符串列表/元组或空格分隔的字符串
 - 输入（dict）–一种字典，指定一个或多个输入为键，其对应选项为值
