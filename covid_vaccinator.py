### Previous steps:
### 1) Download mhcflurry through: pip3 install mhcflurry
### 2) Download mhcflurry models through: mhcflurry-downloads fetch models_class1_presentation

from mhcflurry import Class1PresentationPredictor

def load_predictor():
    """ Returns an object
    Loads the mhcflurry predictor of class I alleles
    """
    predictor = Class1PresentationPredictor.load()
    return predictor

def supported_alleles(predictor):
    """ Returns a list
    Get all alleles that can be predicted with this mhcflurry version
    """
    alleles = predictor.supported_alleles
    return alleles

def filter_human_alleles(alleles):
    """ Returns a list
    Filter human alleles from all alleles: they start by "HLA-"
    Print how many human alleles can be predicted in each HLA family
    """
    human_alleles = []
    human_groups = {}
    for allele in alleles:
        if allele.startswith("HLA-"):
            group = allele[4]
            human_alleles.append(allele)
            human_groups.setdefault(group, []).append(allele)
    for group, allele_list in human_groups.items():
        print("HLA-{} family with {} predictable alleles".format(group, len(allele_list)))
    return human_alleles

def read_fasta(file_path):
    """ Returns a dictionary
    Converts a fasta file into a dictionary, where key is
    the ID and the value is the sequence of the protein
    """
    data, names, sequences = {}, [], []
    with open(file_path, "r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                name = line[1:]
                names.append(name)
            else:
                sequences.append(line)
    for name, sequence in zip(names, sequences):
        data.setdefault(name, sequence)
    return data

def predicting_binding_affinity(predictor, fasta_data, human_alleles, threshold):
    data = predictor.predict_sequences(
                sequences=fasta_data,
                alleles=human_alleles,
                result="filtered",
                comparison_quantity="affinity",
                filter_value=threshold,
                verbose=0)
    print(data)

def main():
    fasta_file = "fasta.fa"
    predictor = load_predictor()
    alleles = supported_alleles(predictor)
    human_alleles = filter_human_alleles(alleles)
    fasta_data = read_fasta(fasta_file)
    predicting_binding_affinity(predictor, fasta_data, ["HLA-A*02:01"], threshold=500)

main()







