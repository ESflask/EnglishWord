import json

additional_level1 = [
  # 動詞 100語
  ("abhor","ひどく嫌う","動詞"),("abide","従う","動詞"),("abjure","放棄する","動詞"),
  ("abnegate","否定する","動詞"),("abrogate","廃止する","動詞"),("accede","同意する","動詞"),
  ("accentuate","強調する","動詞"),("accrue","蓄積する","動詞"),("adhere","付着する","動詞"),
  ("adjoin","隣接する","動詞"),("adulterate","混ぜ物をする","動詞"),("afflict","苦しめる","動詞"),
  ("affront","侮辱する","動詞"),("aggrandize","拡大する","動詞"),("aggrieve","悩ます","動詞"),
  ("alight","降りる","動詞"),("allude","ほのめかす","動詞"),("amend","修正する","動詞"),
  ("annex","併合する","動詞"),("apprehend","逮捕する","動詞"),("archaic","時代遅れにする","動詞"),
  ("arraign","起訴する","動詞"),("arrogate","自分のものにする","動詞"),("aspire","熱望する","動詞"),
  ("atone","償う","動詞"),("avert","防ぐ","動詞"),("belie","偽る","動詞"),
  ("bequeath","遺贈する","動詞"),("berate","叱る","動詞"),("betray","裏切る","動詞"),
  ("bewilder","当惑させる","動詞"),("blandish","おだてる","動詞"),("blight","損なう","動詞"),
  ("browbeat","脅す","動詞"),("burnish","磨く","動詞"),("cajole","言いくるめる","動詞"),
  ("canvass","調査する","動詞"),("cede","譲渡する","動詞"),("chide","叱る","動詞"),
  ("cleave","割る","動詞"),("coax","なだめる","動詞"),("cobble","修繕する","動詞"),
  ("coerce","強制する","動詞"),("compel","強いる","動詞"),("conciliate","なだめる","動詞"),
  ("confound","混乱させる","動詞"),("conquer","征服する","動詞"),("consummate","完成する","動詞"),
  ("contend","争う","動詞"),("controvert","反論する","動詞"),("convict","有罪にする","動詞"),
  ("counterfeit","偽造する","動詞"),("covet","欲しがる","動詞"),("cringe","縮み上がる","動詞"),
  ("debunk","暴く","動詞"),("decamp","逃げ出す","動詞"),("defer","延期する","動詞"),
  ("defraud","詐取する","動詞"),("demean","品位を下げる","動詞"),("demystify","解明する","動詞"),
  ("denounce","非難する","動詞"),("deprive","奪う","動詞"),("deride","嘲笑する","動詞"),
  ("desist","やめる","動詞"),("deter","思いとどまらせる","動詞"),("disclaim","否認する","動詞"),
  ("disconcert","狼狽させる","動詞"),("dislodge","追い出す","動詞"),("disparage","けなす","動詞"),
  ("displace","置き換える","動詞"),("dispute","争う","動詞"),("dissuade","思いとどまらせる","動詞"),
  ("distort","歪める","動詞"),("dupe","騙す","動詞"),("edify","教化する","動詞"),
  ("elicit","引き出す","動詞"),("embellish","飾る","動詞"),("embezzle","横領する","動詞"),
  ("emigrate","移住する","動詞"),("emulate","模倣する","動詞"),("encumber","邪魔する","動詞"),
  ("endure","耐える","動詞"),("estrange","疎遠にする","動詞"),("evict","退去させる","動詞"),
  ("exalt","称賛する","動詞"),("excise","切除する","動詞"),("exhort","促す","動詞"),
  ("expropriate","収用する","動詞"),("extort","脅し取る","動詞"),("fawn","こびる","動詞"),
  ("feign","偽る","動詞"),("filibuster","議事妨害する","動詞"),("flout","無視する","動詞"),
  ("foment","扇動する","動詞"),("forgo","断念する","動詞"),("fracture","骨折する","動詞"),
  ("fulminate","激しく非難する","動詞"),("garble","歪曲する","動詞"),("glean","収集する","動詞"),
  ("goad","駆り立てる","動詞"),("grieve","悲しむ","動詞"),("haggle","値切る","動詞"),
  ("harness","利用する","動詞"),("hasten","急がせる","動詞"),("impair","損なう","動詞"),
  ("impersonate","成りすます","動詞"),("implicate","関与させる","動詞"),("importune","しつこく頼む","動詞"),

  # 名詞 100語
  ("abeyance","一時停止","名詞"),("abyss","深淵","名詞"),("accolade","称賛","名詞"),
  ("acquittal","無罪判決","名詞"),("adage","ことわざ","名詞"),("affront","侮辱","名詞"),
  ("aggression","攻撃","名詞"),("alacrity","敏速さ","名詞"),("alienation","疎外","名詞"),
  ("allegiance","忠誠","名詞"),("allocation","配分","名詞"),("altercation","口論","名詞"),
  ("anguish","苦悩","名詞"),("animosity","憎しみ","名詞"),("annexation","併合","名詞"),
  ("apprehension","逮捕","名詞"),("arbitrariness","恣意性","名詞"),("archaism","古語","名詞"),
  ("ardor","熱意","名詞"),("artistry","芸術性","名詞"),("ascendancy","優位","名詞"),
  ("assertion","主張","名詞"),("astonishment","驚き","名詞"),("attrition","消耗","名詞"),
  ("audacity","大胆さ","名詞"),("austerity","緊縮","名詞"),("avarice","強欲","名詞"),
  ("backlash","反発","名詞"),("belligerency","交戦","名詞"),("bereavement","死別","名詞"),
  ("bigotry","偏見","名詞"),("bravado","虚勢","名詞"),("brevity","簡潔さ","名詞"),
  ("brinkmanship","瀬戸際政策","名詞"),("candor","率直さ","名詞"),("capitulation","降伏","名詞"),
  ("caricature","風刺画","名詞"),("carnage","大虐殺","名詞"),("casualty","犠牲者","名詞"),
  ("charlatan","詐欺師","名詞"),("chicanery","ごまかし","名詞"),("clemency","慈悲","名詞"),
  ("clout","影響力","名詞"),("coercion","強制","名詞"),("collateral","担保","名詞"),
  ("commotion","騒ぎ","名詞"),("compulsion","強制","名詞"),("conceit","うぬぼれ","名詞"),
  ("condemnation","非難","名詞"),("condescension","見下し","名詞"),("connivance","黙認","名詞"),
  ("consternation","狼狽","名詞"),("contempt","軽蔑","名詞"),("contention","争い","名詞"),
  ("contrition","後悔","名詞"),("contumacy","反抗","名詞"),("conviction","有罪","名詞"),
  ("corruption","腐敗","名詞"),("coup","クーデター","名詞"),("cowardice","臆病","名詞"),
  ("credulity","信じやすさ","名詞"),("cupidity","強欲","名詞"),("debasement","貶め","名詞"),
  ("deception","欺き","名詞"),("defiance","反抗","名詞"),("demagogy","扇動","名詞"),
  ("denouement","結末","名詞"),("depravity","堕落","名詞"),("dereliction","怠慢","名詞"),
  ("despotism","専制政治","名詞"),("destitution","極貧","名詞"),("diatribe","激しい非難","名詞"),
  ("disdain","軽蔑","名詞"),("dissension","不和","名詞"),("dissonance","不協和","名詞"),
  ("dogmatism","独断主義","名詞"),("domination","支配","名詞"),("dormancy","休眠","名詞"),
  ("duplicity","二心","名詞"),("durance","監禁","名詞"),("effrontery","厚かましさ","名詞"),
  ("elitism","エリート主義","名詞"),("empiricism","経験論","名詞"),("encroachment","侵害","名詞"),
  ("enmity","敵意","名詞"),("enormity","甚大さ","名詞"),("estrangement","疎外","名詞"),
  ("euphemism","婉曲表現","名詞"),("exaggeration","誇張","名詞"),("exasperation","激怒","名詞"),
  ("exile","追放","名詞"),("exploitation","搾取","名詞"),("extortion","恐喝","名詞"),
  ("fabrication","でっち上げ","名詞"),("fanaticism","狂信","名詞"),("farce","茶番","名詞"),
  ("fervency","熱烈さ","名詞"),("feud","確執","名詞"),("fiasco","大失敗","名詞"),
  ("fickleness","気まぐれ","名詞"),("flagrancy","露骨さ","名詞"),("flippancy","軽率さ","名詞"),
  ("foreboding","予感","名詞"),("forgery","偽造","名詞"),("fortitude","不屈の精神","名詞"),
  ("fraud","詐欺","名詞"),("frustration","欲求不満","名詞"),("futility","無益さ","名詞"),
  ("gallantry","勇敢さ","名詞"),("grievance","不満","名詞"),("guile","狡猾さ","名詞"),

  # 形容詞 100語
  ("abject","みじめな","形容詞"),("abominable","ひどい","形容詞"),("abrasive","刺激的な","形容詞"),
  ("absurd","ばかげた","形容詞"),("acerbic","辛辣な","形容詞"),("acrimonious","辛辣な","形容詞"),
  ("adept","熟練した","形容詞"),("adroit","器用な","形容詞"),("adversarial","対立的な","形容詞"),
  ("affronted","侮辱された","形容詞"),("aggrieved","憤慨した","形容詞"),("aghast","ぞっとした","形容詞"),
  ("aloof","よそよそしい","形容詞"),("altruistic","利他的な","形容詞"),("ambiguous","曖昧な","形容詞"),
  ("amiable","愛想のよい","形容詞"),("amicable","友好的な","形容詞"),("anarchic","無政府的な","形容詞"),
  ("antagonistic","敵対的な","形容詞"),("antiquated","時代遅れの","形容詞"),("apocryphal","信憑性のない","形容詞"),
  ("arduous","骨の折れる","形容詞"),("arrogant","傲慢な","形容詞"),("astute","抜け目ない","形容詞"),
  ("atrocious","残酷な","形容詞"),("avaricious","貪欲な","形容詞"),("averse","嫌って","形容詞"),
  ("banal","陳腐な","形容詞"),("beguiling","魅惑的な","形容詞"),("belated","遅れた","形容詞"),
  ("belligerent","好戦的な","形容詞"),("benign","良性の","形容詞"),("blatant","露骨な","形容詞"),
  ("boisterous","騒々しい","形容詞"),("brusque","ぶっきらぼうな","形容詞"),("bumptious","生意気な","形容詞"),
  ("callous","冷淡な","形容詞"),("callow","未熟な","形容詞"),("cantankerous","口やかましい","形容詞"),
  ("capricious","気まぐれな","形容詞"),("caustic","腐食性の","形容詞"),("cavalier","いいかげんな","形容詞"),
  ("censorious","批判的な","形容詞"),("churlish","無礼な","形容詞"),("circuitous","遠回りな","形容詞"),
  ("clairvoyant","透視できる","形容詞"),("clandestine","秘密の","形容詞"),("coercive","強制的な","形容詞"),
  ("complacent","自己満足した","形容詞"),("condescending","見下した","形容詞"),("conniving","陰謀を企む","形容詞"),
  ("contemptuous","軽蔑的な","形容詞"),("contrarian","反対する","形容詞"),("convoluted","複雑な","形容詞"),
  ("corrosive","腐食性の","形容詞"),("craven","臆病な","形容詞"),("credulous","信じやすい","形容詞"),
  ("cunning","狡猾な","形容詞"),("deceptive","欺瞞的な","形容詞"),("defiant","反抗的な","形容詞"),
  ("degenerate","退廃した","形容詞"),("deleterious","有害な","形容詞"),("delinquent","非行の","形容詞"),
  ("delusional","妄想的な","形容詞"),("demoralized","意気消沈した","形容詞"),("deplorable","嘆かわしい","形容詞"),
  ("depraved","堕落した","形容詞"),("derisive","嘲笑的な","形容詞"),("despicable","卑劣な","形容詞"),
  ("deviant","逸脱した","形容詞"),("devious","狡猾な","形容詞"),("dictatorial","独裁的な","形容詞"),
  ("diffident","自信のない","形容詞"),("dilapidated","荒廃した","形容詞"),("disenchanted","幻滅した","形容詞"),
  ("disingenuous","不誠実な","形容詞"),("dismissive","一蹴する","形容詞"),("dispassionate","冷静な","形容詞"),
  ("disreputable","評判の悪い","形容詞"),("dissident","反体制の","形容詞"),("dogmatic","独断的な","形容詞"),
  ("domineering","横柄な","形容詞"),("draconian","厳しすぎる","形容詞"),("duplicitous","二枚舌の","形容詞"),
  ("dysfunctional","機能不全の","形容詞"),("ebullient","元気いっぱいの","形容詞"),("eccentric","奇人の","形容詞"),
  ("egotistical","自己中心的な","形容詞"),("elitist","エリート主義的な","形容詞"),("embittered","恨みを持つ","形容詞"),
  ("empirical","経験的な","形容詞"),("enigmatic","謎めいた","形容詞"),("erratic","気まぐれな","形容詞"),
  ("evasive","回避的な","形容詞"),("exorbitant","法外な","形容詞"),("expedient","便宜的な","形容詞"),
  ("extravagant","贅沢な","形容詞"),("fanatical","狂信的な","形容詞"),("fastidious","気難しい","形容詞"),
  ("flippant","軽率な","形容詞"),("foreboding","不吉な","形容詞"),("fraudulent","詐欺的な","形容詞"),
  ("furtive","こそこそした","形容詞"),("gaudy","派手な","形容詞"),("grandiloquent","大げさな","形容詞"),
  ("gullible","だまされやすい","形容詞"),("hapless","不運な","形容詞"),("harrowing","胸を引き裂く","形容詞"),
]

# 現在のwords.jsonを読み込む
with open("/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json", encoding="utf-8") as f:
    current = json.load(f)

# 現在の最大インデックスを確認
level1_count = sum(1 for w in current if w["level"] == "1級")
print(f"現在の1級語数: {level1_count}")

# 追加単語のUUIDを生成（既存と衝突しないよう大きなオフセットから）
new_words = []
for i, (eng, jpn, cat) in enumerate(additional_level1, level1_count + 1):
    uid = f"11000000-{i:04d}-{i:04d}-{i:04d}-{i:012d}"
    new_words.append({"id": uid, "english": eng, "japanese": jpn, "category": cat, "level": "1級"})

combined = current + new_words
new_level1 = sum(1 for w in combined if w["level"] == "1級")
print(f"追加後の1級語数: {new_level1}")
print(f"総語数: {len(combined)}")

out = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)
print("書き込み完了")
