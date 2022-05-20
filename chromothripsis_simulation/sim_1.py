import random

# simple demonstration of concept for chromothripsis simulation
# all steps of chromothripsis are determined randomly

genes = ['AAAAAAAAAA', 'TTTTTTTTTT', 'CCCCCCCCCC', 'GGGGGGGGGG']

# genome contains each gene with a total of 10 nucleotides of non-coding regions
non_code_region = '..........'

# create genome with all genes padded with non-coding regions
genome = non_code_region + non_code_region.join(genes) + non_code_region

print('Genes')
print([gene for gene in genes])
print(genome)


def run_chromothripsis(gene_list, genome_str, _print=False):
    # number of possible breaks is based on the number of genes found in genome
    # no biological basis for this number, used purely for exploratory simulation
    # in real models, number of breaks is significantly lower

    num_breaks = random.randint(1, len(gene_list))
    break_indices = [random.randint(0, len(genome_str)) for _break in range(num_breaks)]
    break_indices.sort()

    # split the genome into list of all nucleotides to allow break insertions
    genome_list = list(genome_str)

    # insert break indices into genome list
    for i in break_indices:
        genome_list.insert(i, '_')

    genome_with_break_indices = ''.join(genome_list)

    # shatter genome into fragments and shuffle randomly
    fragments = genome_with_break_indices.split('_')
    random.shuffle(fragments)

    # allow fragments to invert
    inverted_fragments = [fragment[::[-1, 1][random.randrange(2)]] for fragment in fragments]

    # allow fragments to be lost to the cell
    lost_fragments = []
    for i in range(len(inverted_fragments)):
        if random.choice([True, False]):
            lost_fragments.append(inverted_fragments[i])
    remaining_fragments = [fragment for fragment in inverted_fragments if fragment not in lost_fragments]

    # recombine fragments to form new genome
    new_genome = ''.join(remaining_fragments)
    nucs_lost = len(genome) - len(new_genome)

    # print optional report
    if _print:
        print('Number of breaks')
        print(num_breaks)
        print('Break indices')
        print(break_indices)
        print(genome_with_break_indices)
        print('Fragments')
        print(fragments)
        print('Shuffled fragments')
        print(fragments)
        print('Inverted Fragments')
        print(inverted_fragments)
        print('Lost_fragments')
        print(lost_fragments)
        print(nucs_lost, ' Nucleotides lost')
        print('Original genome, length : ', len(genome))
        print('New genome length: ', len(new_genome))
        print(new_genome)

    return new_genome


# run_chromothripsis(gene_list=genes, genome_str=genome)
