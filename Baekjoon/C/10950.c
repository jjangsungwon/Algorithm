#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdlib.h>

//JJangSungWon BaekJoon_10950
int main(void)
{
	int n;
	int *a, *b;

	scanf("%d", &n); //input test number

	a = (int*)malloc(sizeof(int) * n);
	b = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		scanf("%d %d", &a[i], &b[i]);

	for (int i = 0; i < n; i++)
		printf("%d\n", a[i] + b[i]);

	free(a);
	free(b);
	//system("pause");
	return 0;
}