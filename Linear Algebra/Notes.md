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


