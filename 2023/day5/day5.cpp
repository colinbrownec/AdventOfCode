#include <algorithm>
#include <execution>
#include <iostream>
#include <numeric>
#include <ranges>
#include <sstream>
#include <vector>

using namespace std;

struct MapRange {
  MapRange(unsigned long dst, unsigned long src, unsigned long n)
    : destination_start(dst)
    , source_start(src)
    , n(n)
  {}
  unsigned long destination_start;
  unsigned long source_start;
  unsigned long n;
};

unsigned long use_map(const vector<MapRange>& map, unsigned long val) {
  for (const auto& range : map) {
    if (range.source_start <= val && val < range.source_start + range.n) {
      return val - range.source_start + range.destination_start;
    }
  }
  return val;
}

int main()
{
  vector<unsigned long> seeds;
  vector<vector<MapRange>> maps;
  string line;
  
  // parse seeds
  {
    getline(cin, line);
    stringstream ss;
    ss << line;
    
    string tmp;
    unsigned long seed;
    
    ss >> tmp;
    while (ss >> seed) seeds.push_back(seed);
  }
  
  getline(cin, line);

  // parse maps
  {
    unsigned long dst, src, n;
    
    while (getline(cin, line)) {
      maps.emplace_back();
      while (getline(cin, line) && !line.empty()) {
        stringstream ss;
        ss << line;
        ss >> dst >> src >> n;
        maps.back().emplace_back(dst, src, n);
      }
    }
  }

  auto seed_to_location = [&maps](unsigned long val) {
    for (const auto& map : maps) {
      val = use_map(map, val);
    }
    return val;
  };

  // part 1
  unsigned long p1 = ranges::min(seeds | views::transform(seed_to_location));
  cout << "p1 = " << p1 << endl;

  // part 2
  unsigned long p2 = numeric_limits<unsigned long>::max();
  for (size_t i = 0; i < seeds.size(); i += 2) {
     ranges::iota_view range{ seeds[i], seeds[i] + seeds[i + 1] };
     p2 = transform_reduce(
       execution::par,
       range.begin(),
       range.end(),
       p2,
       [](unsigned long a, unsigned long b) { return min(a, b); },
       seed_to_location);
  }
  cout << "p2 = " << p2 << endl;
}
