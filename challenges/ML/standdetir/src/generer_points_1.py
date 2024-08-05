import random
import math
import matplotlib.pyplot as plt
import csv

random.seed(0)

def get_random_point(dim):
    return tuple(random.random() for _ in range(dim))

def distance_euclide(p1, p2):
    dists = []
    for p_1, p_2 in zip(p1, p2):
        dists.append((p_1 - p_2)**2)
    return math.sqrt(sum(dists))

def score_point(point):
    #distance du centre
    dist = distance_euclide((0.5 for _ in range(len(point))), point)
    
    #scores non lineaires selon la distance du centre
    #score_ranges = [0.03, 0.1, 0.17, 0.25, 0.32, 0.4, 0.45, 0.5, 1.0]
    score_ranges = [0.08, 0.15, 0.3, 0.45, 1.0]
    scores = [10, 8, 6, 4, 0]

    score = 10
    for i, max_dist in enumerate(score_ranges):
        if dist < max_dist:
            score = scores[i]
            break
    return 10 - score, dist

def save_to_csv(points, scores = None, fichier = '../dataset/dataset.csv'):
    with open(fichier, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        if scores is not None:
            writer.writerow(['x', 'y', 'score'])
            for point, score in zip(points, scores):
                writer.writerow((*point, score))
        else:
            writer.writerow(['x', 'y'])
            for point in points:
                writer.writerow(point)

def creer_dataset_random(taille):
    points = []
    scores = []
    for _ in range(taille):
        point = get_random_point(2) # a remplacer par des points choisis a la main
        points.append(point)
        score, dist = score_point(point)
        scores.append(score)
        
    #plt.scatter([p[0] for p in points], [p[1] for p in points], c=scores)
    #plt.show()
    return points, scores

def creer_dataset_test_standard():
    points = []
    points.append((0.0, 0.0))
    points.append((0.3, 0.2))
    points.append((0.7, 0.6))
    points.append((0.5, 0.6))
    points.append((0.5, 0.5))
    return points

def main():
    points, scores = creer_dataset_random(300)
    save_to_csv(points, scores, '../dataset/dataset_train_1.csv')

    points, scores = creer_dataset_random(16)
    points += creer_dataset_test_standard()
    save_to_csv(points, fichier='../dataset/dataset_test_1.csv')

if __name__ == '__main__':
    main()
