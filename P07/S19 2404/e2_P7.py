gene = ['FRAT1', 'ADA', 'FXN', 'RNU6_269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
id = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296',
      'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']

genes = dict(zip(gene, id))

print("Dictionary of genes")
print(f"There are {len(genes)} in the dictionary")
print(genes)
