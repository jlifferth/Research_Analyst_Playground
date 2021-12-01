import scipy.io
mat = scipy.io.loadmat('MCMC_para.mat')
mat = str(mat)

with open('MCMC_para.txt', 'w') as out_file:
    out_file.write(mat)
