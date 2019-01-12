#include<stdio.h>

int check(int n);
// BaekJoon 2581
int main(void)
{
	int n1,n2, i, count = 0;
	int arr[100], flag = 0,flag2=1,min,sum=0;

	//input(range)
	scanf("%d %d", &n1, &n2);

	//error check
	if (n1 > 10000 || n2 > 10000)
		return;
	if (n1 < 1 || n2 < 1 )
		return 0;
	if (n1 > n2)
		return 0;

	//check;
	for (i = n1; i <= n2; i++)
	{
		flag = check(i);
		if (flag) {
			if (flag2) { //제일 처음 찾는 소수를 최솟값 가정
				min = i;
				flag2 = 0;
			}
			if (min > i)
				min = i;
			sum += i;
		}

	}
	if (sum == 0)
		printf("-1");
	else
		printf("%d\n%d", sum,min);
	return 0;
}

//소수 check
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
//101
