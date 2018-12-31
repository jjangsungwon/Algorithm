#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//Jang Sung Won
int main(void)
{
	int case_num;
	int *arr;
	char **ch;
	int i, j;
	int sum = 0;
	int score = 1;
	scanf("%d", &case_num);

	//동적할당
	arr = (int*)malloc(sizeof(int) * case_num);

	ch = (char **)malloc(sizeof(char *) * case_num);

	for (i = 0; i < case_num; i++) {
		ch[i] = (char *)malloc(sizeof(char) * 80);
	}
	for (i = 0; i < case_num; i++) {
		scanf("%s", ch[i]);
	}

	for (i = 0; i < case_num; i++)
	{
		sum = 0;
		score = 1;
		for (j = 0; j < 80; j++) 
		{
			if (ch[i][j] == 0)
				break;

			if (ch[i][j] == 'O') {
				sum += score;
				score++;
			}
			else {
				score = 1;
			}
		}
		arr[i] = sum;
	}
	
	for (i = 0; i < case_num; i++)
		printf("%d\n", arr[i]);

	return 0;
}
