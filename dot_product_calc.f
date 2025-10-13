C This file contains a Fortran subroutine to calculate the dot product of two vectors.
      SUBROUTINE DOT_PRODUCT_CALC(VEC1, VEC2, N, RESULT)
C
C     This subroutine calculates the dot product of two vectors VEC1 and VEC2.
C
C     Parameters:
C     VEC1 (input) : First vector (REAL array of size N)
C     VEC2 (input) : Second vector (REAL array of size N)
C     N    (input) : Number of elements in the vectors (INTEGER)
C     RESULT (output) : The calculated dot product (REAL)
C
      INTEGER N
      REAL VEC1(N), VEC2(N), RESULT
C
      INTEGER I
      RESULT = 0.0
      DO 10 I = 1, N
          RESULT = RESULT + VEC1(I) * VEC2(I)
10    CONTINUE
C
      RETURN
      END