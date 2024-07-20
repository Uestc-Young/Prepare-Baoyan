1. CNN和transformer的区别  
- 原理上：CNN主要依赖于卷积运算，通过卷积核（或滤波器）在输入图像上滑动来捕捉局部特征。通过多层卷积和池化操作，逐步提取图像的高级特征；Transformer主要基于自注意力机制（self-attention），能够捕捉序列中不同位置元素之间的关系。通过堆叠多层自注意力和前馈神经网络来处理输入数据。
- 结构上：CNN主要由卷积层和池化层组成，卷积层用来提取特征，池化层用来降维，全连接层用来分类或回归；transformer主要由多头自注意力机制和前馈神经网络组成，包括编码器和解码器两部分，每部分都包含多层自注意力和前馈神经网络。编码器用于将输入序列编码成特征表示，解码器用于从特征表示生成输出序列。
- 应用上：CNN主要用于图像处理，transformer主要用于自然语言处理
2. 为什么dropout可以防止过拟合  
- 减少依赖性：Dropout通过随机丢弃网络中的神经元（即将它们的输出设置为零），减少了神经元之间复杂的共适应关系。这防止了网络对训练数据中的特定特征过度依赖。
3. softmax和sigmoid的区别
- 数学公式：$softmax(x) = \frac{e^{x_i}}{\sum_{j}e^{x_j}}$，$sigmoid(x) = \frac{1}{1+e^{-x}}$
- 应用场景：softmax主要用于多分类问题，将模型输出转换为概率分布；sigmoid主要用于二分类问题，将模型输出转换为0到1之间的概率值。
4. cross entropy loss的公式
- 二分类问题：$L(y, \hat{y}) = -y\log(\hat{y}) - (1-y)\log(1-\hat{y})$
5. 介绍normalization的一些方法
- max-min scaling： $x' = x - min(x) / max(x)-min(x)$
- 标准化： $x' = x - \mu / \sigma$
6. LayerNorm 和 BatchNorm 有什么区别

7. 介绍attention机制
8. 介绍一些常见的激活函数  
- Sigmoid
- ReLU
- LeakyReLU
- tanh