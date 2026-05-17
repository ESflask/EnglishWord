import json

existing_words = json.load(open('existing_words.json'))
grade_4_3 = ['blackboard', 'eraser', 'locker', 'corridor', 'playground', 'recess', 'graduation', 'semester', 'microwave', 'toaster', 'kettle', 'stove', 'dishwasher', 'iron', 'mirror', 'blanket', 'pillow', 'cushion', 'balcony', 'attic', 'basement', 'chimney', 'fence', 'mailbox', 'porch', 'hallway', 'strawberry', 'grape', 'peach', 'watermelon', 'pineapple', 'mango', 'kiwi', 'pear', 'cabbage', 'broccoli', 'spinach', 'lettuce', 'garlic', 'cucumber', 'eggplant', 'pumpkin', 'pea', 'honey', 'steak', 'burger', 'pasta', 'noodle', 'cookie', 'lion', 'elephant', 'giraffe', 'zebra', 'kangaroo', 'koala', 'panda', 'wolf', 'fox', 'squirrel', 'deer', 'goat', 'duck', 'goose', 'turkey', 'owl', 'eagle', 'hawk', 'penguin', 'ostrich', 'flamingo', 'swan', 'whale', 'dolphin', 'shark', 'octopus', 'squid', 'crab', 'shrimp', 'turtle', 'frog', 'snake', 'lizard', 'spider', 'butterfly', 'jungle', 'desert', 'valley', 'canyon', 'coast', 'cave', 'waterfall', 'volcano', 'glacier', 'planet', 'storm', 'thunder', 'lightning', 'rainbow', 'dentist', 'vet', 'attack', 'beat', 'blow', 'complain', 'destroy', 'greet', 'hunt', 'kill', 'lay', 'lock', 'march', 'mark', 'adventure', 'autumn', 'business', 'film', 'beauty', 'blood', 'brain', 'breath', 'coach', 'collection', 'comfort', 'couple', 'court', 'death', 'distance', 'duty', 'edge', 'end', 'expression', 'fear', 'fiction', 'figure', 'file', 'flood', 'flow', 'able', 'alive', 'asleep', 'blind', 'crowded', 'cruel', 'dead', 'deaf', 'dear', 'delighted', 'distant', 'double', 'due', 'eager', 'electric', 'elementary', 'extra', 'false', 'fancy', 'fantastic', 'female', 'flat', 'foolish', 'former', 'front', 'golden', 'grand', 'guilty', 'ahead', 'anywhere', 'apart', 'besides', 'certainly', 'completely', 'directly', 'elsewhere', 'entirely', 'especially', 'extremely', 'fairly', 'further', 'hardly', 'highly', 'immediately', 'largely', 'mostly', 'naturally', 'nearly', 'necessarily', 'obviously', 'originally', 'partly', 'perfectly', 'possibly', 'previously', 'probably', 'properly', 'purely', 'rarely', 'regularly', 'roughly', 'safely']

seen = set(existing_words) | set(grade_4_3)

