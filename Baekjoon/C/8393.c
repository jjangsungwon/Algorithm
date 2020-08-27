#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_8393
int main(void)
{
	int i, n;
	int sum = 0;

	scanf("%d", &n);

	if (n < 1 || n>10000)
		return 0;

	for (i = 1; i <= n; i++)
		sum += i;

	printf("%d", sum);
	//system("pause");
	return 0;
}