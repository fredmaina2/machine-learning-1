from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#preparing the customer data using a Python list
customer_data = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]
]
#to use Standardscaler  to scale the spending and visits
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)

#to create a K-Means model  using n_clusters=3
kmeans = KMeans(n_clusters=3,random_state=42, n_init=10)

#training the model using customer dataset
kmeans.fit(scaled_data)
cluster = kmeans.labels_

#to display the cluster assigned to each customer
for i , cluster_id in enumerate(cluster):
    print(f"customer {i + 1}belongs to Cluster{cluster_id}")


#to display the total number of customers in each cluster
for cluster_id in range(3):
    count = list(cluster) .count(cluster_id)
    print(f"Total customers in Cluster {cluster_id}: {count}")