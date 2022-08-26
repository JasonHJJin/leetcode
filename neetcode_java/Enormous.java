class Enormous {

    public static int[] twoSum(int[] nums, int target) {
        int [] result = {};
        int [] temp = nums;
        int length = nums.length;
        
        for (int i = 0; i < length; i++) {
            
            for (int j = 0; j < length; j++) {
                
                if(i==j){continue;}
            
                if(nums[i] + temp[j] == target){
                
                }

            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println("Hellow");
    }
}