import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<arr.length; i++){
            if(arr[i] % divisor == 0){
                list.add(arr[i]);
            }
        }
        if(list.size() == 0){  // 나누어 떨어지는 element가 없으면 배열에 -1을 담아 반환
            int[] answer = {-1};
            return answer;
        }
        else{
            Collections.sort(list); // 오름차순 정렬
            int[] answer = new int[list.size()];
            for(int i=0; i<list.size(); i++){
                answer[i] = list.get(i);
            }
            return answer;
        }
    }
}