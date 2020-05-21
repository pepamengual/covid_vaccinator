### Previous steps:
### 1) Download mhcflurry through: pip3 install mhcflurry
### 2) Download mhcflurry models through: mhcflurry-downloads fetch models_class1_presentation

from mhcflurry import Class1PresentationPredictor

def load_predictor():
    """
    Loads the mhcflurry predictor of class I alleles
    """
    predictor = Class1PresentationPredictor.load()
    return predictor

def supported_alleles(predictor):
    """
    Get all alleles that can be predicted with this mhcflurry version
    """
    alleles = predictor.supported_alleles
    return alleles

def filter_human_alleles(alleles):
    """
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

def main():
    predictor = load_predictor()
    alleles = supported_alleles(predictor)
    human_alleles = filter_human_alleles(alleles)

main()







