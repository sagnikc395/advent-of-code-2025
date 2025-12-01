#include <fstream>
#include <iostream>
#include <string>



int main() {
  std::string data_path = "../data/day1-input.txt";

  //helper function
  std::vector<std::string> file_data = read_file_line_by_line(data_path);

  std::cout << "Read " << file_data.size() << "lines" << std::endl;

  return 0;
}
