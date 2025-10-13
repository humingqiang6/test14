#ifndef SWAP_TEMPLATE_HPP
#define SWAP_TEMPLATE_HPP

// A generic template function to swap the values of two variables.
template<typename T>
void my_swap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

#endif // SWAP_TEMPLATE_HPP