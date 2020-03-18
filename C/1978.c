#include<stdio.h>

int check(int n);
// BaekJoon 1978
int main(void)
{
	int N, i, count = 0;
	int arr[100], flag = 0;

	//input
	scanf("%d", &N);
	for (i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	//check;
	for (i = 0; i < N; i++)
	{
		flag = check(arr[i]);
		if (flag)
			count++;

	}
	printf("%d", count);
	return 0;
}

//¼Ò¼ö check
int check(int n)
{
	int i;
	if (n == 1)
		return 0;

	for (i = 2; i < n; i++)
		if (n%i == 0)
			return 0;
	return 1;
}