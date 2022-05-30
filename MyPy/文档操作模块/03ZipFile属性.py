import zipfile, os

zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'duoduo.zip'))
zipInfo = zipFile.getinfo('文件中的文件.txt')

print('filename:', zipInfo.filename)    # 获取文件名称
print('date_time:', zipInfo.date_time)    # 获取文件最后修改时间。返回一个包含6个元素的元组：(年, 月, 日, 时, 分, 秒)
print('compress_type:', zipInfo.compress_type)    # 压缩类型
print('comment:', zipInfo.comment)    # 文档说明
print('extra:', zipInfo.extra)    # 扩展项数据
print('create_system:', zipInfo.create_system)    # 获取创建该zip文档的系统。
print('create_version:', zipInfo.create_version)    # 获取 创建zip文档的PKZIP版本。
print('extract_version:', zipInfo.extract_version)    # 获取 解压zip文档所需的PKZIP版本。
print('extract_version:', zipInfo.reserved)    # 预留字段，当前实现总是返回0。
print('flag_bits:', zipInfo.flag_bits)    # zip标志位。
print('volume:', zipInfo.volume)    # 文件头的卷标。
print('internal_attr:', zipInfo.internal_attr)    # 内部属性。
print('external_attr:', zipInfo.external_attr)    # 外部属性。
print('header_offset:', zipInfo.header_offset)    # 文件头偏移位。
print('CRC:', zipInfo.CRC)    # 未压缩文件的CRC-32。
print('compress_size:', zipInfo.compress_size)    # 获取压缩后的大小。
print('file_size:', zipInfo.file_size)    # 获取未压缩的文件大小。
zipFile.close()