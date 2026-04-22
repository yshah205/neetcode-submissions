class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

    Map<String, List<String>> ana = new HashMap<> ();
    for (String s : strs) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        String sortedS = new String (charArray);
        ana.putIfAbsent(sortedS, new ArrayList<> ());
        ana.get(sortedS).add(s);
    }   

return new ArrayList<> (ana.values());
    }
}
