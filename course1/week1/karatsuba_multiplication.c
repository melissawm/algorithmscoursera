#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

char * string_operate(char *s, char *r, char op);
char * string_pad(char *s, int n, char side);

int main() {

  /* Variable declarations */
  int n, m, half;

  /* Numbers we wish to multiply */
  char pi[65];
  char exp[65];

  strcpy(pi, "3141592653589793238462643383279502884197169399375105820974944592");
  strcpy(exp, "2718281828459045235360287471352662497757247093699959574966967627");
  n = strlen(pi);
  m = strlen(exp);

  printf("pi   = %s\n", pi);
  printf("pi has length %d\n", n);
  printf("exp  = %s\n", exp);
  printf("exp has length %d\n", m);
  
  half = ceil(n/2);
  printf("half = %d\n", half);

  char *result = string_operate(pi, exp, 'B');
  printf("result = %s\n", result);

  char* result_padded = (char*)malloc(strlen(pi)+n+3);
  result_padded = string_pad(pi, 3, 'L');

  /* To compare: strncmp(string1, string2, nbcharstobecompared) */
  
  return 0;
}

char *string_operate(char *s, char *r, char op) {
    char* result = (char*)malloc(strlen(s) + strlen(r)+3);//new string with enough space for both and \0
    if (op == 'A') {
        // we are adding the two strings
        //printf("s = %s\n", s);
        strcpy(result, s);
    } else if (op == 'S') {
        // we are subtracting the two strings
        //printf("r = %s\n", r);
        strcpy(result, r);
    } else {
        printf("Warning: wrong operation for strings.\n");
        // strncat(dest, src, howmanychars)
        strcpy(result, r);
        strncat(result, s, strlen(result));
    }
    return result;
}

char * string_pad(char *s, int n, char side) {
    int i;
    char temp[strlen(s)+n+1];
    char zeros[n];
    for (i=1; i<=n; i++) {
        strncat(zeros, "0", 2);
    }
    if (side == 'L') {
        strncat(temp, zeros, n);
        strncat(temp, s, strlen(s));
    } else if (side == 'R') {
        strncat(temp, s, strlen(s));
        strncat(temp, zeros, n);
    } else {
        printf("Wrong padding option");
    }
    printf("apos padding: %s\n", temp);
    return temp;
}