import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

Future<void> fetchAndSaveData() async {
  try {
    print('正在获取数据...');
    final response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/posts/1'));

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      print('数据获取成功: $data');

      // 生成随机文件名
      final randomId = DateTime.now().millisecondsSinceEpoch;
      final fileName = 'data_$randomId.dart';
      final filePath = '/workspace/$fileName';

      // 创建一个包含获取到的数据的简单Dart代码字符串
      final fileContent = '''
// Auto-generated Dart file with fetched data
// Fetched at: ${DateTime.now().toIso8601String()}

final Map<String, dynamic> fetchedData = ${jsonEncode(data)};
''';

      // 将内容写入文件
      await File(filePath).writeAsString(fileContent);
      print('数据已保存到 $filePath');
    } else {
      print('请求失败，状态码: ${response.statusCode}');
    }
  } catch (e) {
    print('发生错误: $e');
  }
}

void main() async {
  await fetchAndSaveData();
}