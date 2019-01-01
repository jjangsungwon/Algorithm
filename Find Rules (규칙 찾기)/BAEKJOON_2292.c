#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//Jang Sung Won

int main(void)
{
	// 1锅规 1 (1)
	// 2锅规 2 3 4 5 6 7 (6)
	// 3锅规 8 9 10 11 12 13 14 15 16 17 18 19 (12)
	// 4锅规 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 (18)
	// 5锅规 38 ~ 24 (61)
	int n;
	int check = 1;
	int check2 = 0;
	int count = 2;
	//input
	scanf("%d", &n);

	//error check
	if (n < 1 || n > 1000000000)
		return 0;
 
	while (1)
	{
		if (n == 1) {
			printf("1");
			return 0;
		}
		else if (n <= ((6 * check)+1)) {
			printf("%d",count);
			return 0;
		}
		// 1 3 6
		check= check+2+check2;
		check2++;
		count++;
	}
	
	// 1 / 6 / 12 / 18 / 24 / 30 / 36 / 42
	// 1 / 2 /  3 /  4 /  5 /  6 /  7 /  8
	return 0;
}