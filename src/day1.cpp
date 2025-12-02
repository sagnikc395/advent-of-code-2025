#include "../include/file_utils.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

int solve_part1(const std::vector<std::string> &lines)
{
  if (lines.empty())
  {
    std::cout << "Input is empty.Cannot solve." << std::endl;
    return 0;
  }

  int total_length = 0;
  for (const std::string &line : lines)
  {
    if (!line.empty())
    {
      total_length += line.length();
    }
  }

  std::cout << "Processed " << lines.size() << "lines" << std::endl;

  return 1;
}

int solve_part2(const std::vector<std::string> &lines)
{
  return 0;
}

int main()
{

  const std::string input_filepath = "../../data/day1.txt";
  std::cout << "Starting Part 1 Solver: Reading input from " << input_filepath << std::endl;

  // 2. I/O Delegation (Calling the utility function to read and trim the file)
  // The implementation of this function is in src/utils/file_utils.cpp
  std::vector<std::string> lines = read_file_line_by_line(input_filepath);

  if (lines.empty())
  {
    std::cout << "Could not retrieve input data. Exiting." << std::endl;
    return 0;
  }

  // 3. Core Logic Execution
  std::cout << "\n--- Running Part 1 Solver ---" << std::endl;
  int result1 = solve_part1(lines);
  int result2 = solve_part2(lines);

  std::cout << "\n===============================" << std::endl;
  std::cout << "Part 1 Final Answer: " << result1 << std::endl;
  std::cout << "Part 2 Final Answer: " << result2 << std::endl;
  std::cout << "===============================" << std::endl;

  return 0;
}