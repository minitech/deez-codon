#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>

#include "ArithmeticCoder.h"

int main() {
    Array<uint8_t> dest;
    ArithmeticCoder ac;
    ac.initEncode(&dest);

    for (;;) {
        std::string line;

        if (!std::getline(std::cin, line)) {
            if (std::cin.bad()) {
                std::perror("Error reading from stdin");
                return EXIT_FAILURE;
            }

            break;
        }

        std::uint32_t cumFreq;
        std::uint32_t freq;
        std::uint32_t totFreq;

        std::istringstream words {line};

        if (words >> cumFreq >> freq >> totFreq) {
            if (words.peek() != std::char_traits<char>::eof()) {
                std::cerr << "Input format error: unexpected trailing input\n";
                return EXIT_FAILURE;
            }
        } else {
            std::cerr << "Input format error: expected unsigned 32-bit integer\n";
            return EXIT_FAILURE;
        }

        ac.encode(cumFreq, freq, totFreq);
    }

    ac.flush();

    // NOTE: Windows needs binary mode
    std::cout.write(reinterpret_cast<char const*>(dest.data()), dest.size());

    if (!std::cout.good()) {
        std::cerr << "Error writing to stdout\n";
        return EXIT_FAILURE;
    }
}
