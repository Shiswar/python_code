import math

# This code is entirely the work of Shae Iswar as a submission for the TCS Codevita coding contest

# This function determines whether a matrix contains a square sub-matrix that contains a set of given values.
# Input 1: two space separated integer values (m n) denoting the dimension of the matrix
# inputs 2 -> m: Space separated integer values to denote each row of the matrix
# Next input: Size of the set which contains the values of the sub-matrix (this number is always a square number)
# Final input: Values of the square sub-matrix to be checked

def possible():
    dimensions = input("").split(" ")
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    mat = [ [ 0 for i in range(cols) ] for j in range(rows) ] #build empty matrix

    for r in range(rows):
        row = input("")
        mat[r] = row.split(" ")

    sub_size = int(input(""))
    sub_dim = int(math.sqrt(sub_size))


    sub_vals = input("").split(" ")

    pos = True


    for i in range(rows):
        for j in range(cols):

            if str(mat[i][j]) in sub_vals:

                for k in range(sub_dim):
                    for l in range(sub_dim):
                        if str(mat[i+k][j+l]) in sub_vals:

                            sub_vals.pop(sub_vals.index(str(mat[i+k][j+l])))

                        else:
 
                            return False
                return True
            
            else:
                pass

if possible() == True:
    print("Possible")
else:
    print("Not Possible")
