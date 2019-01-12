#include<stdio.h>

int check(int n);
// BaekJoon 4948
int main(void)
{
	int n, i, count = 0;
	int flag = 0, flag2 = 1;
	int len = 0;
	int arr[123456];
	//input
	scanf("%d", &n);
	if (n > 123456)//error check
		return 0;

	while (n > 0)//자연수에 대해서 입력받는다.
	{
		if (n > 123456) //error check
			return 0;

		//check;
		for (i = n+1; i <= 2 * n; i++){
			if (check(i)) {
				count++;
			}
		}
		arr[len++] = count;
		count = 0;
		scanf("%d", &n);
	}
	
	for (i = 0; i < len; i++)
		printf("%d\n", arr[i]);
	
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
