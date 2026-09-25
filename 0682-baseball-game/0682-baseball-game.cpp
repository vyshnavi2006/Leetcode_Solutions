class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int>v;
        for(int i=0;i<operations.size();i++){
            if(operations[i] == "+"){
                int n = v.size();
                v.push_back(v[n-1]+v[n-2]);
            }
            else if(operations[i]=="D"){
                v.push_back(v.back()*2);
            }
            else if(operations[i]=="C"){
                v.pop_back();
            }
            else{
                v.push_back(stoi(operations[i]));
            }
        }
        int sum =0;
        for(int i=0;i<v.size();i++){
            sum+=v[i];
        }
        return sum;
    }
};