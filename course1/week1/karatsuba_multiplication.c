#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

char * string_operate(char *s, char *r, char op);
char * string_pad(char *s, int n, char side);

int main() {

  // Variable declarations
  int n, m, half;

  // Numbers we wish to multiply
  // Why can't we do char pi[4] = "3141";?
  char pi[] = "3141"; //592653589793238462643383279502884197169399375105820974944592";
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
    char * result = (char*)malloc(lens + lenr + 1);//new string with enough space for both and \0

    if (lens > lenr) {
        // Pad r with zeros to the left
        strcpy(result, r);
        string_pad(result, lens-lenr, 'L');
        // r = pad(r, lens-lenr)
    } else if (lens < lenr) {
        // Pad s with zeros to the left
        strcpy(result, s);
        string_pad(result, lenr-lens, 'L');
        // s = pad(s, lenr-lens)
    }

    if (op == 'A') {
        // we are adding the two strings
        strcpy(result, s);
        strcat(result, r);
//    } else if (op == 'S') {
//        // we are subtracting the two strings
//        //printf("r = %s\n", r);
//        strcpy(result, r);
//    } else {
//        printf("Warning: wrong operation for strings.\n");
//        // strncat(dest, src, howmanychars)
//        strcpy(result, r);
//        //strncat(result, s, strlen(result));
    }
    return result;
////
////    carry = 0
////    result = ""
////    if op=="add":
////    for i in range(max(lens, lenr)-1, -1, -1):
////    partial = str(int(s[i])+int(r[i])+carry)
////    if len(partial) == 2:
////    carry = int(partial[0])
////    else:
////    carry = 0
////    result = partial[-1] + result
////    elif op=="subtract":
////    for i in range(max(lens, lenr)-1, -1, -1):
////    if int(s[i])-carry >= int(r[i]):
////    partial = str(int(s[i])-carry-int(r[i]))
////    carry = 0
////    else:
////    partial = str(10+(int(s[i])-carry)-int(r[i]))
////    carry = 1
////    result = partial[-1] + result
////    else:
////    raise("Error: wrong string operation!")
////
////    if carry != 0:
////    result = str(carry)+result
////    return result
}

char * string_pad(char *s, int n, char side) {
    int i;
    char zeros[n];
    printf("n = %d\n", n);
    for (i=0; i<=n; i++) {
        zeros[i] = '0';
    }
    printf("%s\n", zeros);
    if (side == 'L') {
        strncat(s, zeros, n);
        strncat(temp, s, strlen(s));
//    } else if (side == 'R') {
//        strncat(temp, s, strlen(s));
//        strncat(temp, zeros, n);
//    } else {
//        printf("Wrong padding option");
    }
    printf("apos padding: %s\n", temp);
    return s;
}