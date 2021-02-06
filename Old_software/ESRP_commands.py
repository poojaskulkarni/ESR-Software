# Baseline Function - Performs Baseline normalization of the spectrum
 def baseline(in_reg):
    out_reg = in_reg
    #calculate averages
   Avg1 = 0
   Avg2 = 0
   #define number of samples
   Navg =20
  for I in range (1, Navg):
  Avg1 = Avg1+R[Rn,I]
 Avg2 = Avg2+R[Rn,Par[Rn,1]-I+1]
Av1 = Av1/Navg
Av2 = Av2/Navg
  Dif = (Avg2-Avg1)/Par[Rn,1]:no
 for I in range(1 , Par[Rn,1]):
  R[Rn,I] = R[Rn,I]-Avg1-I*Dif
 NEXT I
    return out_reg
    
 # Integrate Function - Performs double integrals of the spectrum
 def integrate(in_reg):
 
    integ_val = 0
     Aux[Par[Rn,1]]
   H = 0
  for I in range(1 , Par[Rn,1]):
  H = H+R[Rn,I]
  Aux[I] = H
  CALL P_MAX(Aux,H,Nh)
  K = 0
 Lsum1 = 0
 Lsum2 = 0
 for I in range( Nh, Par[Rn,5]) STEP -1
 Lsum1 = Lsum1+R[Rn,I]
 Lsum2 = Lsum2+R[Rn,I]*K
K = K+1
 K = 0
 Rsum1 = 0
 Rsum2 = 0
 for  I in range ( Nh,Par[Rn,6])
 Rsum1 = Rsum1-R[Rn,I]
 Rsum2 = Rsum2+R[Rn,I]*K
 K = K+1
 Ss = (Lsum2-Rsum2)*Par[Rn,3]^2
 HOME
 PRINT "DOUBLE INTEGRAL = ";Ss
 PRINT "LEFT AND RIGHT FIRST INTEGRALS = ";Lsum1,Rsum1
 Par[Rn,4] = Ss
    return integ_val
    
# Find Function -
sum1 = 0
sum2 = 0
 for I in range (1, Navg):
  sum1 = sum1+R[Rn,I]+R[Rn,Par[Rn,1]-I+1]
   sum2 = sum2+R[Rn,I]*R[Rn,I]+R[Rn,Par[Rn,1]-I+1]*R[Rn,Par[Rn,1]-I+1]

 Avg = S1/2/Navg
Delta = SQR((S2-2*Navg*Avg*Avg)/2/Navg)
 Thr = 2.5*Delta
 for I in range(1 , Par[Rn,1])
  Fr[I] = R[Rn,I]
 CALL P_CROSS(Fr,Thr) RETURN N1
   Thr = -Thr
  CALL P_CROSS(Fr,Thr,1,-Par[Rn,1]) RETURN N2
  Par[Rn,5] = N1
  Par[Rn,6] = N2