#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>

/*
	BAEKJOON_2941
	GITHUB : JJANGSUNGWON
	c,d,l,n,s,z로 시작하지 않는 것은 1글자로 바로 처리한다. (크게 if문 2개로 나눈다)
	해당 글자로 시작하였을때 다음 글자를 보고, 해당하는 것이 있으면 크로아티아 문자로 확인, 아니면 처음꺼 1글자로 인식하고 진행
*/
char Croatia_Language[8][100] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };

int main(void)
{
	int length, count=0, index=0;
	char word[200];

	//input
	scanf("%s", word);

	// word_length
	length = strlen(word);

	// word_count 
	while (length > 0)
	{
		switch (word[index]) {
		case 'c' : 
			if (word[index + 1] == '=' || word[index + 1] == '-')
			{
				index = index + 2;
				length = length - 2;
			}
			else
			{
				index = index + 1;
				length = length - 1;
			}
			break;
		case 'd':
			if (word[index + 1] == 'z' && word[index + 2] == '=')
			{
				index = index + 3;
				length = length - 3;
			}
			else if(word[index +1] =='-')
			{
				index = index + 2;
				length = length - 2;
			}
			else
			{
				index = index + 1;
				length = length - 1;
			}
			break;
		case 'l':
			if (word[index + 1] == 'j' )
			{
				index = index + 2;
				length = length - 2;
			}
			else
			{
				index = index + 1;
				length = length - 1;
			}
			break;
		case 'n':
			if (word[index + 1] == 'j')
			{
				index = index + 2;
				length = length - 2;
			}
			else
			{
				index = index + 1;
				length = length - 1;
			}
			break;
		case 's':
			if (word[index + 1] == '=')
			{
				index = index + 2;
				length = length - 2;
			}
			else
			{
				index = index + 1;
				length = length - 1;
			}
			break;
		case 'z':
			if (word[index + 1] == '=')
			{
				index = index + 2;
				length = length - 2;
			}
			else
			{
				index = index + 1;
				length = length - 1;
			}
			break;
		default :
			index = index + 1;
			length = length - 1;
		}
		count++;
	}

	printf("%d", count);

	return 0;
}