pre_2_candidates = [
    ("accept", "受け入れる", "動詞"), ("accident", "事故", "名詞"), ("action", "行動", "名詞"),
    ("activity", "活動", "名詞"), ("actor", "俳優", "名詞"), ("actress", "女優", "名詞"),
    ("actually", "実際は", "副詞"), ("additional", "追加の", "形容詞"), ("admire", "賞賛する", "動詞"),
    ("adult", "大人", "名詞"), ("advanced", "進歩した", "形容詞"), ("advantage", "利点", "名詞"),
    ("adventure", "冒険", "名詞"), ("advertise", "広告する", "動詞"), ("advertisement", "広告", "名詞"),
    ("afraid", "恐れて", "形容詞"), ("against", "に対して", "副詞"), ("agree", "同意する", "動詞"),
    ("agreement", "合意", "名詞"), ("airport", "空港", "名詞"), ("allow", "許可する", "動詞"),
    ("almost", "ほとんど", "副詞"), ("already", "すでに", "副詞"), ("although", "けれども", "副詞"),
    ("amazing", "驚くべき", "形容詞"), ("amount", "量", "名詞"), ("ancient", "古代の", "形容詞"),
    ("announce", "発表する", "動詞"), ("anxious", "心配して", "形容詞"), ("apologize", "謝る", "動詞"),
    ("appear", "現れる", "動詞"), ("appearance", "外見", "名詞"), ("apply", "申し込む", "動詞"),
    ("appointment", "約束", "名詞"), ("area", "地域", "名詞"), ("arrival", "到着", "名詞"),
    ("arrive", "到着する", "動詞"), ("article", "記事", "名詞"), ("ashamed", "恥じて", "形容詞"),
    ("aside", "脇に", "副詞"), ("aspect", "側面", "名詞"), ("assist", "助ける", "動詞"),
    ("assistant", "助手", "名詞"), ("associate", "関連づける", "動詞"), ("association", "協会", "名詞"),
    ("assume", "仮定する", "動詞"), ("assumption", "仮定", "名詞"), ("atmosphere", "雰囲気", "名詞"),
    ("attach", "取り付ける", "動詞"), ("attempt", "試みる", "動詞"), ("attend", "出席する", "動詞"),
    ("attention", "注意", "名詞"), ("attitude", "態度", "名詞"), ("attract", "引きつける", "動詞"),
    ("attractive", "魅力的な", "形容詞"), ("audience", "聴衆", "名詞"), ("author", "著者", "名詞"),
    ("authority", "権威", "名詞"), ("available", "利用可能な", "形容詞"), ("average", "平均", "名詞"),
    ("avoid", "避ける", "動詞"), ("award", "賞", "名詞"), ("aware", "気づいて", "形容詞"),
    ("background", "背景", "名詞"), ("baggage", "手荷物", "名詞"), ("balance", "均衡", "名詞"),
    ("basically", "基本的に", "副詞"), ("basis", "基礎", "名詞"), ("battle", "戦い", "名詞"),
    ("behavior", "行動", "名詞"), ("belief", "信念", "名詞"), ("belong", "属する", "動詞"),
    ("benefit", "利益", "名詞"), ("besides", "そのうえ", "副詞"), ("beyond", "の向こうに", "副詞"),
    ("bill", "請求書", "名詞"), ("birth", "誕生", "名詞"), ("bit", "少し", "名詞"),
    ("bite", "噛む", "動詞"), ("blame", "非難する", "動詞"), ("blank", "空白", "名詞"),
    ("board", "板", "名詞"), ("boil", "沸騰させる", "動詞"), ("bomb", "爆弾", "名詞"),
    ("bone", "骨", "名詞"), ("border", "境界", "名詞"), ("borrow", "借りる", "動詞"),
    ("bother", "悩ませる", "動詞"), ("bottom", "底", "名詞"), ("bound", "縛られた", "形容詞"),
    ("bowl", "鉢", "名詞"), ("brain", "脳", "名詞"), ("branch", "枝", "名詞"),
    ("brave", "勇敢な", "形容詞"), ("breathe", "呼吸する", "動詞"), ("bridge", "橋", "名詞"),
    ("brief", "簡潔な", "形容詞"), ("briefly", "簡潔に", "副詞"), ("brilliant", "輝かしい", "形容詞"),
    ("broad", "広い", "形容詞"), ("broadcast", "放送", "名詞"), ("bubble", "泡", "名詞"),
    ("budget", "予算", "名詞"), ("building", "建物", "名詞"), ("bullet", "銃弾", "名詞"),
    ("bunch", "束", "名詞"), ("burst", "破裂する", "動詞"), ("bury", "埋める", "動詞"),
    ("bush", "低木", "名詞"), ("business", "仕事", "名詞"), ("button", "ボタン", "名詞"),
    ("buyer", "買い手", "名詞"), ("cabinet", "戸棚", "名詞"), ("calm", "穏やかな", "形容詞"),
    ("camp", "キャンプ", "名詞"), ("campaign", "運動", "名詞"), ("can", "缶", "名詞"),
    ("cancel", "中止する", "動詞"), ("cancer", "がん", "名詞"), ("candidate", "候補者", "名詞"),
    ("candle", "ろうそく", "名詞"), ("cap", "キャップ", "名詞"), ("capital", "首都", "名詞"),
    ("captain", "船長", "名詞"), ("capture", "捕らえる", "動詞"), ("care", "注意", "名詞"),
    ("career", "経歴", "名詞"), ("careful", "注意深い", "形容詞"), ("careless", "不注意な", "形容詞"),
    ("carpet", "カーペット", "名詞"), ("carriage", "馬車", "名詞"), ("carrot", "人参", "名詞"),
    ("carry", "運ぶ", "動詞"), ("cartoon", "漫画", "名詞"), ("case", "場合", "名詞"),
    ("cash", "現金", "名詞"), ("castle", "城", "名詞"), ("casual", "形式ばらない", "形容詞"),
    ("catch", "捕まえる", "動詞"), ("cattle", "牛", "名詞"), ("cause", "引き起こす", "動詞"),
    ("cave", "洞窟", "名詞"), ("celebrate", "祝う", "動詞"), ("cell", "細胞", "名詞"),
    ("central", "中央の", "形容詞"), ("century", "世紀", "名詞"), ("ceremony", "儀式", "名詞"),
    ("certain", "確信して", "形容詞"), ("certificate", "証明書", "名詞"), ("chain", "鎖", "名詞"),
    ("chair", "椅子", "名詞"), ("challenge", "挑戦", "名詞"), ("champion", "王者", "名詞"),
    ("chance", "機会", "名詞"), ("change", "変化", "名詞"), ("channel", "チャンネル", "名詞"),
    ("chapter", "章", "名詞"), ("character", "性格", "名詞"), ("characteristic", "特徴", "名詞"),
    ("charge", "料金", "名詞"), ("charity", "慈善", "名詞"), ("chart", "図表", "名詞"),
    ("chase", "追跡する", "動詞"), ("cheap", "安い", "形容詞"), ("cheat", "だます", "動詞"),
    ("check", "確認する", "動詞"), ("cheerful", "陽気な", "形容詞"), ("cheese", "チーズ", "名詞"),
    ("chef", "料理長", "名詞"), ("chemical", "化学物質", "名詞"), ("chemistry", "化学", "名詞"),
    ("chest", "胸", "名詞"), ("chief", "主要な", "形容詞"), ("childhood", "子供時代", "名詞"),
    ("china", "陶磁器", "名詞"), ("choice", "選択", "名詞"), ("choke", "窒息させる", "動詞"),
    ("choose", "選ぶ", "動詞"), ("chop", "切り刻む", "動詞"), ("chorus", "合唱", "名詞"),
    ("christian", "キリスト教徒", "名詞"), ("church", "教会", "名詞"), ("cigarette", "タバコ", "名詞"),
    ("cinema", "映画館", "名詞"), ("circle", "円", "名詞"), ("circumstance", "状況", "名詞"),
    ("citizen", "市民", "名詞"), ("city", "都市", "名詞"), ("civil", "市民の", "形容詞"),
    ("civilization", "文明", "名詞"), ("claim", "主張する", "動詞"), ("clap", "拍手する", "動詞"),
    ("class", "階級", "名詞"), ("classic", "名作", "名詞"), ("classical", "古典の", "形容詞")
]

