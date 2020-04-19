# -*- coding: utf-8 -*-

from python.decisiontreeclassifier import DecisionTreeClassifier

if __name__ == "__main__":
    lense_labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    X = []
    Y = []
    with open('lenses.txt', 'r') as f:
        for line in f:
            comps = line.strip().split('\t')
            X.append(comps[: -1])
            Y.append(comps[-1])
    print("decision tree")
    clf = DecisionTreeClassifier()
    clf.create_tree(X, Y, lense_labels)
    print(clf.tree);

    # 使用构建好的决策树进行分类
    # 递归查找树
    clf.classify()
