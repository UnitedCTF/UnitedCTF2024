import csv
from sklearn.neighbors import KNeighborsClassifier
from utils import distance_euclide
from generer_points_2 import score_point
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

#lit un fichier CSV
def load_dataset(fichier, dim=3):
    points = []
    scores = []
    with open(fichier, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            x = float(line[0])
            y = float(line[1])
            z = float(line[2])
            points.append((x, y, z))
            if len(line) > dim:
                scores.append(int(line[-1]))
    return points, scores

#knn fait main juste pour le fun
def knn(points_train, scores_train, points_test, k):
    scores_test = []
    for point_test in points_test:
        dists = [distance_euclide(point_test, point) for point in points_train]
        combined_list = [(point, score, dist) for point, score, dist in zip(points_train, scores_train, dists)]
        combined_list.sort(key=lambda a: a[-1])
        knn_scores = [p[1] for p in combined_list[:k]]
        mode = max(set(knn_scores[:k]), key=knn_scores[:k].count)  # calcul de la valeur modale
        scores_test.append(mode)
    return scores_test

#knn de sklearn
def knn_sklearn(points_train, scores_train, points_test, k=3):
    knc = KNeighborsClassifier(n_neighbors=k)
    knc.fit(points_train, scores_train)
    scores_test = [knc.predict([pt])[0] for pt in points_test]
    return scores_test


def svc_sklearn(points_train, scores_train, points_test):
    svc = SVC()
    svc.fit(points_train, scores_train)
    scores_test = [svc.predict([pt])[0] for pt in points_test]
    return scores_test

def mlp_sklearn(points_train, scores_train, points_test):
    mlp = MLPClassifier()
    mlp.fit(points_train, scores_train)
    scores_test = [mlp.predict([pt])[0] for pt in points_test]
    return scores_test

# Verite absolue
def get_gt(points, centre_zones, centre_zones_scores):
    scores = []
    for point in points:
        score = score_point(point, centre_zones, centre_zones_scores)
        scores.append(score)
    return scores

def main():
    centre_zones, centre_zones_scores = load_dataset('../dataset/centres_zones_2.csv')
    points_train, scores_train = load_dataset('../dataset/dataset_train_2.csv')
    points_test, _ = load_dataset('../dataset/dataset_test_2.csv')
    print(len(points_test))
    scores_test = knn(points_train, scores_train, points_test, 3)
    scores_test2 = knn_sklearn(points_train, scores_train, points_test, 3)
    scores_test3 = svc_sklearn(points_train, scores_train, points_test)
    scores_test4 = mlp_sklearn(points_train, scores_train, points_test)
    print(scores_test)
    print(scores_test2)
    print(scores_test3)
    print(scores_test4)
    scores_test_gt = get_gt(points_test, centre_zones, centre_zones_scores)
    print(scores_test_gt)
    print('Checksum:', sum(scores_test), sum(scores_test2), sum(scores_test3), sum(scores_test4), sum(scores_test_gt))

if __name__ == '__main__':
    main()
