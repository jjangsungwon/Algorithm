#include<stdio.h>

int check(int n);
// BaekJoon 1929
int main(void)
{
	int n1,n2, i, count = 0;
	int flag = 0, flag2 = 1;

	//input(range)
	scanf("%d %d", &n1, &n2);

	//error check
	if (n1 > 1000000 || n2 > 1000000)
		return;
	if (n1 < 1 || n2 < 1 )
		return 0;
	if (n1 > n2)
		return 0;

	//check;
	for (i = n1; i <= n2; i++)
	{
		if (check(i)) {
			printf("%d\n", i);
		}

	}
	
	return 0;
}

//소수 check
int check(int n)
{
	int i;
	if (n == 1)
		return 0;

	//이렇게 다 check할 필요는 없는데..
	for (i = 2; i*i <=  n; i++)
		if (n%i == 0)
			return 0;
	return 1;
}
