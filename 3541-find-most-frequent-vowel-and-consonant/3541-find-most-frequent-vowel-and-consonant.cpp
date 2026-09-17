class Solution {
public:
    int maxFreqSum(string s) {
         map<char,int>mp;
        map<char,int>mpp;
        for(int i=0;i<s.size();i++){
            if(s[i] =='a' || s[i] =='e'||s[i] == 'i'||s[i]=='o'||s[i]=='u'){
                mp[s[i]]++;
            }
            else mpp[s[i]]++;
        }
        int maxmp = 0;
        int maxmpp = 0;
        for(auto x: mp){
            maxmp = max(maxmp,x.second);
        }
        for(auto y: mpp){
            maxmpp = max(maxmpp,y.second);
        }
        int t = maxmp+maxmpp;
        return t;
    }
};