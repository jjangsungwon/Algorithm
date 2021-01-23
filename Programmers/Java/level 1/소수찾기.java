class Solution {
    public int solution(int n) {
        int[] prime = new int[n + 1];
        for(int i = 2; i <= Math.sqrt(n); i++){
            if (prime[i] == 0){
                for(int j = i + i; j <= n; j = j + i){
                    prime[j] = -1;
                }
            }
        }
        int answer = 0;
        System.out.println(prime[2]);
        for(int i=2; i<=n; i++){
            if (prime[i] != -1){
                answer += 1;
            }
        }
        return answer;
    }
}