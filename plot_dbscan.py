
import numpy as np
import os.path


from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


##############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

X = StandardScaler().fit_transform(X)

if os.path.exists("log.npy"):
    info = np.load("log.npy")
X=info



# Y = []
# for x in range(0,len(X)):
#   # print X[x][1]
#   if X[x][1]>400:
#     Y.append(X[x])
# X = Y
# print X

X = X.tolist();
# print X
mean =  np.mean(X,axis=0)
print mean
Xlength = len(X)
X_corrd = X
print Xlength
X.append([0,mean[1]])
X.append([1,mean[1]])
X.append([3,mean[1]])
X.append([4,mean[1]])
X.append([5,mean[1]])
X.append([1200,mean[1]])
X.append([1201,mean[1]])
X.append([1202,mean[1]])
X.append([1230,mean[1]])
X.append([1220,mean[1]])

print X
X = StandardScaler().fit_transform(X)
X[:,1] = 0.15*X[:,1]
# print 


##############################################################################
# Compute DBSCAN
# db = DBSCAN(eps=30, min_samples=8).fit(X)
db = DBSCAN(eps=0.15, min_samples=5).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_


print X[labels == 5]
print labels ==0
print labels



# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


def  findBounday(lbl):
  "This returns a bounding box for a label lbl"
  upper=0
  low = 10000
  left = 10000
  right =0
  for  i in range(0,Xlength):
    if labels[i]==lbl:
      x = X_corrd[i][0]
      y = X_corrd[i][1]
      if x<left:
        left = x
      if x>right:
        right = x
      if y < low:
        low = y
      if y > upper:
        upper = y

  return [left, low, right - left, upper - low]

print findBounday(3)
print findBounday(2)
print findBounday(1)
print findBounday(0)
  # labels_index = []
  # for n_c in range(0,n_clusters_):
  #   index_each_label = []
  #   for x in range(0,Xlength):
  #     if labels[x]==n_c:
  #       index_each_label.append(x)



print('Estimated number of clusters: %d' % n_clusters_)
# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.3f"
#       % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f"
#       % metrics.adjusted_mutual_info_score(labels_true, labels))
# print("Silhouette Coefficient: %0.3f"
#       % metrics.silhouette_score(X, labels))

##############################################################################
# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)
    # print class_member_mask
    # print core_samples_mask

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

