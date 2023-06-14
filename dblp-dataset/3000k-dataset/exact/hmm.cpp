#include <bits/stdc++.h>

using namespace std;
using namespace std::chrono;

class DoubleLetterHMM {
public:
  DoubleLetterHMM(int n) : states(n) {}

  void add_word(string& word) {
    word = normalize_strings(word);
    for (int i = 0; i < word.size() - 1; i++) {
      states[i][word.substr(i, 2)]++;
      states[i][word.substr(i, 1) + '%']++;
      states[i]['%' + word.substr(i+1, 1)]++;
      states[i]["%%"]++;
    }
    total_words++;
  }
  
  double get_probability(string& word) {
    pair<string, vector<bool>> normalized = normalize_strings_and_create_branch(word);
    string& new_word = normalized.first;
    vector<bool>& branches = normalized.second;
    map<array<int, 2>, double> dp;
    return get_probability_helper(dp, new_word, branches, 0, 0);
  }

  void print(){
    for (int i = 0; i < states.size(); i++) {
      cout << "State " << i << endl;
      for (auto& p : states[i]) {
        cout << p.first << " " << p.second << endl;
      }
    }
  }

private:
  vector<unordered_map<string, int>> states;
  int total_words = 0;

  double get_probability_helper(map<array<int, 2>, double>& dp, string& word, vector<bool>& branches, int word_index, int state_index) {
    if (word_index == word.size() - 1) {
      return 1.0;
    }

    // if the state and word index is already calculated
    // return the value
    if (dp.find({word_index, state_index}) != dp.end()) {
      // cout << "Found " << word_index << " " << state_index << endl;
      return dp[{word_index, state_index}];
    }

    // if there are no observation for specific state 
    // return 0 
    double prob;
    if (states[state_index].find(word.substr(word_index, 1) + '%') == states[state_index].end()){
      return 0.0;
    } else {
      // otherwise calculate the probability as usual
      // if (word[word_index] == '%') {
      //   prob = 1.0;
      // } else {
        prob = states[state_index][word.substr(word_index, 2)] / 
              (double)states[state_index][word.substr(word_index, 1) + '%'];
      // }
    }

    // if the current letter does not have a proceeding with %
    if (!branches[word_index]) { 
      return dp[{word_index, state_index}] = 
          prob * get_probability_helper(dp, word, branches, word_index + 1, state_index + 1);
    } else { // the letter has preciding % character 
      double sub_prob = 0.0;
      int remaining_letters = word.size() - 1 - word_index;

      // the empty string case instead of % character
      sub_prob += (states[state_index][word.substr(word_index, 1) + word.substr(word_index+2, 1)] / 
              (double)states[state_index][word.substr(word_index, 1) + '%']) *
              get_probability_helper(dp, word, branches, word_index + 2, state_index + 1);

      // same loop as single-letter case
      for (int i = state_index + 1; i <= states.size() - remaining_letters; i++) {
        sub_prob += get_probability_helper(dp, word, branches, word_index + 1, i);
      }
      double res_prob = min(1.0, prob * sub_prob);
      return dp[{word_index, state_index}] = res_prob;
    }
  }

  string normalize_strings(string& word) {
    return "$" + word + "#";
  }

  pair<string, vector<bool>> normalize_strings_and_create_branch(string& word) {
    vector<bool> branches(word.size() + 3, false);
    string new_word = "$";
    for (int i = 0; i < word.size(); i++) {
      if (word[i] == '%'){ // don't jump the loop if the letter is %
                          // leave the % characters in the new word
        branches[i] = true;
      }
      new_word += word[i];
    }
    new_word += "#";
    return {new_word, branches};
  }
};


int main(){

  ifstream file_words("authors.txt");
  ifstream file_queries("queries.txt");
  ofstream file_results("hmm_output.txt");

  double total_build_time = 0.0;
  auto startTime = high_resolution_clock::now();

  DoubleLetterHMM hmm(60);
  string word;
  long long int count = 0;
  while (getline(file_words, word)) {
    // cout << "Adding " << word << endl;
    hmm.add_word(word);
    count++;
  }

  auto stopTime = high_resolution_clock::now();
  auto duration = duration_cast<milliseconds>(stopTime - startTime);
  total_build_time += duration.count();
  cout << "Total words: " << count << endl;
  // hmm.print();

  double total_query_time = 0.0;
  double total_count = 0.0;
  while (getline(file_queries, word)) {
    auto startTime = high_resolution_clock::now();
    double query_prob = min(1.0, hmm.get_probability(word));
    double query_count = query_prob * count;
    query_count = round(query_count);
    if (query_count == 0) {
      query_count = 1;
    }
    auto stopTime = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stopTime - startTime);
    total_query_time += duration.count();
    total_count++;
    file_results << query_count << endl;
    cout << "The probabilty of " << word << " is " << query_count << endl;
  }
  cout << "Average query time: " << total_query_time / total_count << " ms" << endl;
  cout << "Average build time: " << total_build_time << " ms" << endl;
}
