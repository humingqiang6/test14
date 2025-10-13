#include <iostream>
#include <fstream>
#include <string>
#include <random>

// Template function to swap two values
template<typename T>
void mySwap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    // Example usage with integers
    int x = 10;
    int y = 20;
    std::cout << "Before swap: x = " << x << ", y = " << y << std::endl;
    mySwap(x, y);
    std::cout << "After swap: x = " << x << ", y = " << y << std::endl;

    // Example usage with doubles
    double a = 5.5;
    double b = 3.3;
    std::cout << "Before swap: a = " << a << ", b = " << b << std::endl;
    mySwap(a, b);
    std::cout << "After swap: a = " << a << ", b = " << b << std::endl;

    // Generate a random filename
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(10000, 99999);
    std::string filename = "swap_output_" + std::to_string(dis(gen)) + ".cpp";

    // Write the template function to the file
    std::ofstream file(filename);
    if (file.is_open()) {
        file << "#include <iostream>\n";
        file << "#include <fstream>\n";
        file << "#include <string>\n";
        file << "#include <random>\n\n";
        file << "// Template function to swap two values\n";
        file << "template<typename T>\n";
        file << "void mySwap(T& a, T& b) {\n";
        file << "    T temp = a;\n";
        file << "    a = b;\n";
        file << "    b = temp;\n";
        file << "}\n\n";
        file << "int main() {\n";
        file << "    // Example usage with integers\n";
        file << "    int x = 10;\n";
        file << "    int y = 20;\n";
        file << "    std::cout << \"Before swap: x = \" << x << \", y = \" << y << std::endl;\n";
        file << "    mySwap(x, y);\n";
        file << "    std::cout << \"After swap: x = \" << x << \", y = \" << y << std::endl;\n\n";
        file << "    // Example usage with doubles\n";
        file << "    double a = 5.5;\n";
        file << "    double b = 3.3;\n";
        file << "    std::cout << \"Before swap: a = \" << a << \", b = \" << b << std::endl;\n";
        file << "    mySwap(a, b);\n";
        file << "    std::cout << \"After swap: a = \" << a << \", b = \" << b << std::endl;\n\n";
        file << "    return 0;\n";
        file << "}\n";
        file.close();
        std::cout << "Template function saved to file: " << filename << std::endl;
    } else {
        std::cerr << "Error: Could not create file " << filename << std::endl;
        return 1;
    }

    return 0;
}