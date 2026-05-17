import json

with open('existing_words.json', 'r') as f:
    existing_words = set(word.lower() for word in json.load(f))

g4_verbs = [
    ("arrive", "到着する", "動詞"), ("ask", "尋ねる", "動詞"), ("become", "〜になる", "動詞"), 
    ("begin", "始まる", "動詞"), ("borrow", "借りる", "動詞"), ("bring", "持ってくる", "動詞"), 
    ("buy", "買う", "動詞"), ("call", "呼ぶ", "動詞"), ("carry", "運ぶ", "動詞"), 
    ("catch", "捕まえる", "動詞"), ("change", "変える", "動詞"), ("check", "調べる", "動詞"), 
    ("clean", "掃除する", "動詞"), ("climb", "登る", "動詞"), ("collect", "集める", "動詞"), 
    ("cook", "料理する", "動詞"), ("dance", "踊る", "動詞"), ("decide", "決める", "動詞"), 
    ("draw", "描く", "動詞"), ("drink", "飲む", "動詞"), ("drive", "運転する", "動詞"), 
    ("drop", "落とす", "動詞"), ("eat", "食べる", "動詞"), ("enjoy", "楽しむ", "動詞"), 
    ("explain", "説明する", "動詞"), ("fall", "落ちる", "動詞"), ("feel", "感じる", "動詞"), 
    ("find", "見つける", "動詞"), ("finish", "終える", "動詞"), ("forget", "忘れる", "動詞"), 
    ("get", "手に入れる", "動詞"), ("give", "与える", "動詞"), ("happen", "起こる", "動詞"), 
    ("hear", "聞こえる", "動詞"), ("help", "手伝う", "動詞"), ("hope", "望む", "動詞"), 
    ("hurry", "急ぐ", "動詞"), ("join", "加わる", "動詞"), ("keep", "保つ", "動詞"), 
    ("know", "知っている", "動詞"), ("learn", "学ぶ", "動詞"), ("leave", "去る", "動詞"), 
    ("lend", "貸す", "動詞"), ("look", "見る", "動詞"), ("lose", "失う", "動詞"), 
    ("make", "作る", "動詞"), ("mean", "意味する", "動詞"), ("meet", "会う", "動詞"), 
    ("move", "動く", "動詞"), ("need", "必要とする", "動詞")
]

g4_nouns = [
    ("a.m.", "午前", "名詞"), ("p.m.", "午後", "名詞"), ("airport", "空港", "名詞"), 
    ("animal", "動物", "名詞"), ("apartment", "アパート", "名詞"), ("artist", "芸術家", "名詞"), 
    ("aunt", "おば", "名詞"), ("bank", "銀行", "名詞"), ("beach", "浜辺", "名詞"), 
    ("bicycle", "自転車", "名詞"), ("boat", "ボート", "名詞"), ("bridge", "橋", "名詞"), 
    ("building", "建物", "名詞"), ("calendar", "カレンダー", "名詞"), ("camera", "カメラ", "名詞"), 
    ("camp", "キャンプ", "名詞"), ("center", "中心", "名詞"), ("chicken", "鶏肉", "名詞"), 
    ("children", "子供たち", "名詞"), ("chocolate", "チョコレート", "名詞"), ("classmate", "同級生", "名詞"), 
    ("clothes", "服", "名詞"), ("club", "クラブ", "名詞"), ("college", "大学", "名詞"), 
    ("computer", "コンピューター", "名詞"), ("concert", "コンサート", "名詞"), ("corner", "角", "名詞"), 
    ("country", "国", "名詞"), ("cousin", "いとこ", "名詞"), ("curtain", "カーテン", "名詞"), 
    ("daughter", "娘", "名詞"), ("diary", "日記", "名詞"), ("dictionary", "辞書", "名詞"), 
    ("dinner", "夕食", "名詞"), ("dish", "皿", "名詞"), ("doctor", "医者", "名詞"), 
    ("dream", "夢", "名詞"), ("driver", "運転手", "名詞"), ("earth", "地球", "名詞"), 
    ("engineer", "エンジニア", "名詞"), ("evening", "夕方", "名詞"), ("exam", "試験", "名詞"), 
    ("factory", "工場", "名詞"), ("family", "家族", "名詞"), ("farm", "農場", "名詞"), 
    ("favorite", "お気に入り", "名詞"), ("festival", "祭り", "名詞"), ("field", "野原", "名詞"), 
    ("floor", "床", "名詞"), ("forest", "森", "名詞"), ("future", "未来", "名詞"), 
    ("garden", "庭", "名詞"), ("gate", "門", "名詞"), ("grade", "学年", "名詞"), 
    ("grandfather", "祖父", "名詞"), ("grandmother", "祖母", "名詞"), ("health", "健康", "名詞"), 
    ("history", "歴史", "名詞"), ("hobby", "趣味", "名詞"), ("holiday", "休日", "名詞"), 
    ("homework", "宿題", "名詞"), ("hospital", "病院", "名詞"), ("hotel", "ホテル", "名詞"), 
    ("island", "島", "名詞"), ("job", "仕事", "名詞"), ("kitchen", "台所", "名詞"), 
    ("lake", "湖", "名詞"), ("language", "言語", "名詞"), ("lesson", "授業", "名詞"), 
    ("library", "図書館", "名詞"), ("magazine", "雑誌", "名詞"), ("market", "市場", "名詞"), 
    ("member", "会員", "名詞"), ("message", "伝言", "名詞"), ("mountain", "山", "名詞"), 
    ("museum", "博物館", "名詞"), ("neighbor", "隣人", "名詞"), ("newspaper", "新聞", "名詞"), 
    ("ocean", "海洋", "名詞"), ("office", "事務所", "名詞")
]

