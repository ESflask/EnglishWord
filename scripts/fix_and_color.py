import json

with open("/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json", encoding="utf-8") as f:
    words = json.load(f)

# retirement の category を修正
fixed = 0
for w in words:
    if w["category"] == "退職":
        w["category"] = "名詞"
        fixed += 1

print(f"修正: {fixed}件")

watch_out = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json"
ios_out   = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWordIOS/Resources/words.json"
for path in [watch_out, ios_out]:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
print("完了")
