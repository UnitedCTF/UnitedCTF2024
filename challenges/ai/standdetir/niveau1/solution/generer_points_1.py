import random
import matplotlib.pyplot as plt

from utils import get_random_point, distance_euclide, save_to_csv

random.seed(0)

"""
Premier test : cible "standard", en cercles concentriques.
Le score (en nombres entiers) varie selon la distance par rapport au point (0.5, 0.5).
Certains points du set de test sont choisis a la main, d'autres sont aleatoires.
"""

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
    return score, dist

def creer_dataset_random(taille):
    points = []
    scores = []
    for _ in range(taille):
        point = get_random_point(2)
        points.append(point)
        score, dist = score_point(point)
        scores.append(score)
        
    return points, scores

def creer_dataset_test():
    points = []
    points.append((0.12,0.88))
    points.append((0.04,0.26))
    points.append((0.52,0.58))
    points.append((0.39,0.10))
    points.append((0.25,0.28))
    points.append((0.75,0.90))
    points.append((0.59,0.03))
    points.append((0.79,0.30))
    points.append((0.38,0.56))
    points.append((0.24,0.91))
    points.append((0.16,0.41))
    points.append((0.28,0.51))
    points.append((0.52,0.62))
    points.append((0.53,0.41))
    points.append((0.63,0.40))
    points.append((0.0, 0.0))
    points.append((0.7, 0.2))
    points.append((0.7, 0.6))
    points.append((0.5, 0.4))
    points.append((0.5, 0.5))
    plt.scatter([p[0] for p in points], [p[1] for p in points])
    plt.show()
    return points

def main():
    points, scores = creer_dataset_random(300)
    save_to_csv(points, header=['x', 'y', 'score'], scores=scores, fichier='../dataset/dataset_train_1.csv')

    points = creer_dataset_test()
    save_to_csv(points, header=['x', 'y'], fichier='../dataset/dataset_test_1.csv')

if __name__ == '__main__':
    main()