g4_adjectives = [
    ("afraid", "恐れて", "形容詞"), ("angry", "怒った", "形容詞"), ("beautiful", "美しい", "形容詞"), 
    ("boring", "退屈な", "形容詞"), ("busy", "忙しい", "形容詞"), ("careful", "注意深い", "形容詞"), 
    ("cheap", "安い", "形容詞"), ("cloudy", "曇った", "形容詞"), ("cold", "寒い", "形容詞"), 
    ("cool", "涼しい", "形容詞"), ("cute", "かわいい", "形容詞"), ("dark", "暗い", "形容詞"), 
    ("delicious", "おいしい", "形容詞"), ("different", "違った", "形容詞"), ("difficult", "難しい", "形容詞"), 
    ("dirty", "汚い", "形容詞"), ("early", "早い", "形容詞"), ("easy", "簡単な", "形容詞"), 
    ("excited", "わくわくした", "形容詞"), ("exciting", "わくわくさせる", "形容詞"), 
    ("expensive", "高価な", "形容詞"), ("famous", "有名な", "形容詞"), ("fast", "速い", "形容詞"), 
    ("fine", "元気な", "形容詞"), ("foreign", "外国の", "形容詞"), ("free", "自由な", "形容詞"), 
    ("friendly", "親しみやすい", "形容詞"), ("glad", "うれしい", "形容詞"), ("great", "すばらしい", "形容詞"), 
    ("happy", "幸せな", "形容詞"), ("hard", "一生懸命な", "形容詞"), ("healthy", "健康な", "形容詞"), 
    ("heavy", "重い", "形容詞"), ("important", "重要な", "形容詞"), ("interesting", "おもしろい", "形容詞"), 
    ("kind", "親切な", "形容詞"), ("large", "大きい", "形容詞"), ("late", "遅い", "形容詞"), 
    ("light", "軽い", "形容詞"), ("lucky", "幸運な", "形容詞")
]

g4_adverbs = [
    ("again", "再び", "副詞"), ("ago", "〜前に", "副詞"), ("almost", "ほとんど", "副詞"), 
    ("already", "すでに", "副詞"), ("also", "〜もまた", "副詞"), ("always", "いつも", "副詞"), 
    ("away", "離れて", "副詞"), ("back", "戻って", "副詞"), ("before", "以前に", "副詞"), 
    ("carefully", "注意深く", "副詞"), ("easily", "簡単に", "副詞"), ("enough", "十分に", "副詞"), 
    ("ever", "今までに", "副詞"), ("finally", "ついに", "副詞"), ("just", "ちょうど", "副詞"), 
    ("maybe", "たぶん", "副詞"), ("never", "一度も〜ない", "副詞"), ("often", "しばしば", "副詞"), 
    ("once", "一度", "副詞"), ("outside", "外で", "副詞"), ("over", "向こうへ", "副詞"), 
    ("perhaps", "ひょっとすると", "副詞"), ("quickly", "速く", "副詞"), ("really", "本当に", "副詞"), 
    ("slowly", "ゆっくりと", "副詞"), ("someday", "いつか", "副詞"), ("sometimes", "ときどき", "副詞"), 
    ("soon", "すぐに", "副詞"), ("still", "まだ", "副詞"), ("together", "一緒に", "副詞")
]

