#include <iostream>
#include <vector>
#include <algorithm> // for std::max_element
#include <iterator>  // for std::begin, std::end

int main() {
    // Example array
    std::vector<int> numbers = {3, 7, 2, 9, 1, 5, 8};

    // Find the maximum element
    auto max_it = std::max_element(std::begin(numbers), std::end(numbers));

    if (max_it != std::end(numbers)) {
        std::cout << "The maximum number in the array is: " << *max_it << std::endl;
    } else {
        std::cout << "The array is empty." << std::endl;
    }

    return 0;
}