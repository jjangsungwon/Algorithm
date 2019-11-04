#define _CRT_SECURE_NO_WARNINGS

//Baek_Joon_15891
#include<stdio.h>

int main(void) {
	int N;
	scanf("%d", &N);
	int arr[5] = { 65, 17, 4, 4, 64 };

	printf("%d", arr[N - 1]);
	return 0;
}