g3_verbs = [
    ("agree", "同意する", "動詞"), ("appear", "現れる", "動詞"), ("believe", "信じる", "動詞"), 
    ("build", "建てる", "動詞"), ("choose", "選ぶ", "動詞"), ("continue", "続ける", "動詞"), 
    ("deliver", "配達する", "動詞"), ("describe", "説明する", "動詞"), ("discover", "発見する", "動詞"), 
    ("follow", "従う", "動詞"), ("grow", "育つ", "動詞"), ("hold", "開催する", "動詞"), 
    ("imagine", "想像する", "動詞"), ("improve", "向上させる", "動詞"), ("introduce", "紹介する", "動詞"), 
    ("invite", "招待する", "動詞"), ("laugh", "笑う", "動詞"), ("notice", "気づく", "動詞"), 
    ("offer", "提供する", "動詞"), ("order", "注文する", "動詞"), ("practice", "練習する", "動詞"), 
    ("prepare", "準備する", "動詞"), ("produce", "生産する", "動詞"), ("promise", "約束する", "動詞"), 
    ("protect", "守る", "動詞")
]
# I need more Grade 3 words. Let's add some common ones.
g3_verbs += [
    ("act", "行動する", "動詞"), ("advice", "忠告する", "動詞"), ("allow", "許す", "動詞"),
    ("answer", "答える", "動詞"), ("attack", "攻撃する", "動詞"), ("attend", "出席する", "動詞"),
    ("beat", "打つ", "動詞"), ("belong", "属する", "動詞"), ("blow", "吹く", "動詞"),
    ("borrow", "借りる", "動詞"), ("break", "壊す", "動詞"), ("burn", "燃える", "動詞"),
    ("care", "気にする", "動詞"), ("cause", "引き起こす", "動詞"), ("celebrate", "祝う", "動詞"),
    ("climb", "登る", "動詞"), ("compare", "比較する", "動詞"), ("complain", "不平を言う", "動詞"),
    ("complete", "完了する", "動詞"), ("cost", "費用がかかる", "動詞"), ("count", "数える", "動詞"),
    ("cover", "覆う", "動詞"), ("create", "創造する", "動詞"), ("cross", "横切る", "動詞"),
    ("cry", "泣く", "動詞")
]

g3_nouns = [
    ("accident", "事故", "名詞"), ("activity", "活動", "名詞"), ("address", "住所", "名詞"), 
    ("adult", "大人", "名詞"), ("adventure", "冒険", "名詞"), ("advice", "助言", "名詞"), 
    ("area", "地域", "名詞"), ("art", "芸術", "名詞"), ("attention", "注意", "名詞"), 
    ("autumn", "秋", "名詞"), ("birthday", "誕生日", "名詞"), ("bottle", "瓶", "名詞"), 
    ("business", "ビジネス", "名詞"), ("card", "カード", "名詞"), ("care", "世話", "名詞"), 
    ("case", "場合", "名詞"), ("chance", "機会", "名詞"), ("church", "教会", "名詞"), 
    ("city", "都市", "名詞"), ("course", "コース", "名詞"), ("danger", "危険", "名詞"), 
    ("energy", "エネルギー", "名詞"), ("farmer", "農家", "名詞"), ("film", "映画", "名詞"), 
    ("fruit", "果物", "名詞"), ("gift", "贈り物", "名詞"), ("modern", "現代", "名詞")
]
# Add more G3 nouns
g3_nouns += [
    ("air", "空気", "名詞"), ("amount", "量", "名詞"), ("article", "記事", "名詞"),
    ("attention", "注意", "名詞"), ("audience", "観客", "名詞"), ("author", "著者", "名詞"),
    ("base", "底", "名詞"), ("beauty", "美しさ", "名詞"), ("benefit", "利益", "名詞"),
    ("blood", "血", "名詞"), ("board", "板", "名詞"), ("body", "体", "名詞"),
    ("brain", "脳", "名詞"), ("breath", "呼吸", "名詞"), ("bridge", "橋", "名詞"),
    ("capital", "首都", "名詞"), ("captain", "船長", "名詞"), ("cash", "現金", "名詞"),
    ("cause", "原因", "名詞"), ("century", "世紀", "名詞"), ("character", "性格", "名詞"),
    ("choice", "選択", "名詞"), ("clerk", "店員", "名詞"), ("climate", "気候", "名詞"),
    ("cloud", "雲", "名詞"), ("coach", "コーチ", "名詞"), ("coast", "海岸", "名詞"),
    ("collection", "収集", "名詞"), ("comfort", "快適さ", "名詞"), ("common", "共通", "名詞"),
    ("community", "共同体", "名詞"), ("company", "会社", "名詞"), ("condition", "状態", "名詞"),
    ("control", "支配", "名詞"), ("conversation", "会話", "名詞"), ("cost", "費用", "名詞"),
    ("couple", "カップル", "名詞"), ("court", "法廷", "名詞"), ("culture", "文化", "名詞"),
    ("customer", "顧客", "名詞"), ("cycle", "周期", "名詞"), ("damage", "損害", "名詞"),
    ("death", "死", "名詞")
]

