#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>

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

unsigned long seed_to_location(const vector<vector<MapRange>>& maps, unsigned long val) {
  for (const auto& map : maps) {
    val = use_map(map, val);
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

  // part 1
  vector<unsigned long> locations;
  transform(seeds.begin(), seeds.end(), back_inserter(locations), [&maps](unsigned long seed) {
    return seed_to_location(maps, seed);
  });

  unsigned long p1 = *min_element(locations.begin(), locations.end());
  cout << "p1 = " << p1 << endl;

  unsigned long p2 = numeric_limits<unsigned long>::max();
  for (size_t i = 0; i < seeds.size(); i += 2) {
    for (unsigned long seed = seeds[i]; seed < seeds[i] + seeds[i + 1]; ++seed) {
      // if (seed % 100'000'000 == 0) {
      //   cout << (seed - seeds[i]) << " / " << seeds[i + 1] << "\r";
      // }
      p2 = min(p2, seed_to_location(maps, seed));
    }
    // cout << "[" <<seeds[i] << ", " << (seeds[i] + seeds[i + 1]) << "] done\n";
  }

  cout << "p2 = " << p2 << endl;
}
