#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>    // qsort 함수가 선언된 헤더 파일

//JJang Sung Won BaekJoon_1026
int compare(const void *a, const void *b)    // 오름차순 비교 함수 구현
{
	int num1 = *(int *)a;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴
	int num2 = *(int *)b;    // void 포인터를 int 포인터로 변환한 뒤 역참조하여 값을 가져옴

	if (num1 < num2)    // a가 b보다 작을 때는
		return -1;      // -1 반환

	if (num1 > num2)    // a가 b보다 클 때는
		return 1;       // 1 반환

	return 0;    // a와 b가 같을 때는 0 반환
}

int main()
{
	int *a, *b, *copy,result=0;
	int N,i,j,temp;

	scanf("%d", &N);

	a = (int*)malloc(sizeof(int) * N);
	b = (int*)malloc(sizeof(int) * N);
	copy = (int*)malloc(sizeof(int) * N);

	for (i = 0; i < N; i++)
		scanf("%d", &a[i]);

	for (i = 0; i < N; i++)
		scanf("%d", &b[i]);

	// 정렬할 배열, 요소 개수, 요소 크기, 비교 함수를 넣어줌
	//qsort(a, sizeof(a) / sizeof(int), sizeof(int), compare);
	//이미 정렬된 배열은 적용하던데 scanf 입력하면 정렬이 안된다..

	for (i = 0; i < N; i++)
		copy[i] = b[i];

	for (i = 0; i < N; i++)
	{
		for (j = i; j < N; j++)
		{
			if(copy[i] < copy[j])
			{
				temp = copy[i];
				copy[i] = copy[j];
				copy[j] = temp;
			}
			if (a[i] > a[j])
			{
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}

	for (i = 0; i < N; i++)
		result += (a[i] * copy[i]);

	printf("%d",result);

	return 0;
}