#define _CRT_SECURE_NO_WARNINGS

//BaekJoon_1016
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

#define TRUE 1
#define FALSE 0

clock_t start, end;

long long int prime[2000000] = { 0, };
long long int square[2000000] = { 0, };
long long int p [2000000] = { 0, };

int p_size = 0, s_size = 0;

void fill(long long max)
{
	unsigned long long i,j;
	long long int temp;
		
	temp = sqrtl((long double)max);

	prime[0] = prime[1] = TRUE;

	for (i = 2; i <= temp; i++)
	{
		if(prime[i])
			continue;

		for (j = i * 2; j <= temp; j += i)
		{
			if (prime[j])
				continue;
			prime[j] = TRUE;
		}

		p[p_size++] = i * i;
	}

}

int main(void)
{
	//start = clock();
	
	int count = 0;
	long long int min, max;
	long long int i,j,t_min, t_max;

	//input
	scanf("%lld %lld", &min, &max);

	fill(max);

	for (i = 0; i < p_size; i++)
	{
		if (min % p[i])
		{
			t_min = ((long long int)(min / p[i]) + 1) * p[i];
		}
		else
			t_min = min;

		t_max = (long long int)(max / p[i]) * p[i];

		for (j = t_min; j <= t_max; j += p[i])
		{
			//중복방지
			if (square[j - min])
				continue;
			square[j - min] = TRUE;
		}
	}

	for (i = 0; i <= max - min; i++)
		if (!square[i])
			count++;

	printf("%d", count);

	//end = clock();
	//printf("%f", (double)end - start);
	return 0;
}