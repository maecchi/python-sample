# 内包表記

# 0 - 9
# print([i for i in range(10)])
# print([i * 3 for i in range(10)])
print([i * 3 for i in range(10) if i % 2 == 0])  # リスト型
print(i * 3 for i in range(10) if i % 2 == 0)  # ジェネレータ
print({i * 3 for i in range(10) if i % 2 == 0})  # 集合型
