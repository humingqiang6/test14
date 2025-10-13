#!/bin/bash

# 模拟Dart异步函数获取网络数据并保存到随机命名的.dart文件中

echo "正在模拟获取网络数据..."

# 使用curl模拟网络请求
response=$(curl -s https://api.github.com/users/octocat)
if [ $? -ne 0 ]; then
    echo "网络请求失败"
    exit 1
fi

# 检查响应状态（这里简单模拟200 OK）
if [[ $response == *"login"* ]]; then
    echo "数据获取成功，正在保存..."

    # 生成一个随机文件名，使用时间戳确保唯一性
    random_suffix=$(date +%s%3N)
    file_name="/workspace/dart_async/simulated_data_${random_suffix}.dart"

    # 将数据转换为Dart Map格式的字符串
    cat <<EOF > "$file_name"
// 模拟数据文件
// 该文件由模拟脚本生成，代表从网络获取的数据。
const Map<String, dynamic> githubUserData = ${response};
EOF

    echo "数据已模拟保存到 $file_name"
else
    echo "获取数据失败，响应格式不正确"
    exit 1
fi