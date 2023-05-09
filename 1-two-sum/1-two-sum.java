class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map <Integer, Integer> hashmap = new HashMap<>();
        int[] answer = new int[2];
        for (int i = 0; i < nums.length ; i++){
            if(hashmap.containsKey(target - nums[i])){
              answer[0] = i;
              answer[1] = hashmap.get(target - nums[i]);
              break;
            }
            else
            hashmap.put(nums[i],i);
        }
        return answer;
    }
}