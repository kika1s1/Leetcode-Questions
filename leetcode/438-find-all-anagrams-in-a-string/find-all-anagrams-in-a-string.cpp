
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.size() < p.size()){
            return result;
        }

        vector<int> p_count(26, 0), s_count(26, 0);
        for (char c : p) p_count[c - 'a']++;
        
        for (int i = 0; i < s.size(); i++) {
            s_count[s[i] - 'a']++;
            if (i >= p.size()) s_count[s[i - p.size()] - 'a']--;
            if (s_count == p_count) result.push_back(i - p.size() + 1);
        }
        
        return result;
    }
};