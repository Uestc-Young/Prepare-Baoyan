# 行列式
- 上三角/下三角行列式 : $\begin{vmatrix}
  a_{11} & 0 & 0 \\
  a_{21}& a_{22} & 0\\
  a_{32}& a_{32} &a_{33}
\end{vmatrix} = a_{11}a_{22}a_{33}$
- 行列式倍加：倍加行列式的某一行（列）的k倍到另一行（列），行列式的值不变
- 行列式某一行（列）所有元素的公因子可以提到行列式外
- 交换行列式的两行（列），行列式变号
- 每行元素之和相等: $\begin{vmatrix}
  x & a & a \\
  a& x & a\\
  a& a &x
\end{vmatrix}$ 把第2,3列均加到第一列，再提公因子即可
- 范德蒙行列式: $\begin{vmatrix}
  1 & 1 & 1 \\
  a& b & c\\
  a^2& b^2 &c^2
  \end{vmatrix} = (b-a)(c-a)(c-b)$
- 爪型（箭型）行列式: $\begin{vmatrix}
  a_1 & 1 & 1 \\
  1& a_2 & 0\\
  1& 0 &a_3
  \end{vmatrix} = a_2 a_3\begin{vmatrix}
  a_1 & 1 & 1 \\
  1/a_2& 1 & 0\\
  1/a_3& 0 &1
  \end{vmatrix} = a_2a_3(a_1 - 1/a_2 - 1/a_3)$ 先提公因子，再化成三角形行列式
- 余子式与代数余子式: 有矩阵 $A = \begin{bmatrix}
  a_{11} & a_{12} & a_{13} \\
  a_{21}& a_{22} & a_{23}\\
  a_{31}& a_{32} &a_{33}
\end{bmatrix}$，则 $M_{ij} = (-1)^{i+j} \begin{vmatrix}
  a_{11} & a_{12}  \\
  a_{31}& a_{32}
\end{vmatrix}$ 是 $a_{ij} (i=2, j=2)$ 的余子式，$A_{ij}$ 是 $a_{ij}$ 的代数余子式，$A_{ij} = (-1)^{i+j}M_{ij}$
- 行列式展开定理: 按某一行（列）展开，得到 $\sum_{j=1}^n a_{ij}A_{ij}$ 或 $\sum_{i=1}^n a_{ij}A_{ij}$，其中 $A_{ij}$ 是 $a_{ij}$ 的代数余子式
- 若行列式的某一行（列）的元素都是两个数的和，如 $\begin{vmatrix}
  a+b & c+d & e+f \\
  g& i & k\\
  m& o &q
\end{vmatrix}$，则可以分开展开，再相加得到$\begin{vmatrix}
  a & c & e \\
  g& i & k\\
  m& o &q
\end{vmatrix} + \begin{vmatrix}
    b & d & f \\
    g& i & k\\
    m& o &q
\end{vmatrix}$
- 拉普拉斯公式: $\begin{vmatrix}
  a_{1} & a_{2} & 0 & 0 \\
  a_{3}& a_{4} & 0 & 0 \\
  b_{1} & b_{2} & c_{1} & c_{2} \\
    b_{3}& b_{4} & c_{3} & c_{4}
\end{vmatrix} = \begin{vmatrix}
    a_{1} & a_{2}  \\
    a_{3}& a_{4}
\end{vmatrix} \begin{vmatrix}
    c_{1} & c_{2}  \\
    c_{3}& c_{4}  \end{vmatrix}$

# 矩阵
- 矩阵乘法: 略
- 矩阵求逆: $(A | E) = (E | A^-1)$，即把单位矩阵变成A的逆矩阵
- 矩阵可逆的充要条件: $|A| \neq 0$
- A的伴随矩阵: $A^* = (A_{ij})^T$，即把A的代数余子式矩阵转置，$A^*A = AA^* = |A|E, \quad A^* = |A|A^{-1}$
- 方阵的行列式: $|A^{-1}| = 1 / |A|, \quad |A^T| = |A|, \quad |kA_{n\times n}|=k^n|A|, \quad |A^*_{n \times n}| = |A|^{n-1}$
- 矩阵的秩: 矩阵$A$的秩是把$A$利用初等变化化为行阶梯形矩阵后非零行的行数，记作$r(A)$

