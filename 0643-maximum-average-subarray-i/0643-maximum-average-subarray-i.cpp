class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum = 0;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        double avg = sum/k;
        double avg1 =0;
        int i=0;
        int j=k;
        while(j<nums.size()){
           sum+=nums[j];
           sum-=nums[i];
           i++;
           j++;
           avg1 = sum/k;
           if(avg1>avg) avg = avg1;
        }
        return avg;
    }
};