#include <fstream>
#include <string>
#include <iostream>
#include <cmath>

int solve_part1(std::vector<std::string> &contents)
{
  int zero_count = 0;
  int current_position = 50;

  for (const std::string &rotation : contents)
  {
    if (rotation.empty())
    {
      continue;
    }

    char direction = rotation[0];

    std::string distance_str = rotation.substr(1);

    int distance = 0;
    try
    {
      distance = std::stoi(distance_str);
    }
    catch (const std::invalid_argument &e)
    {
      distance = 0;
    }
    catch (const std::out_of_range &e)
    {
      distance = 0;
    }
    const int TRACK_SIZE = 100;

    if (direction == 'L')
    {
      current_position = (current_position - distance % TRACK_SIZE + TRACK_SIZE) % TRACK_SIZE;
    }
    else if (direction == 'R')
    {
      current_position = (current_position + distance) % TRACK_SIZE;
    }

    if (current_position == 0)
    {
      zero_count++;
    }
  }

  return zero_count;
}

int calculate_zero_crossings(int start_pos, std::string direction, int distance)
{
  if (direction == "R")
  {
    return (start_pos + distance) / 100;
  }
  else if (direction == "L")
  {
    double start_val = static_cast<double>(start_pos - 1) / 100.0;
    double end_val = static_cast<double>(start_pos - distance - 1) / 100.0;

    return static_cast<int>(std::floor(start_val) - std::floor(end_val));
  }
  return 0;
}

int solve_part2(std::vector<std::string> &contents)
{
  int current_position = 50;
  int total_zero_crossings = 0;
  const int TRACK_SIZE = 100;

  for (const std::string &rotation : contents)
  {
    if (rotation.empty())
    {
      continue;
    }

    char direction_char = rotation[0];
    std::string direction_str(1, direction_char);

    std::string distance_str = rotation.substr(1);

    int distance = 0;
    try
    {
      distance = std::stoi(distance_str);
    }
    catch (const std::exception &e)
    {
      distance = 0;
    }

    int crossings_this_rotation = calculate_zero_crossings(current_position, direction_str, distance);
    total_zero_crossings += crossings_this_rotation;

    if (direction_char == 'L')
    {
      current_position = (current_position - (distance % TRACK_SIZE) + TRACK_SIZE) % TRACK_SIZE;
    }
    else if (direction_char == 'R')
    {
      current_position = (current_position + distance) % TRACK_SIZE;
    }
  }

  return total_zero_crossings;
}

int main()
{
  std::ifstream inputFile("../data/day1-input.txt");

  if (!inputFile.is_open())
  {
    std::cerr << "Error opening the file!" << std::endl;
    return 1;
  }

  std::string line;
  std::vector<std::string> contents;
  while (std::getline(inputFile, line))
  {
    contents.push_back(line);
  }

  int result1 = solve_part1(contents);
  std::cout << "Part1 solution: " << result1 << std::endl;
  int result2 = solve_part2(contents);
  std::cout << "Part2 solution: " << result2 << std::endl;

  inputFile.close();
  return 0;
}