# 向量组的线性相关性
- 向量组的线性相关性: 向量组$A = \{a_1, a_2, \cdots, a_n\}$，如果存在不全为0的数$k_1, k_2, \cdots, k_n$，使得$k_1a_1 + k_2a_2 + \cdots + k_na_n = 0$，则称$A$线性相关
- 两个向量$\alpha_1$与$\alpha_2$线性相关的充要条件是$\alpha_1$与$\alpha_2$的分量成比例, 即$\alpha_1 = k\alpha_2$。如果能够构成方阵，还有$|\alpha_1, \alpha_2| = 0$
- 多个向量线性相关的充要条件是它们的行列式为0，即$\alpha_1, \alpha_2, \cdots, \alpha_n$线性相关的充要条件是$|\alpha_1, \alpha_2, \cdots, \alpha_n| = 0$。如果不能构成方阵，$\alpha_1, \alpha_2, \cdots, \alpha_n$线性相关的充要条件是$\alpha_1, \alpha_2, \cdots, \alpha_n$构成的矩阵的秩小于$n$
- 无关组*可逆阵 -> 无关； 无关组\*不可逆阵 -> 相关
- 极大无关组: 向量组$A = \{a_1, a_2, \cdots, a_n\}$，如果$A$中任意一个向量都不能由其余$n-1$个向量线性表示，则称$A$是一个极大无关组
- 给出一个向量组，求出它的一个极大无关组的方法：把向量组的向量按列排成一个矩阵，然后对矩阵进行初等行变换，使其化为行阶梯形矩阵，然后把矩阵中的非零行对应的向量取出来，就是一个极大无关组 
e.g $\begin{bmatrix}
  1 & 2 & 3 & 4 \\
  2 & 3 & 4 & 5 \\
  3 & 4 & 5 & 6
\end{bmatrix} \rightarrow \begin{bmatrix}
  1 & 2 & 3 & 4 \\
  0 & -1 & -2 & -3 \\
  0 &  -2 & -4 & -6 \\
\end{bmatrix} \rightarrow \begin{bmatrix}
  1 & 2 & 3 & 4 \\
  0 & -1 & -2 & -3 \\
  0 &  0 & 0 & 0 \\
  \end{bmatrix}$，则极大无关组为$\begin{bmatrix}
  1 \\
  0 \\
  0 \\
\end{bmatrix}, \begin{bmatrix}
  2 \\
  -1 \\
  0 \\
\end{bmatrix}$

# 线性方程组
- 齐次线性方程组的解: 齐次线性方程组$A_{m \times n}X = 0$，如果$A$的秩等于$n$，则齐次线性方程组有唯一解$x = 0$；如果$A$的秩小于$n$，则齐次线性方程组有无穷多解
- 齐次线性方程组的基础解系: 齐次线性方程组$A_{m \times n}X = 0$，把系数矩阵$A$化为行阶梯形矩阵，然后把非零行对应的未知数取出来，就是基础解系。基础解系的个数等于$n-r(A)$
- 非齐次线性方程组的解: 非齐次线性方程组$A_{m \times n}X = B$，如果$r(A) = r(A, B)$，则非齐次线性方程组有解；如果$r(A) = r(A, B) < n$，则非齐次线性方程组有无穷多解；如果$r(A) = r(A, B) = n$，则非齐次线性方程组有唯一解
- 非齐次线性方程组的解的求法: 把非齐次线性方程组化为齐次线性方程组，然后求出基础解系，再求出特解，特解加上基础解系就是非齐次线性方程组的解
  
# 特征值和特征向量
- 特征值和特征向量: 设$A$是$n$阶矩阵，如果存在数$\lambda$和非零向量$\alpha$，使得$A\alpha = \lambda \alpha$，则称$\lambda$是$A$的特征值，$\alpha$是$A$的对应于特征值$\lambda$的特征向量
- 求特征值和特征向量的方法: $|\lambda E - A| = 0$，求出$\lambda$，然后把对应的$\lambda$代入$(\lambda E - A)\alpha = 0$，求出对应的特征向量$\alpha$(即求出$(\lambda E - A)\alpha = 0$的基础解系)
- 设$A$的特征值为$\lambda_1, \lambda_2, \lambda_3$，对应的特征向量为$\alpha_1, \alpha_2, \alpha_3$，则$A$的行列式为$|A| = \lambda_1\lambda_2\lambda_3$，$A$的迹为$tr(A) = \lambda_1 + \lambda_2 + \lambda_3$
- 矩阵的相似对角化: 设$A$和$B$是两个$n$阶矩阵，如果存在可逆矩阵$P$，使得$P^{-1}AP = B$，其中，$B$是对角矩阵，则称$A$和$B$相似，$B$是$A$的相似对角矩阵。
- 如何求解相似对角化：求出$A$的特征值和特征向量，然后把特征向量按列排成一个矩阵$P$，$P^{-1}AP = \Lambda$，其中$\Lambda$是$A$的特征值构成的对角矩阵
- 若$A^T = A$，则一定存在正交阵$Q$，使得$Q^{-1}AQ = \Lambda$，其中$\Lambda$是$A$的特征值构成的对角矩阵，其中，正交阵是指$Q^TQ = I$，即$Q^T = Q^{-1}$  
具体求解正交化矩阵的步骤，就是在求解相似对角化的基础上，再对特征向量进行正交化处理(施密特正交化)。
