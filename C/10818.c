#define _CRT_SECURE_NO_WARNINGS

//Baek_Joon_10818
#include<stdio.h>

int main(void)
{
	int N;
	int Min, Max;
	int i;
	int num;

	//input
	scanf("%d", &N);

	for (i = 0; i < N; i++){
		scanf("%d", &num);

		//inital value
		if (i == 0) {
			Min = num;
			Max = num;
		}
		else{
			if (Min > num)
				Min = num;
			else if (Max < num)
				Max = num;
		}
	}

	//print
	printf("%d %d", Min, Max);

	return 0;
}