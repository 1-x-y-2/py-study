# py-study

## 随机抽取 Codeforces 题目

先安装依赖：

```bash
python -m pip install requests
```

直接传入最低和最高 rating（区间包含边界）：

```bash
python rating.py 800 1200
```

也可以不传参数，程序会交互式询问分数区间：

```bash
python rating.py
```

程序会从 Codeforces 题库 API 获取题目，随机选择符合区间的题目，并输出题名、分数和题目链接。
