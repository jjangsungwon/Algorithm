#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

//JJang Sung Won BaekJoon_2309

int main(int argc, char *argv[])
{
	int i, j,arr[9];
	int sum = 0;
	int check,temp;
	int c[2];

	for (i = 0; i < 9; i++) {
		scanf("%d", &arr[i]);
		sum += arr[i];
	} //모든 수를 더한다.

	check = sum - 100; //check를 두 수로 만들어지게 하는 것만 구하면 됨.

	for(i=0;i<9;i++)
		for(j=0;j<9;j++)
			if (arr[i] + arr[j] == check)
			{
				c[0] = arr[i];
				c[1] = arr[j];
			}
	//두 수 찾기
	//printf("%d %d\n", c[0], c[1]);
	for (i = 0; i < 9; i++)
	{
		if (arr[i] == c[0] || arr[i] == c[1])
			arr[i] = -1; //-1로 표시.
	}

	for (i = 0; i < 9; i++)
	{
		for (j = 0; j < 9; j++)
		{
			if (arr[i] != -1 || arr[j] != -1) {
				if (arr[i] < arr[j])
				{
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
	}

	for (i = 0; i < 9; i++) {
		if (arr[i] != -1)
			printf("%d\n", arr[i]);
	}

	//system("pause");
	return 0;
}