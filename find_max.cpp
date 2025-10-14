#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <ctime>
#include <fstream>

int main() {
    // Example array
    std::vector<int> numbers = {3, 7, 2, 9, 1};

    // Find the maximum element
    int max_num = *std::max_element(numbers.begin(), numbers.end());

    std::cout << "The maximum number in the array is: " << max_num << std::endl;

    // Generate a random filename
    std::srand(std::time(0));
    int random_id = std::rand();
    std::string filename = "/workspace/max_result_" + std::to_string(random_id) + ".txt";

    // Write the result to the file
    std::ofstream file(filename);
    if (file.is_open()) {
        file << max_num;
        file.close();
        std::cout << "Result saved to file: " << filename << std::endl;
    } else {
        std::cerr << "Could not open file for writing." << std::endl;
        return 1;
    }

    return 0;
}