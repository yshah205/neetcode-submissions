class Solution {
    public int[] twoSum(int[] numbers, int target) {

    Map<Integer, Integer> twosum = new HashMap<>();


    for (int k = 0; k < numbers.length; k++){
        twosum.put(numbers[k], k);
    }
    
    for (int i = 0; i < numbers.length; i++){

    int secondNum = target - numbers[i];
    Integer j = twosum.get(secondNum); 
    if (twosum.containsKey(secondNum)){
     return new int [] {i+1, j+1};
     }  
    }
     return new int [] {-1, -1};
    }

    }
