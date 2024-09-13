import math
import random
import csv

def get_random_point(dim):
    return tuple(random.random() for _ in range(dim))

def distance_euclide(p1, p2):
    dists = []
    for p_1, p_2 in zip(p1, p2):
        dists.append((p_1 - p_2)**2)
    return math.sqrt(sum(dists))

def save_to_csv(points, header = [], scores = None, fichier = '../dataset/dataset.csv'):
    with open(fichier, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(header)
        if scores is not None:
            for point, score in zip(points, scores):
                writer.writerow((*point, score))
        else:
            for point in points:
                writer.writerow(point)
