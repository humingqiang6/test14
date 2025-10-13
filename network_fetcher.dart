import 'dart:io';
import 'dart:convert';
import 'dart:math';

Future<void> fetchAndSaveData(String url) async {
  try {
    final client = HttpClient();
    final request = await client.getUrl(Uri.parse(url));
    final response = await request.close();

    if (response.statusCode == 200) {
      final responseBody = await response.transform(utf8.decoder).join();
      client.close();

      // 生成随机文件名
      const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      final random = Random();
      final fileName = 'data_${String.fromCharCodes(Iterable.generate(8, (_) => chars.codeUnitAt(random.nextInt(chars.length))))}.dart';

      final file = File(fileName);
      await file.writeAsString('''
// Data fetched from $url
const String rawData = r\'\'\'
$responseBody
\'\'\';
''');

      print('Data successfully fetched and saved to $fileName');
    } else {
      client.close();
      throw HttpException('Failed to fetch data. Status code: ${response.statusCode}');
    }
  } catch (e) {
    print('An error occurred: $e');
  }
}
