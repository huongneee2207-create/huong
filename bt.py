import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# Tạo dữ liệu giả lập (4 features)
np.random.seed(42)
data = np.random.rand(100, 4) * 1000
df = pd.DataFrame(data, columns=['Doanh_thu', 'Loi_nhuan', 'Chi_phi_Marketing', 'Khach_hang'])

# a) Tiền xử lý: Chuẩn hóa dữ liệu (Standardization)
# Bước này cực kỳ quan trọng vì các thuật toán tính khoảng cách (Euclidean)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
# Tìm K tối ưu bằng Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Số lượng cụm (K)')
plt.ylabel('WCSS')
plt.show()

# Giả sử K tối ưu chọn được là 3
kmeans_final = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans_final.fit_predict(df_scaled)
# Vẽ Dendrogram
plt.figure(figsize=(10, 7))
dendro = dendrogram(linkage(df_scaled, method='ward'))
plt.title("Dendrogram")
plt.show()

# Chạy mô hình với số cụm tương ứng (ví dụ 3)
hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
hc_labels = hc.fit_predict(df_scaled)
# Thử nghiệm với eps và min_samples
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(df_scaled)

# Lưu ý: Nếu tất cả nhãn là -1, có nghĩa là eps quá nhỏ (tất cả là nhiễu)
#include <iostream>
using namespace std;

long long giaiThua(int n) {
    long long gt = 1;
    for(int i = 1; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << "! = " << giaiThua(n);

    return 0;
}

#include <iostream>
using namespace std;

long long giaiThua(int n) {
    long long gt = 1;
    for(int i = 1; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << "! = " << giaiThua(n);

    return 0;
}#include <iostream>
using namespace std;

long long giaiThua(int n) {
    long long gt = 1;
    for(int i = 1; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << "! = " << giaiThua(n);

    return 0;
}#include <iostream>
using namespace std;

long long giaiThua(int n) {
    long long gt = 1;
    for(int i = 1; i <= n; i++) {
        gt *= i;
    }
    return gt;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << "! = " << giaiThua(n);

    return 0;
}
# 3. Tính lợi nhuận sau 12 tháng

so_tien_ban_dau = float(input("Nhập số tiền ban đầu: "))
lai_suat = float(input("Nhập lãi suất mỗi tháng (%): "))

so_tien = so_tien_ban_dau

for i in range(12):
    so_tien += so_tien * (lai_suat / 100)

loi_nhuan = so_tien - so_tien_ban_dau

print("Số tiền sau 12 tháng là:", so_tien)
print("Lợi nhuận là:", loi_nhuan)