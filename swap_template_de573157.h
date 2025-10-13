#ifndef SWAP_TEMPLATE_H
#define SWAP_TEMPLATE_H

// A generic template function to swap the values of two variables.
template<typename T>
void mySwap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}

#endif // SWAP_TEMPLATE_H