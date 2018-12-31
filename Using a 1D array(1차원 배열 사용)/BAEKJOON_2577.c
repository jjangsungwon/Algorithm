#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//Jang Sung Won
int main(void)
{
	int arr[10] = { 0, };
	int num1, num2, num3;
	int result = 0;
	int div = 1;
	int len = 0;
	int flag;
	int i;

	//input
	scanf("%d", &num1);
	scanf("%d", &num2);
	scanf("%d", &num3);

	//error check
	if ((num1 < 100) || (num2 < 100) || (num3 < 100))
		return;
	if ((num1 >= 1000) || (num2 >= 1000) || (num3 >= 1000))
		return;

	result = num1 * num2 * num3;

	//자릿수 구하기
	while (1) {
		flag = result / div;
		if (flag) {
			div *= 10;
			len++;
		}
		else {
			div /= 10;
			break;
		}
	}
	
	for (i = len; i >= 1; i--) {
		flag = result / div;
		result = result % div;
		arr[flag]++;
		div /= 10;
	}
	
	for (i = 0; i <= 9; i++)
		printf("%d\n", arr[i]);
	return 0;
}
