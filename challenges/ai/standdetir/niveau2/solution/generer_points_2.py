import random
import matplotlib.pyplot as plt

from utils import get_random_point, distance_euclide, save_to_csv

random.seed(0)

"""
Deuxieme test : espaces 3D. On determine les zones par une liste de points, puis la classe de chaque coordonee est determinee par le point le plus proche.
Le score (en nombres entiers) varie selon le point le plus pres.
Toutes les donnees sont determinees aleatoirement.
"""

def fonction_score(nb_zones, dim):
    centres_zones = []
    for _ in range(nb_zones):
        point = get_random_point(dim)
        centres_zones.append(point)
    scores = [i+1 for i in range(nb_zones)]
    return centres_zones, scores

def score_point(point, centres_zones, scores_zones):
    #distance du centre
    min_dist = 1000
    min_zone = None
    for i, centre_zone in enumerate(centres_zones):
        dist = distance_euclide((dim for dim in centre_zone), point)
        if dist < min_dist:
            min_dist = dist
            min_zone = i
    score = scores_zones[min_zone]

    return score

def creer_dataset_random(taille, centres_zones, scores_zones, dim):
    points = []
    scores = []
    for _ in range(taille):
        point = get_random_point(dim)
        points.append(point)
        score = score_point(point, centres_zones, scores_zones)
        scores.append(score)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    p1 = [p[0] for p in points]
    p2 = [p[1] for p in points]
    p3 = [p[2] for p in points]
    ax.scatter(p1, p2, p3, c=scores)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    return points, scores

def creer_dataset_test():
    points = []
    points.append((0.05054094001118514,0.6288734113160805,0.563120693977036))
    points.append((0.5631497372559444,0.08095065729667783,0.35674747019982944))
    points.append((0.13057866604435242,0.46791656250384794,0.370620929023317))
    points.append((0.32983446943201444,0.8817984841814537,0.6242448812511249))
    points.append((0.11005618651538773,0.6573683269943955,0.9962462900587857))
    points.append((0.36529196933279284,0.7705231532984238,0.6571483742776576))
    points.append((0.4750520691644966,0.4046014967029461,0.213949092412954))
    points.append((0.4177612204461568,0.266812815842432,0.48630594038918096))
    points.append((0.6693754903435739,0.8868669672069712,0.14542527816603945))
    points.append((0.8097781852311406,0.761961090744142,0.6280694735868528))
    points.append((0.19207459142533134,0.07170711315686995,0.13685161221759867))
    points.append((0.7837985890347726,0.30331272607892745,0.4765969541523558))
    points.append((0.343591319367598,0.16226944670950127,0.9757208982672713))
    points.append((0.7048934127379858,0.8033085258237557,0.49722071852049776))
    points.append((0.09689896208558291,0.5862592876295961,0.44474305755772836))
    points.append((0.31804972271765364,0.08748170480830497,0.3161120203373988))
    points.append((0.2723104054859511,0.3562621896150353,0.7133340686479843))
    points.append((0.6108869734438016,0.9130110532378982,0.9666063677707588))
    points.append((0.3096883619821068,0.8559724000250744,0.8640600741021592))
    points.append((0.8444218515250481,0.7579544029403025,0.420571580830845))
    return points


def main():
    dim = 3
    centres_zones, scores = fonction_score(10, dim)
    save_to_csv(centres_zones, header=['x', 'y', 'z', 'score'], scores=scores, fichier='../dataset/centres_zones_2.csv')
    points, scores = creer_dataset_random(1000, centres_zones, scores, dim)
    save_to_csv(points, header=['x', 'y', 'z', 'score'], scores=scores, fichier='../dataset/dataset_train_2.csv')

    points = creer_dataset_test()
    save_to_csv(points, header=['x', 'y', 'z'], fichier='../dataset/dataset_test_2.csv')

if __name__ == '__main__':
    main()
