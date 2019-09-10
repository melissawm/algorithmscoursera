#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <sys/param.h>

char * string_operate(char *s, char *r, char op);
char * string_pad(char *s, int n, char side);

int main() {

  // Variable declarations
  int n, m, half;

  // Numbers we wish to multiply
  // Why can't we do char pi[4] = "3141";?
  char pi[] = "31415"; //92653589793238462643383279502884197169399375105820974944592";
  char exp[] = "2718"; //281828459045235360287471352662497757247093699959574966967627";

  n = strlen(pi);
  m = strlen(exp);

  printf("pi   = %s\n", pi);
  printf("pi has length %d\n", n);
  printf("exp  = %s\n", exp);
  printf("exp has length %d\n", m);
  
  half = ceil(n/2);
  printf("half = %d\n", half);

  // Let's first try to add the two strings
  char * result = string_operate(pi, exp, 'A');
  printf("result = %s\n", result);

  //char * result_padded = (char*)malloc(2*n+3);
//  char * result_padded = string_pad(pi, 3, 'L');

  /* To compare: strncmp(string1, string2, nbcharstobecompared) */
  
  return 0;
}

char * string_operate(char * s, char * r, char op) {

    int lens = strlen(s);
    int lenr = strlen(r);
    int carry = 0;
    int i, partialvalue, imax;

    char * result = (char*)malloc(lens + lenr + 1);//new string with enough space for both and \0
    char * partial = (char*)malloc(lens + lenr + 1);//new string with enough space for both and \0

    if (lens > lenr) {
        // Pad r with zeros to the left
        strcpy(result, r);
        string_pad(result, lens-lenr, 'L');
        printf("result after padding: %s\n", result);
    } else if (lens < lenr) {
        // Pad s with zeros to the left
        strcpy(result, s);
        string_pad(result, lenr-lens, 'L');
    }

    if (op == 'A') {
        // we are adding the two strings
        strcpy(result, s);
        strcat(result, r);

        if (lens > lenr) {
            imax = lens;
        } else {
            imax = lenr;
        }

        for (i=imax-1; i>=0; i--) {
            //partial = str(int(s[i])+int(r[i]) + carry);
            partialvalue = strtol(&s[i], NULL, 10) + strtol(&r[i], NULL, 10) + carry;
            sprintf(partial, "%d", partialvalue);
            printf("i = %d\n", i);
            printf("partial = %d\n", partial);
            //if len(partial) == 2:
            //    carry = int(partial[0])
            //else:
            //    carry = 0
            //result = partial[-1] + result
        }
//    } else if (op == 'S') {
//        // we are subtracting the two strings
//        //printf("r = %s\n", r);
//        strcpy(result, r);
////    for i in range(max(lens, lenr)-1, -1, -1):
////    if int(s[i])-carry >= int(r[i]):
////    partial = str(int(s[i])-carry-int(r[i]))
////    carry = 0
////    else:
////    partial = str(10+(int(s[i])-carry)-int(r[i]))
////    carry = 1
////    result = partial[-1] + result
//    } else {
//        printf("Warning: wrong operation for strings.\n");
//        // strncat(dest, src, howmanychars)
//        strcpy(result, r);
//        //strncat(result, s, strlen(result));
    }
////    if carry != 0:
////    result = str(carry)+result
////    return result
    return result;

}

char * string_pad(char *result, int n, char side) {
    int i;
    char zeros[n];
    char temp[strlen(result)];

    printf("n = %d\n", n);
    for (i=0; i<n; i++) {
        zeros[i] = '0';
    }
    if (side == 'L') {
        strcpy(temp, result);
        strcpy(result, zeros);
        strcat(result, temp);
    } else if (side == 'R') {
        strcat(result, zeros);
    } else {
        printf("Wrong padding option");
    }
    return result;
}