
# Baseline: ten buttons, saves baseline() output (pooja) to same register, updates plot
def baseline(in_reg):
    out_reg = in_reg
    return out_reg


# Find: ten buttons, saves two find() outputs (pooja) to same register struct, updates plot
def find(in_reg):
    n_left = 0
    n_right = len(in_reg)
    return n_left, n_right


# Integrate: ten buttons, saves integrate() output (pooja) to same register struct
# error message if first integrals are >15% difference.
# display double integral next to integrate button
def integrate(in_reg):
    integ_val = 0
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
    out_weights = [0 for i in range(len(basis_reg_2Darray))]
    return out_reg, out_weights
