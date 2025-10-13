import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

Future<void> fetchAndSaveData() async {
  try {
    print('正在获取网络数据...');
    final response = await http.get(Uri.parse('https://api.github.com/users/octocat'));

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      print('数据获取成功，正在保存...');

      // 生成一个随机文件名
      var random = DateTime.now().millisecondsSinceEpoch;
      String fileName = '/workspace/dart_async/data_$random.dart';

      // 将数据转换为Dart Map格式的字符串
      String dartCode = '''
// 数据文件
const Map<String, dynamic> githubUserData = $data;
''';

      // 写入文件
      await File(fileName).writeAsString(dartCode);
      print('数据已保存到 $fileName');
    } else {
      throw Exception('获取数据失败: ${response.statusCode}');
    }
  } catch (e) {
    print('发生错误: $e');
  }
}

void main() async {
  await fetchAndSaveData();
}