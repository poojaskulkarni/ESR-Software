
# Baseline:Performs Baseline normalization of the spectrum. ten buttons, saves baseline() output (pooja) to same register, updates plot
def baseline(in_reg):
    out_reg = in_reg
    #calculate averages
    Avg1 = 0
    Avg2 = 0
    Navg = 20
    for I in range (1, Navg):
       Avg1 = Avg1+in_reg[I]
       Avg2 = Avg2+in_reg[reg_size-I+1]
    Avg1 = Avg1/Navg
    Avg2 = Avg2/Navg
    Dif = (Avg2-Avg1)/(reg_size)
    for I in range(reg_size):
        in_reg[I] = in_reg[I]-Avg1-I*Dif
    return out_reg

# Find: ten buttons, saves two find() outputs (pooja) to same register struct, updates plot
def find(in_reg):
    n_left = 0
    n_right = len(in_reg)
    return n1, n2


# Integrate:Performs double integrals of the spectrum. ten buttons, saves integrate() output (pooja) to same register struct
# error message if first integrals are >15% difference.
# display double integral next to integrate button
def integrate(in_reg, reg_size, n1, n2, fremy):
    integ_val = 0
    H = 0
    for I in range(reg_size):
        H = H + in_reg[I]
        Aux[I] = H
    Aux = max(H)
    K = 0
    Lsum1 = 0
    Lsum2 = 0
    for I in range( Nh, n1, -1):
        Lsum1 = Lsum1+in_reg[I]
        Lsum2 = Lsum2+in_reg[I]*K
        K = K+1
    K = 0
    Rsum1 = 0
    Rsum2 = 0
    for  I in range ( Nh,n2):
        Rsum1 = Rsum1-in_reg[I]
        Rsum2 = Rsum2+in_reg[I]*K
        K = K+1
    integ_val = (Lsum2-Rsum2)*Par[Rn,3]^2
    return integ_val


# Subtract: one button, creates pop up window asking for
# input registers
# weighting factorssub
# output register
# then stores subtract() output (Pooja) into output register
def subtract(in_reg_2Darray, weights_array):
    out_reg = in_reg_2Darray[1]
    return out_reg


# Fit: one button, creates pop up window asking for
# register to be fitted
# basis registers
# boundary points of fitting
# output register
# then stores fit() output (Pooja) into output register
def fit(in_reg, basis_reg_2Darray, start_index, end_index):
    out_reg = in_reg
    start_index = start_index-1
    out_weights = [0 for i in range(len(basis_reg_2Darray))]
    return out_reg, out_weights
