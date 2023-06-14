#include <bits/stdc++.h>

using namespace std;

class SingleLetterHMM {
public:
  SingleLetterHMM(int n) : states(n) {}

  void add_word(string& word) {
    word = normalize_strings(word);
    for (int i = 0; i < word.size(); i++) {
      states[i][word[i]]++;
      states[i]['%']++;
    }
    total_words++;
  }

  double get_probability(string& word) {
    pair<string, vector<bool>> normalized = normalize_strings_and_create_branch(word);
    string& new_word = normalized.first;
    vector<bool>& branches = normalized.second;
    return get_probability_helper(new_word, branches, 0, 0);
  }

private:
  vector<unordered_map<char, int>> states;
  int total_words = 0;

  double get_probability_helper(string& word, vector<bool>& branches, int word_index, int state_index) {
    if (word_index == word.size()) {
      return 1.0;
    }

    double prob = 1.0;
    if (!branches[word_index]) { // if the current letter does not have a proceeding with %
      prob *= states[state_index][word[word_index]] / (double)states[state_index]['%'];
      return prob * get_probability_helper(word, branches, word_index + 1, state_index + 1);
    } else {
      prob *= states[state_index][word[word_index]] / (double)states[state_index]['%'];
      double sub_prob = 0.0;
      int remaining_letters = word.size() - 1 - word_index;
      for (int i = state_index + 1; i <= states.size() - remaining_letters; i++) {
        sub_prob += get_probability_helper(word, branches, word_index + 1, i);
      }
      return prob * sub_prob;
    }
  }

  string normalize_strings(string& word) {
    return "$" + word;
  }

  pair<string, vector<bool>> normalize_strings_and_create_branch(string& word) {
    vector<bool> branches(word.size() + 3, false);
    string new_word = "$";
    for (int i = 0; i < word.size(); i++) {
      if (word[i] == '%'){
        branches[i] = true;
        continue;
      }
      new_word += word[i];
    }
    return {new_word, branches};
  }
};


int main(){

  ifstream file_words("word-set.txt");
  ifstream file_queries("query-set.txt");

  SingleLetterHMM hmm(13);
  string word;
  while (file_words >> word) {
    cout << "Adding " << word << endl;
    hmm.add_word(word);
  }

  while (file_queries >> word) {
    cout << "The probabilty of " << word << " is " << hmm.get_probability(word) << endl;
  }
}
