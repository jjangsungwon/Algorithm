import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0; i<commands.length; i++){
            ArrayList<Integer> list = new ArrayList<Integer>();
            for(int j=commands[i][0]; j<commands[i][1] + 1; j++){
                list.add(array[j - 1]);
            }
            int[] temp = new int[list.size()];
            for(int k=0; k<list.size(); k++){
                temp[k] = list.get(k);
            }
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2] - 1];
        }
        return answer;
    }
}