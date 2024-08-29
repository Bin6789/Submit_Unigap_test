import json
from collections import Counter

def def_word_cnt(input_string):
# Chia chuỗi vào thành các từ riêng và chuyển chúng thành viết thường
    words = input_string.lower().split()
# Đếm số lượng các từ sử dụng Counter
    word_counts = Counter(words)
# Ghi kết quả vào dictionary
    result_dicts = dict(word_counts)
# Trả về dictionary kết quả
    return result_dicts

# Nhập chuỗi đầu vào
input_str = input("Nhập input: ")
output = def_word_cnt(input_str)

# Viết output vào file json
with open("result.json", "w") as json_file:
    json.dump(output, json_file, indent=2)
    
# Tạo 100 file json chứa kết quả
for i in range(1, 101):
    filename = f"result_{i}.json"
    with open(filename, "w") as json_file:
        json.dump(output, json_file, indent=2)