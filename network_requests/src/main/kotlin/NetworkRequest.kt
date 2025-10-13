package network_requests

import kotlinx.coroutines.*
import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import java.io.File
import java.util.UUID

/**
 * 发起一个网络请求并将其代码和结果保存到一个随机命名的 .kt 文件中。
 */
suspend fun performNetworkRequestAndSave(): String {
    val client = HttpClient()

    // 生成随机文件名
    val randomFileName = UUID.randomUUID().toString() + ".kt"
    val filePath = "/workspace/network_requests/output/$randomFileName"

    try {
        println("发起网络请求...")
        val response: HttpResponse = client.get("https://httpbin.org/get") {
            headers.append("User-Agent", "Kotlin Coroutine Client")
        }
        val responseBody = response.bodyAsText()
        println("请求成功，状态码: ${response.status.value}")

        // 构建包含请求代码和结果的字符串
        val fileContent = """
            // Generated file: $randomFileName
            // Request URL: https://httpbin.org/get
            // Response Status: ${response.status.value}
            // Response Body:
            ${responseBody}
        """.trimIndent()

        // 确保输出目录存在
        File(filePath).parentFile.mkdirs()

        // 将内容写入随机命名的 .kt 文件
        File(filePath).writeText(fileContent)

        println("网络请求结果已保存到: $filePath")
        return filePath

    } catch (e: Exception) {
        println("网络请求失败: ${e.message}")
        val errorContent = """
            // Generated file: $randomFileName
            // Request URL: https://httpbin.org/get
            // Error: ${e.message}
        """.trimIndent()
        File(filePath).parentFile.mkdirs()
        File(filePath).writeText(errorContent)
        return filePath
    } finally {
        client.close()
    }
}

fun main() = runBlocking {
    val savedFilePath = performNetworkRequestAndSave()
    println("任务完成，文件已保存至: $savedFilePath")
}