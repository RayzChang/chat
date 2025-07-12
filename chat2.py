# 定義函式：讀取檔案，回傳每一行的清單
def read_file(filename):
    lines = []  # 建立一個空清單來存放每一行的資料
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  # 去除每行文字的換行符號並加入清單中
    return lines  # 回傳清單

# 定義函式：轉換對話格式，讓每行都有說話者名稱
def convert(lines):
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count +=1    
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1 
            elif s[2] == '圖片':
                viki_image_count +=1          
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了', allen_word_count, '個字')
    print('Viki說了', viki_word_count, '個字')
    print('Allen傳送了', allen_sticker_count, '張貼圖')
    print('Viki傳送了', viki_sticker_count, '張貼圖')
    print('Allen傳送了', allen_image_count, '張圖片')
    print('Viki傳送了', viki_image_count, '張圖片')


# 定義函式：把轉換好的對話寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')  # 每一筆對話寫入一行

# 主程式：呼叫三個函式完成整體流程
def main():
    lines = read_file('LINE-Viki.txt')        # 讀取原始檔案
    lines = convert(lines)                # 轉換對話格式
    # write_file('output.txt', lines)       # 輸出到新檔案

# 如果是直接執行這個檔案，就呼叫 main()
main()