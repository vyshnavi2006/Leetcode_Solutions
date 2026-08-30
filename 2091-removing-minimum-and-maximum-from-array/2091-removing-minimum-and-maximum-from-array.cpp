class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int maxi = *max_element(nums.begin(),nums.end());
        int mini = *min_element(nums.begin(),nums.end());
        int n=nums.size();
        int f=-1,l=-1;
        for(int i=0;i<n;i++){
            if(nums[i] == maxi) f=i;
            if(nums[i]==mini) l=i;
        }
        int fst = min(f,l);
        int sec = max(f,l);
        int front = sec+1;
        int back = n-fst;
        int both = (fst+1)+(n-sec);
        return min({front,back,both});
    }
};