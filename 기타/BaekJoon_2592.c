#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJangSungWon BaekJoon_2592
int main(void)
{
	int i, sum=0,num;
	int count[1000] = { 0, };
	int max = 0;
	int temp;

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &num);
		sum += num;
		count[num]++;
	}

	printf("%d\n", sum / 10);
	
	for (i = 0; i < 1000; i++)
	{
		if (max < count[i]) {
			max = count[i];
			temp = i;
		}
	}
	printf("%d", temp);
	//system("pause");
	return 0;
}