#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>

//JJangSungWon BaekJoon_2420
int main() {

	long long int N, M;
	long long int result;

	scanf("%lld %lld", &N, &M); //input

	//error check
	if (N < -2000000000 || N > 2000000000)
		return 0;
	if (M < -2000000000 || M > 2000000000)
		return 0;

	if (M > N)
		result = M - N;
	else
		result = N - M;

	printf("%lld", result);

	return 0;
}
