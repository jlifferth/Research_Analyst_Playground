with open('/Users/jonathanlifferth/Downloads/H2_2.clean.fq', 'r') as in_file:

    total_n = 0
    total_gc = 0
    for line in in_file:
        line = line.strip()
        total_n += 1

        # if total_n < 10:
            # print(line)

