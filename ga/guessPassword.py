import datetime
import random
geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello world"


def genrate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), geneSet)
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)


def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes else newGene
    return ''.join(childGenes)


def display(guess, fitness, gen):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}\t{3}".format(guess, fitness, str(timeDiff), gen))


random.seed()
startTime = datetime.datetime.now()
bestParent = genrate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent, bestFitness, 1)

g = 1
while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    g += 1
    display(child, childFitness, g)

    if bestFitness >= childFitness:
        continue

    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
