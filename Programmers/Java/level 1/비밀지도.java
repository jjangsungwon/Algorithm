package practice;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        char[][] maps = new char[n][n];
        
        // arr1, arr2 maps에 대입
        for(int i=0; i<n; i++){
            String binary_1 = binary(arr1[i], n);
            for(int j=0; j<n; j++){
                if(maps[i][j] == '1'){
                    continue;
                }else{
                    maps[i][j] = binary_1.charAt(j);
                }
            }
            String binary_2 = binary(arr2[i], n);
            for(int j=0; j<n; j++){
                if(maps[i][j] == '1'){
                    continue;
                }else{
                    maps[i][j] = binary_2.charAt(j);
                }
            }
        }
        String[] answer = new String[n];
        for(int i=0; i<n; i++){
            String temp = "";
            for(int j=0; j<n; j++){
                if(maps[i][j] == '0'){
                    temp += " ";
                }else{
                    temp += "#";
                }
            }
            answer[i] = temp;
        }
        return answer;
    }
    
    // 2진수 변환 함수
    public String binary(int n, int size){
        String result = "";
        while(n != 0){
            result = n % 2 + result;
            n /= 2;
        }
        for(int i=size - result.length(); i>0; i--){ // 공백 0으로 채우기
            result = "0" + result;
        }
        return result;
    }
}