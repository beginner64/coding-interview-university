#include <stdio.h>
/* print Fahrenheit-Celsius table for fahr = 0, 20, ..., 300 
C=(5/9)(F-32)
*/
main()
{
    float fahr, celsius;
    float lower, upper, step;
    lower = 0;
    upper = 300;
    step = 20;
    /* lower limit of temperature scale */
    /* upper limit */
    /* step size */
    fahr = lower;
    /* 
    while (i < j) 
    i = 2 * i;
    */
    printf("Heading \n\n");
    while (fahr <= upper)
    {
        celsius = 5.0 * (fahr - 32.0) / 9.0;
        // printf("%d\t%d\n", fahr, celsius);
        // printf("%3d%5d\n", fahr, celsius);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}