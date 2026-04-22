class Solution {
    public int characterReplacement(String s, int k) {

    Map <Character, Integer> letter = new HashMap<>();

    int l = 0;
    int maxf = 0;
    int res = 0;

for (int r = 0; r < s.length(); r++) {
    letter.put(s.charAt(r), letter.getOrDefault(s.charAt(r), 0) + 1); 
    
    maxf = Math.max(maxf, letter.get(s.charAt(r)));

    while ((r-l+1) - maxf > k) {
        letter.put(s.charAt(l), letter.get(s.charAt(l)) -1);
        l++;
    }
    res = Math.max(res, r - l + 1);
}
return res;

}

}
