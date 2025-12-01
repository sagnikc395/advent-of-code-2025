// helper uitlities
// contains the function prototypes and necessary includes
//
#ifndef  FILE_UTILS_H
#define FILE_UTILS_H

#include <string>
#include <vector>

// function declaration
// reads the content of the file and returns it as a vector of strings
std::vector<std::string> read_file_line_by_line(const std::string& filename);

#endif 
