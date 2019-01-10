#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//Jang Sung Won
int main(void)
{
	int arr[9] = { 0, };
	int i;
	int flag1 = 0; // ascending
	int flag2 = 0; // descending
	int flag3 = 0; // mixed

	//input
	for(i=1;i<=8;i++)
		scanf("%d", &arr[i]);

	//check (case 1 ascending)
	for (i = 1; i <= 7; i++) {
		if (arr[i] < arr[i + 1]) {
			if (i == 7) {
				printf("ascending");
				return 0;
			}
			continue;
		}
		else
			break;
	}
	
	// (case 2 descending)
	for (i = 1; i <= 7; i++) {
		if (arr[i] > arr[i + 1]) {
			if (i == 7) {
				printf("descending");
				return 0;
			}
			continue;
		}
		else
			break;
	}

	// else
	printf("mixed");
	return 0;
}
