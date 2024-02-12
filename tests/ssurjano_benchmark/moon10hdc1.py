import numpy as np
def moon10hdc1(xx):
    ##########################################################################
    # HIGHDON (2010) FUNCTION, C-1
    #####################################################################
    
    x1 = xx[1]
    x7 = xx[7]
    x12 = xx[12]
    x18 = xx[18]
    x19 = xx[19]
    
    term1 = -19.71*x1*x18 + 23.72*x1*x19
    term2 = -13.34*x19**2 + 28.99*x7*x12
    
    y = term1 + term2
    
    return(y)