g3_adjectives = [
    ("able", "できる", "形容詞"), ("alone", "一人の", "形容詞"), ("another", "別の", "形容詞"), 
    ("brave", "勇敢な", "形容詞"), ("bright", "明るい", "形容詞"), ("clean", "清潔な", "形容詞"), 
    ("clear", "明らかな", "形容詞"), ("clever", "賢い", "形容詞"), ("close", "近い", "形容詞"), 
    ("comfortable", "快適な", "形容詞"), ("common", "共通の", "形容詞"), ("correct", "正しい", "形容詞"), 
    ("deep", "深い", "形容詞"), ("empty", "空の", "形容詞"), ("fresh", "新鮮な", "形容詞"), 
    ("modern", "現代的な", "形容詞"), ("natural", "自然な", "形容詞"), ("necessary", "必要な", "形容詞"), 
    ("nervous", "緊張した", "形容詞"), ("popular", "人気のある", "形容詞")
]
# Add more G3 adjectives
g3_adjectives += [
    ("active", "活動的な", "形容詞"), ("alive", "生きている", "形容詞"), ("ancient", "古代の", "形容詞"),
    ("anxious", "心配な", "形容詞"), ("asleep", "眠っている", "形容詞"), ("awful", "ひどい", "形容詞"),
    ("blind", "盲目の", "形容詞"), ("calm", "穏やかな", "形容詞"), ("central", "中心の", "形容詞"),
    ("certain", "確信して", "形容詞"), ("cheerful", "陽気な", "形容詞"), ("clever", "賢い", "形容詞"),
    ("comfortable", "快適な", "形容詞"), ("common", "共通の", "形容詞"), ("complete", "完全な", "形容詞"),
    ("constant", "一定の", "形容詞"), ("correct", "正しい", "形容詞"), ("crowded", "混雑した", "形容詞"),
    ("cruel", "残酷な", "形容詞"), ("curious", "好奇心の強い", "形容詞"), ("daily", "毎日の", "形容詞"),
    ("dead", "死んだ", "形容詞"), ("deaf", "耳が聞こえない", "形容詞"), ("dear", "親愛な", "形容詞"),
    ("delighted", "喜んでいる", "形容詞"), ("direct", "直接の", "形容詞"), ("distant", "遠い", "形容詞"),
    ("double", "二重の", "形容詞"), ("dry", "乾いた", "形容詞"), ("due", "到着予定の", "形容詞")
]

g3_adverbs = [
    ("actually", "実は", "副詞"), ("alone", "一人で", "副詞"), ("clearly", "はっきりと", "副詞"), 
    ("even", "〜でさえ", "副詞"), ("everywhere", "どこでも", "副詞"), ("forward", "前方へ", "副詞"), 
    ("instead", "代わりに", "副詞"), ("nearly", "ほとんど", "副詞"), ("quite", "かなり", "副詞"), 
    ("rather", "むしろ", "副詞"), ("recently", "最近", "副詞")
]
# Add more G3 adverbs
g3_adverbs += [
    ("abroad", "外国へ", "副詞"), ("ahead", "前方に", "副詞"), ("anywhere", "どこかに", "副詞"),
    ("apart", "離れて", "副詞"), ("besides", "その上", "副詞"), ("certainly", "確かに", "副詞"),
    ("completely", "完全に", "副詞"), ("directly", "直接に", "副詞"), ("elsewhere", "他のどこかに", "副詞"),
    ("entirely", "完全に", "副詞"), ("especially", "特に", "副詞"), ("extremely", "極端に", "副詞"),
    ("fairly", "かなり", "副詞"), ("further", "さらに", "副詞"), ("hardly", "ほとんど〜ない", "副詞"),
    ("highly", "非常に", "副詞"), ("immediately", "直ちに", "副詞"), ("largely", "主に", "副詞"),
    ("mostly", "大部分は", "副詞"), ("naturally", "自然に", "副詞")
]

def filter_words(word_list):
    res = []
    seen = set()
    for eng, jap, cat in word_list:
        if eng.lower() not in existing_words and eng.lower() not in seen:
            res.append((eng, jap, cat))
            seen.add(eng.lower())
    return res

final_g4 = filter_words(g4_verbs + g4_nouns + g4_adjectives + g4_adverbs)
final_g3 = filter_words(g3_verbs + g3_nouns + g3_adjectives + g3_adverbs)

print(f"G4 unique: {len(final_g4)}")
print(f"G3 unique: {len(final_g3)}")

output = {
    "4級": final_g4[:100],
    "3級": final_g3[:100]
}

print(json.dumps(output, ensure_ascii=False, indent=2))
