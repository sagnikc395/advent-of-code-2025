#include "../../include/file_utils.h"
#include <fstream>
#include <iostream>

//return true if character is not whitespace
static bool is_not_space(char c){
  return !std::isspace(static_cast<unsigned char>(c));
}



std::vector<std::string> read_file_line_by_line(const std::string& filename) {
  std::vector<std::string> contents;
  std::ifstream inputFile(filename);

  if(inputFile.is_open()){
    std::string line;
    while(std::getline(inputFile,line)) {
      //trailing whitespace removal logic
      line.erase(std::find_if(line.rbegin(), line.rend(), is_not_space).base(),
      line.end());

      contents.push_back(line);
    }
    inputFile.close();
  } else {
    std::cerr << "Error: Could not open data file: " << filename << std::endl;
  }
  return contents;
}