grade_2_candidates = [
    ("abandon", "捨てる", "動詞"), ("ability", "能力", "名詞"), ("abolish", "廃止する", "動詞"),
    ("absorb", "吸収する", "動詞"), ("abstract", "抽象的な", "形容詞"), ("abuse", "虐待", "名詞"),
    ("academic", "学術的な", "形容詞"), ("accent", "訛り", "名詞"), ("access", "接近", "名詞"),
    ("accommodate", "収容する", "動詞"), ("accompany", "同行する", "動詞"), ("accomplish", "成し遂げる", "動詞"),
    ("accordance", "一致", "名詞"), ("account", "説明", "名詞"), ("accumulate", "蓄積する", "動詞"),
    ("accurate", "正確な", "形容詞"), ("accuse", "非難する", "動詞"), ("acid", "酸", "名詞"),
    ("acknowledge", "認める", "動詞"), ("acquire", "習得する", "動詞"), ("adapt", "適応させる", "動詞"),
    ("adequate", "十分な", "形容詞"), ("adjust", "調整する", "動詞"), ("administration", "管理", "名詞"),
    ("admission", "入場", "名詞"), ("adopt", "採用する", "動詞"), ("adore", "崇拝する", "動詞"),
    ("advocate", "主張する", "動詞"), ("aesthetic", "美的な", "形容詞"), ("affair", "出来事", "名詞"),
    ("affection", "愛情", "名詞"), ("agency", "代理店", "名詞"), ("agenda", "協議事項", "名詞"),
    ("agent", "代理人", "名詞"), ("aggressive", "攻撃的な", "形容詞"), ("agriculture", "農業", "名詞"),
    ("aid", "援助", "名詞"), ("aircraft", "航空機", "名詞"), ("alarm", "警報", "名詞"),
    ("alcohol", "アルコール", "名詞"), ("alert", "油断のない", "形容詞"), ("alien", "外国の", "形容詞"),
    ("alliance", "同盟", "名詞"), ("allocate", "割り当てる", "動詞"), ("alloy", "合金", "名詞"),
    ("ally", "同盟国", "名詞"), ("alphabet", "アルファベット", "名詞"), ("alter", "変える", "動詞"),
    ("alternative", "代替案", "名詞"), ("altitude", "高度", "名詞"), ("aluminium", "アルミニウム", "名詞"),
    ("amateur", "素人", "名詞"), ("amaze", "驚かせる", "動詞"), ("ambassador", "大使", "名詞"),
    ("ambiguous", "曖昧な", "形容詞"), ("ambition", "野望", "名詞"), ("ambitious", "野心的な", "形容詞"),
    ("ambulance", "救急車", "名詞"), ("amend", "修正する", "動詞"), ("amplify", "増幅する", "動詞"),
    ("amuse", "楽しませる", "動詞"), ("analogy", "類推", "名詞"), ("analysis", "分析", "名詞"),
    ("analyze", "分析する", "動詞"), ("ancestor", "祖先", "名詞"), ("anchor", "錨", "名詞"),
    ("anecdote", "逸話", "名詞"), ("angel", "天使", "名詞"), ("anger", "怒り", "名詞"),
    ("angle", "角度", "名詞"), ("anniversary", "記念日", "名詞"), ("annual", "年に一度の", "形容詞"),
    ("anonymous", "匿名の", "形容詞"), ("anticipate", "予期する", "動詞"), ("antique", "骨董品", "名詞"),
    ("anxiety", "不安", "名詞"), ("apartment", "アパート", "名詞"), ("apparent", "明らかな", "形容詞"),
    ("appeal", "訴える", "動詞"), ("appetite", "食欲", "名詞"), ("applaud", "拍手する", "動詞"),
    ("appliance", "器具", "名詞"), ("applicable", "適用できる", "形容詞"), ("appoint", "任命する", "動詞"),
    ("appraisal", "査定", "名詞"), ("apprentice", "見習い", "名詞"), ("appropriate", "適切な", "形容詞"),
    ("approval", "承認", "名詞"), ("approximate", "おおよその", "形容詞"), ("aquarium", "水族館", "名詞"),
    ("arbitrary", "恣意的な", "形容詞"), ("arch", "アーチ", "名詞"), ("architecture", "建築", "名詞"),
    ("archive", "公文書", "名詞"), ("aristocracy", "貴族", "名詞"), ("arithmetic", "算数", "名詞"),
    ("armor", "鎧", "名詞"), ("arouse", "刺激する", "動詞"), ("arrest", "逮捕する", "動詞"),
    ("arrow", "矢", "名詞"), ("artistic", "芸術的な", "形容詞"), ("ascent", "上昇", "名詞"),
    ("aspiration", "抱負", "名詞"), ("assail", "襲撃する", "動詞"), ("assassin", "暗殺者", "名詞"),
    ("assault", "強襲", "名詞"), ("assemble", "組み立てる", "動詞"), ("assembly", "集会", "名詞"),
    ("asset", "資産", "名詞"), ("assignment", "課題", "名詞"), ("assistant", "助手", "名詞"),
    ("association", "協会", "名詞"), ("assort", "分類する", "動詞"), ("assurance", "保証", "名詞"),
    ("assure", "請け合う", "動詞"), ("astonish", "驚天動地させる", "動詞"), ("astound", "びっくり仰天させる", "動詞"),
    ("astray", "道に迷って", "副詞"), ("astronaut", "宇宙飛行士", "名詞"), ("astronomy", "天文学", "名詞"),
    ("asylum", "収容所", "名詞"), ("athlete", "運動選手", "名詞"), ("athletic", "競技の", "形容詞"),
    ("atlas", "地図帳", "名詞"), ("atom", "原子", "名詞"), ("attachment", "愛着", "名詞"),
    ("attainment", "達成", "名詞"), ("attendance", "出席", "名詞"), ("attendant", "添乗員", "名詞"),
    ("attorney", "弁護士", "名詞"), ("attraction", "魅力", "名詞"), ("attractive", "魅力的な", "形容詞"),
    ("auction", "競売", "名詞"), ("audience", "観客", "名詞"), ("audit", "監査", "名詞"),
    ("audition", "オーディション", "名詞"), ("auditorium", "講堂", "名詞"), ("augment", "増やす", "動詞"),
    ("authentic", "本物の", "形容詞"), ("authority", "権限", "名詞"), ("authorize", "権限を与える", "動詞"),
    ("autobiography", "自叙伝", "名詞"), ("automate", "自動化する", "動詞"), ("automatic", "自動の", "形容詞"),
    ("automobile", "自動車", "名詞"), ("autonomous", "自律的な", "形容詞"), ("autopsy", "検死", "名詞"),
    ("auxiliary", "補助の", "形容詞"), ("avail", "役立つ", "動詞"), ("availability", "利用可能性", "名詞"),
    ("avalanche", "なだれ", "名詞"), ("avenge", "報復する", "動詞"), ("avenue", "大通り", "名詞"),
    ("average", "平均的な", "形容詞"), ("aversion", "嫌悪", "名詞"), ("avert", "そらす", "動詞"),
    ("aviation", "航空", "名詞"), ("avid", "熱心な", "形容詞"), ("avoidance", "回避", "名詞"),
    ("await", "待つ", "動詞"), ("awake", "目覚める", "動詞"), ("awaken", "目覚めさせる", "動詞"),
    ("award", "授与する", "動詞"), ("aware", "承知して", "形容詞"), ("awe", "畏敬", "名詞"),
    ("awesome", "素晴らしい", "形容詞"), ("awful", "ひどい", "形容詞"), ("awkward", "不器用な", "形容詞"),
    ("axis", "軸", "名詞"), ("bachelor", "独身男性", "名詞"), ("backbone", "背骨", "名詞"),
    ("background", "素性", "名詞"), ("backward", "後方の", "形容詞"), ("bacteria", "バクテリア", "名詞"),
    ("badge", "バッジ", "名詞"), ("baffle", "当惑させる", "動詞"), ("baggage", "手荷物類", "名詞"),
    ("bail", "保釈", "名詞"), ("bait", "餌", "名詞"), ("balance", "残高", "名詞"),
    ("bald", "はげた", "形容詞"), ("ballet", "バレエ", "名詞"), ("balloon", "気球", "名詞"),
    ("ballot", "投票", "名詞"), ("ban", "禁止", "名詞"), ("bandage", "包帯", "名詞"),
    ("bandit", "強盗", "名詞"), ("bang", "強打する", "動詞"), ("banish", "追放する", "動詞"),
    ("bankrupt", "破産した", "形容詞"), ("bankruptcy", "破産", "名詞"), ("banner", "旗", "名詞"),
    ("banquet", "宴会", "名詞"), ("bar", "棒", "名詞"), ("barbarian", "野蛮人", "名詞"),
    ("barbarous", "野蛮な", "形容詞"), ("barbecue", "バーベキュー", "名詞"), ("bare", "裸の", "形容詞"),
    ("barely", "かろうじて", "副詞"), ("bargain", "格安品", "名詞"), ("bark", "吠える", "動詞"),
    ("barley", "大麦", "名詞"), ("barometer", "気圧計", "名詞"), ("baron", "男爵", "名詞"),
    ("barrel", "樽", "名詞"), ("barren", "不毛の", "形容詞"), ("barrier", "障壁", "名詞"),
    ("barter", "物々交換する", "動詞"), ("base", "基盤", "名詞"), ("baseball", "野球", "名詞")
]

pre_2_filtered = []
for word, jap, cat in pre_2_candidates:
    if word not in seen:
        pre_2_filtered.append((word, jap, cat))
        seen.add(word)
    if len(pre_2_filtered) == 100:
        break

grade_2_filtered = []
for word, jap, cat in grade_2_candidates:
    if word not in seen:
        grade_2_filtered.append((word, jap, cat))
        seen.add(word)
    if len(grade_2_filtered) == 100:
        break

result = {
    "準2級": pre_2_filtered,
    "2級": grade_2_filtered
}

import sys
json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
