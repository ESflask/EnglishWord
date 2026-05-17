import json

level_order = {"4級": 0, "3級": 1, "準2級": 2, "2級": 3, "準1級": 4, "1級": 5}

with open("/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json", encoding="utf-8") as f:
    words = json.load(f)

print(f"処理前: {len(words)}語")

# 英単語（小文字）をキーに、最も低い級のエントリを1つだけ残す
seen = {}
for w in words:
    key = w["english"].lower()
    if key not in seen:
        seen[key] = w
    else:
        existing_rank = level_order.get(seen[key]["level"], 99)
        new_rank = level_order.get(w["level"], 99)
        if new_rank < existing_rank:
            seen[key] = w

result = list(seen.values())
removed = len(words) - len(result)

print(f"削除数: {removed}件")
print(f"処理後: {len(result)}語")
for lv in ["4級", "3級", "準2級", "2級", "準1級", "1級"]:
    c = sum(1 for w in result if w["level"] == lv)
    print(f"  {lv}: {c}語")

watch_out = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json"
ios_out   = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWordIOS/Resources/words.json"
for path in [watch_out, ios_out]:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
print("Watch・iOS両方に書き込み完了")
