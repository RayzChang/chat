# 定義函式：讀取檔案，回傳每一行的清單
def read_file(filename):
    lines = []  # 建立一個空清單來存放每一行的資料
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  # 去除每行文字的換行符號並加入清單中
    return lines  # 回傳清單

# 定義函式：轉換對話格式，讓每行都有說話者名稱
def convert(lines):
    new = []  # 建立新的清單來儲存處理過的對話
    person = None  # 設定初始說話者為 None（空）
    for line in lines:
        if line == 'Allen':  # 如果這行是 Allen，記錄 Allen 為說話者
            person = 'Allen'
            continue  # 跳過這一行（不儲存名字）
        elif line == 'Tom':  # 如果這行是 Tom，記錄 Tom 為說話者
            person = 'Tom'
            continue  # 跳過這一行
        if person:
            new.append(person + ': ' + line)  # 把說話者加到對話前面並加入新清單
    return new  # 回傳處理過的清單

# 定義函式：把轉換好的對話寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')  # 每一筆對話寫入一行

# 主程式：呼叫三個函式完成整體流程
def main():
    lines = read_file('input.txt')        # 讀取原始檔案
    lines = convert(lines)                # 轉換對話格式
    write_file('output.txt', lines)       # 輸出到新檔案

# 如果是直接執行這個檔案，就呼叫 main()
main()