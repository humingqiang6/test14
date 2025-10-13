#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <string>
#include <fstream>

int main() {
    // Example array
    std::vector<int> arr = {3, 7, 2, 9, 1};

    // Find the maximum element
    auto max_element_it = std::max_element(arr.begin(), arr.end());
    if (max_element_it != arr.end()) {
        int max_val = *max_element_it;
        std::cout << "Maximum value in the array is: " << max_val << std::endl;

        // Generate a random filename
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(10000, 99999);
        std::string filename = "max_result_" + std::to_string(dis(gen)) + ".txt";

        // Write the result to the file
        std::ofstream outFile(filename);
        if (outFile.is_open()) {
            outFile << max_val;
            outFile.close();
            std::cout << "Result saved to file: " << filename << std::endl;
        } else {
            std::cerr << "Error: Could not open file for writing." << std::endl;
            return 1;
        }
    } else {
        std::cerr << "Error: Array is empty." << std::endl;
        return 1;
    }

    return 0;
}