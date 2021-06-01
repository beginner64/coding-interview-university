#include <limits.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    printf("%d\n", INT_MAX);
    printf("%d\n", INT_MIN);
    printf("%d\n", CHAR_MAX);
    printf("%d\n", CHAR_MIN);
    printf("%d\n", SHRT_MAX);
    printf("%d\n", SHRT_MIN);
    printf("%ld\n", LONG_MAX);
    printf("%ld\n", LONG_MIN);

    // printf("%d\n", INT_MAX);
    // printf("%d\n", INT_MIN);
    printf("%d\n", UCHAR_MAX);
    // printf("%d\n", UCHAR_MIN);
    // printf("%d\n", SHRT_MAX);
    // printf("%d\n", SHRT_MIN);
    // printf("%ld\n", LONG_MAX);
    // printf("%ld\n", LONG_MIN);
    printf("%d\n", 2 % 10);
    int i;
    char c;
    i = -4;
    c = 'a';
    c = i;
    i = c;
    printf("%d\n", c);
    printf("%d\n", i);
    /* code */
    return 0;
}
