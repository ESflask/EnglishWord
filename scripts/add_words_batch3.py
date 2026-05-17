"""
2級の残り21語を追加して合計100語増加を達成する。
"""
import json
import uuid

WATCH_JSON = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json"
IOS_JSON   = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWordIOS/Resources/words.json"

with open(WATCH_JSON, encoding="utf-8") as f:
    words = json.load(f)

existing = set(w["english"].lower() for w in words)

candidates_2q = [
    ("abolition", "廃止", "名詞"),
    ("accession", "加入", "名詞"),
    ("activism", "積極行動主義", "名詞"),
    ("adjacency", "隣接", "名詞"),
    ("adjudication", "裁定", "名詞"),
    ("aggressiveness", "攻撃性", "名詞"),
    ("apprenticeship", "見習い制度", "名詞"),
    ("backlog", "未処理案件", "名詞"),
    ("byproduct", "副産物", "名詞"),
    ("centralization", "中央集権化", "名詞"),
    ("classification", "分類", "名詞"),
    ("colonization", "植民地化", "名詞"),
    ("commercialization", "商業化", "名詞"),
    ("commonality", "共通性", "名詞"),
    ("conditionality", "条件性", "名詞"),
    ("consumerism", "消費主義", "名詞"),
    ("contradiction", "矛盾", "名詞"),
    ("deconstruction", "脱構築", "名詞"),
    ("deflation", "デフレ", "名詞"),
    ("deliberation", "熟慮", "名詞"),
    ("democratization", "民主化", "名詞"),
    ("depletion", "枯渇", "名詞"),
    ("deprivation", "剥奪", "名詞"),
    ("differentiation", "差別化", "名詞"),
    ("digitalization", "デジタル化", "名詞"),
    ("diversification", "多様化", "名詞"),
    ("emancipation", "解放", "名詞"),
    ("equalization", "均等化", "名詞"),
    ("escalation", "エスカレーション", "名詞"),
    ("facilitation", "促進", "名詞"),
    ("fragmentation", "断片化", "名詞"),
    ("generalization", "一般化", "名詞"),
    ("globalization", "グローバル化", "名詞"),
    ("harmonization", "調和", "名詞"),
    ("homogenization", "均質化", "名詞"),
    ("impoverishment", "貧困化", "名詞"),
    ("inadequacy", "不十分さ", "名詞"),
    ("industrialization", "工業化", "名詞"),
    ("irregularity", "不規則性", "名詞"),
    ("legitimization", "正当化", "名詞"),
    ("liberalization", "自由化", "名詞"),
    ("mobilization", "動員", "名詞"),
    ("monetization", "収益化", "名詞"),
    ("nationalization", "国有化", "名詞"),
    ("normalization", "正常化", "名詞"),
    ("obsolete", "時代遅れの", "形容詞"),
    ("oppression", "抑圧", "名詞"),
    ("polarization", "二極化", "名詞"),
    ("privatization", "民営化", "名詞"),
    ("professionalism", "プロ意識", "名詞"),
    ("radicalization", "過激化", "名詞"),
    ("rationalization", "合理化", "名詞"),
    ("redundancy", "冗長性", "名詞"),
    ("remuneration", "報酬", "名詞"),
    ("secularization", "世俗化", "名詞"),
    ("segregation", "差別", "名詞"),
    ("simplification", "単純化", "名詞"),
    ("stabilization", "安定化", "名詞"),
    ("stratification", "層化", "名詞"),
    ("technocracy", "テクノクラシー", "名詞"),
    ("urbanization", "都市化", "名詞"),
    ("volatility", "不安定性", "名詞"),
]

new_entries = []
count = 0
for english, japanese, category in candidates_2q:
    if english.lower() not in existing:
        existing.add(english.lower())
        new_entries.append({
            "id": str(uuid.uuid4()),
            "english": english,
            "japanese": japanese,
            "category": category,
            "level": "2級",
        })
        count += 1
    if count >= 21:
        break

print(f"2級: {count}語追加")
words.extend(new_entries)
print(f"合計: {len(words)}語")

from collections import Counter
c = Counter(w["level"] for w in words)
for k in ["準2級", "2級", "準1級", "1級"]:
    print(f"  {k}: {c[k]}語")

output = json.dumps(words, ensure_ascii=False, indent=2)
with open(WATCH_JSON, "w", encoding="utf-8") as f:
    f.write(output)
with open(IOS_JSON, "w", encoding="utf-8") as f:
    f.write(output)

print("完了")
