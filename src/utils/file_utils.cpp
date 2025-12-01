#include "file_utils.h"
#include <fstream>
#include <iostream>

std::vector<std::string> read_file_line_by_line(const std::string& filename) {
    std::vector<std::string> contents;
    std::ifstream inputFile(filename);

    if (inputFile.is_open()) {
        std::string line;
        while (std::getline(inputFile, line)) {
            // You can add your trimming logic here if needed
            contents.push_back(line);
        }
        inputFile.close();
    } else {
        std::cerr << "Error: Could not open data file: " << filename << std::endl;
    }
    return contents;
}
