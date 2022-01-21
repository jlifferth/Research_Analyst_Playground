import time

start = time.time()
with open('/Users/jonathanlifferth/Downloads/H2_2.clean.fq', 'r') as in_file:
    A = 0
    T = 0
    C = 0
    G = 0
    row = 0
    for line in in_file:
        line = line.strip()
        # print(row)
        # print(line)
        if row == 1:
            for nucleotide in line:
                # print(nucleotide)
                if nucleotide == 'A':
                    A += 1
                elif nucleotide == 'T':
                    T += 1
                elif nucleotide == 'C':
                    C += 1
                elif nucleotide == 'G':
                    G += 1
                else:
                    pass
        row += 1
        if row == 4:
            row = 0
        # print(f"A: {A}, T: {T}, C: {C}, G: {G}")

total = A + T + C + G
GC_percentage = (C + G) / total

print(f"A: {A}, T: {T}, C: {C}, G: {G}")
print(f"total: {total}")
print(f"GC_percentage: {GC_percentage}")
end = time.time()

print(f"Runtime: {end - start}")
