#!/bin/bash
# 获取当前用户信息并保存到随机命名的.sh文件中

# 获取当前用户名
USERNAME=$(whoami)
# 获取用户ID
USER_ID=$(id -u)
# 获取用户主目录
HOME_DIR=$(echo $HOME)
# 获取当前时间戳，用作随机文件名的一部分
TIMESTAMP=$(date +%s%3N) # 秒级时间戳+毫秒

# 创建包含用户信息的文本
USER_INFO="当前用户名: $USERNAME
用户ID: $USER_ID
主目录: $HOME_DIR
信息获取时间: $(date)
"

# 生成随机文件名 (例如: user_info_123456.sh)
OUTPUT_FILE="user_info_${TIMESTAMP}.sh"

# 将用户信息写入随机命名的文件
echo "$USER_INFO" > "$OUTPUT_FILE"

echo "用户信息已保存到文件: $OUTPUT_FILE"
cat "$OUTPUT_FILE"