#!/bin/bash

# 检查系统内存使用情况并保存到文件

# 获取内存使用信息
memory_info=$(free -h)

# 生成一个随机的.sh文件名
random_filename=$(mktemp --suffix=.sh)

# 将内存信息写入随机命名的.sh文件
echo "$memory_info" > "$random_filename"

# 输出生成的文件名
echo "内存使用情况已保存到: $random_filename"