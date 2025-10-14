#include <iostream>
#include <fstream>
#include <string>
#include <random>

// 模板函数：交换两个变量的值
template<typename T>
void mySwap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

// 生成随机文件名
std::string generateRandomFileName(const std::string& extension = ".txt") {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(10000, 99999);
    return "temp_file_" + std::to_string(dis(gen)) + extension;
}

int main() {
    // 示例：交换两个整数
    int x = 5;
    int y = 10;
    std::cout << "交换前: x = " << x << ", y = " << y << std::endl;
    mySwap(x, y);
    std::cout << "交换后: x = " << x << ", y = " << y << std::endl;

    // 将结果保存到随机命名的文件
    std::string filename = generateRandomFileName(".cpp");
    std::ofstream outFile(filename);
    if (outFile.is_open()) {
        outFile << "// C++ Template Function for Swapping Values\n";
        outFile << "#include <iostream>\n\n";
        outFile << "template<typename T>\n";
        outFile << "void mySwap(T& a, T& b) {\n";
        outFile << "    T temp = a;\n";
        outFile << "    a = b;\n";
        outFile << "    b = temp;\n";
        outFile << "}\n\n";
        outFile << "int main() {\n";
        outFile << "    // Example usage with integers\n";
        outFile << "    int x = 5;\n";
        outFile << "    int y = 10;\n";
        outFile << "    std::cout << \"Before swap: x = \" << x << \", y = \" << y << std::endl;\n";
        outFile << "    mySwap(x, y);\n";
        outFile << "    std::cout << \"After swap: x = \" << x << \", y = \" << y << std::endl;\n";
        outFile << "    return 0;\n";
        outFile << "}";
        outFile.close();
        std::cout << "代码已保存到文件: " << filename << std::endl;
    } else {
        std::cerr << "无法创建文件!" << std::endl;
    }

    return 0;
}