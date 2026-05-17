import json

additional_jun1 = [
  # 動詞 100語
  ("abdicate","退位する","動詞"),("abridge","短縮する","動詞"),("absolve","免除する","動詞"),
  ("abstain","控える","動詞"),("accentuate","強調する","動詞"),("accrue","蓄積する","動詞"),
  ("adhere","付着する","動詞"),("adjudicate","裁定する","動詞"),("admonish","戒める","動詞"),
  ("advocate","主張する","動詞"),("afflict","苦しめる","動詞"),("aggravate","悪化させる","動詞"),
  ("alienate","疎外する","動詞"),("allay","鎮める","動詞"),("alleviate","緩和する","動詞"),
  ("amalgamate","合体する","動詞"),("ameliorate","改善する","動詞"),("amplify","拡大する","動詞"),
  ("appease","なだめる","動詞"),("arbitrate","仲裁する","動詞"),("ascertain","確かめる","動詞"),
  ("assimilate","同化する","動詞"),("atone","償う","動詞"),("attenuate","弱める","動詞"),
  ("augment","増大させる","動詞"),("avert","防ぐ","動詞"),("bolster","強化する","動詞"),
  ("capitalize","利用する","動詞"),("catalyze","触媒する","動詞"),("circumscribe","制限する","動詞"),
  ("coalesce","合体する","動詞"),("codify","成文化する","動詞"),("compel","強制する","動詞"),
  ("conciliate","融和させる","動詞"),("confiscate","没収する","動詞"),("congregate","集まる","動詞"),
  ("connote","暗示する","動詞"),("constrain","制約する","動詞"),("contravene","違反する","動詞"),
  ("converge","収束する","動詞"),("corroborate","裏付ける","動詞"),("culminate","最高潮に達する","動詞"),
  ("curb","抑制する","動詞"),("decentralize","分権化する","動詞"),("delineate","概説する","動詞"),
  ("demarcate","区切る","動詞"),("denigrate","貶める","動詞"),("deplete","減らす","動詞"),
  ("derive","派生する","動詞"),("desist","やめる","動詞"),("deter","抑止する","動詞"),
  ("deviate","逸脱する","動詞"),("diffuse","広める","動詞"),("diminish","減らす","動詞"),
  ("discern","見分ける","動詞"),("discredit","信用を失わせる","動詞"),("dismantle","解体する","動詞"),
  ("disperse","分散する","動詞"),("displace","取って代わる","動詞"),("disseminate","普及させる","動詞"),
  ("dissolve","解散する","動詞"),("diverge","分岐する","動詞"),("dominate","支配する","動詞"),
  ("edify","啓発する","動詞"),("elicit","引き出す","動詞"),("empower","力を与える","動詞"),
  ("encapsulate","要約する","動詞"),("endorse","支持する","動詞"),("envisage","想像する","動詞"),
  ("epitomize","典型となる","動詞"),("erode","侵食する","動詞"),("evade","避ける","動詞"),
  ("exacerbate","悪化させる","動詞"),("exonerate","無罪にする","動詞"),("expedite","早める","動詞"),
  ("fabricate","作り上げる","動詞"),("falter","よろめく","動詞"),("fluctuate","変動する","動詞"),
  ("foster","育成する","動詞"),("galvanize","刺激する","動詞"),("garner","蓄える","動詞"),
  ("hamper","妨げる","動詞"),("herald","前触れとなる","動詞"),("impede","妨害する","動詞"),
  ("implicate","関係させる","動詞"),("inculcate","教え込む","動詞"),("induce","誘導する","動詞"),
  ("inhibit","阻害する","動詞"),("initiate","始める","動詞"),("instigate","扇動する","動詞"),
  ("intercede","仲介する","動詞"),("intimidate","脅す","動詞"),("invalidate","無効にする","動詞"),
  ("jeopardize","危険にさらす","動詞"),("languish","衰える","動詞"),("liquidate","清算する","動詞"),
  ("mandate","命じる","動詞"),("marginalize","周縁化する","動詞"),("mitigate","軽減する","動詞"),
  ("mobilize","動員する","動詞"),("nullify","無効にする","動詞"),("orchestrate","組織する","動詞"),
  ("perpetuate","持続させる","動詞"),("precipitate","引き起こす","動詞"),("proliferate","急増する","動詞"),

  # 名詞 100語
  ("abatement","軽減","名詞"),("aberration","異常","名詞"),("abeyance","中断","名詞"),
  ("abrogation","廃止","名詞"),("abstinence","禁欲","名詞"),("acrimony","辛辣さ","名詞"),
  ("acumen","洞察力","名詞"),("adversity","逆境","名詞"),("affiliation","所属","名詞"),
  ("aftermath","余波","名詞"),("alienation","疎外感","名詞"),("allegiance","忠誠心","名詞"),
  ("alleviation","緩和","名詞"),("altruism","利他主義","名詞"),("ambivalence","曖昧さ","名詞"),
  ("anachronism","時代錯誤","名詞"),("antagonism","敵対","名詞"),("antipathy","反感","名詞"),
  ("apprehension","懸念","名詞"),("arbitration","調停","名詞"),("archetype","原型","名詞"),
  ("ardor","熱意","名詞"),("austerity","緊縮財政","名詞"),("autonomy","自律性","名詞"),
  ("backlash","反発","名詞"),("belligerence","好戦性","名詞"),("benevolence","善意","名詞"),
  ("bias","偏見","名詞"),("bureaucracy","官僚制度","名詞"),("candor","率直さ","名詞"),
  ("catalyst","触媒","名詞"),("causality","因果関係","名詞"),("censorship","検閲","名詞"),
  ("chauvinism","偏狭な愛国心","名詞"),("coercion","強制","名詞"),("cognition","認知","名詞"),
  ("collusion","共謀","名詞"),("complacency","無関心","名詞"),("complexity","複雑性","名詞"),
  ("compliance","服従","名詞"),("concession","譲歩","名詞"),("condemnation","非難","名詞"),
  ("conformity","同調","名詞"),("confrontation","対立","名詞"),("consensus","合意","名詞"),
  ("contamination","汚染","名詞"),("contention","主張","名詞"),("contingency","緊急事態","名詞"),
  ("contradiction","矛盾","名詞"),("conviction","確信","名詞"),("credibility","信頼性","名詞"),
  ("culmination","頂点","名詞"),("cynicism","冷笑主義","名詞"),("decentralization","分権化","名詞"),
  ("deference","敬意","名詞"),("deprivation","剥奪","名詞"),("despondency","絶望","名詞"),
  ("deterrence","抑止力","名詞"),("dichotomy","二分法","名詞"),("discrepancy","食い違い","名詞"),
  ("disparity","格差","名詞"),("dissent","反論","名詞"),("doctrine","教義","名詞"),
  ("dominance","優位性","名詞"),("dysfunction","機能不全","名詞"),("elaboration","詳述","名詞"),
  ("emancipation","解放","名詞"),("empiricism","経験主義","名詞"),("encroachment","侵害","名詞"),
  ("equilibrium","均衡","名詞"),("erosion","侵食","名詞"),("evasion","回避","名詞"),
  ("exploitation","搾取","名詞"),("fallacy","誤謬","名詞"),("fluctuation","変動","名詞"),
  ("fragmentation","断片化","名詞"),("frugality","節約","名詞"),("futility","無駄","名詞"),
  ("globalization","グローバル化","名詞"),("governance","統治","名詞"),("grievance","不満","名詞"),
  ("hegemony","覇権","名詞"),("hubris","傲慢","名詞"),("hypocrisy","偽善","名詞"),
  ("idiosyncrasy","特異性","名詞"),("impasse","行き詰まり","名詞"),("imperialism","帝国主義","名詞"),
  ("inertia","慣性","名詞"),("injustice","不公正","名詞"),("insurgency","反乱","名詞"),
  ("intransigence","非妥協性","名詞"),("litigation","訴訟","名詞"),("manipulation","操作","名詞"),
  ("mediation","調停","名詞"),("momentum","勢い","名詞"),("monopoly","独占","名詞"),
  ("morality","道徳性","名詞"),("nepotism","縁故主義","名詞"),("notion","観念","名詞"),
  ("obligation","義務","名詞"),("oppression","抑圧","名詞"),("ostracism","追放","名詞"),

  # 形容詞 100語
  ("abstract","抽象的な","形容詞"),("accessible","利用しやすい","形容詞"),("accountable","説明責任のある","形容詞"),
  ("acrimonious","険悪な","形容詞"),("adamant","断固とした","形容詞"),("adept","熟達した","形容詞"),
  ("adversarial","対立的な","形容詞"),("ambivalent","態度がはっきりしない","形容詞"),("anachronistic","時代錯誤な","形容詞"),
  ("antagonistic","対立的な","形容詞"),("apathetic","無気力な","形容詞"),("arbitrary","恣意的な","形容詞"),
  ("ardent","熱心な","形容詞"),("astute","鋭敏な","形容詞"),("austere","厳格な","形容詞"),
  ("bellicose","好戦的な","形容詞"),("bilateral","二国間の","形容詞"),("callous","冷淡な","形容詞"),
  ("capricious","気まぐれな","形容詞"),("catastrophic","壊滅的な","形容詞"),("clandestine","秘密の","形容詞"),
  ("coercive","強制的な","形容詞"),("coherent","首尾一貫した","形容詞"),("collusive","共謀した","形容詞"),
  ("complacent","現状満足の","形容詞"),("compatible","互換性の","形容詞"),("compelling","説得力のある","形容詞"),
  ("complicit","共謀している","形容詞"),("concise","簡潔な","形容詞"),("conducive","有益な","形容詞"),
  ("conflicting","矛盾する","形容詞"),("contentious","論争的な","形容詞"),("contradictory","矛盾した","形容詞"),
  ("controversial","物議をかもす","形容詞"),("covert","秘密の","形容詞"),("credible","信頼できる","形容詞"),
  ("cumulative","累積的な","形容詞"),("cynical","冷笑的な","形容詞"),("daunting","気おじさせる","形容詞"),
  ("deceptive","人を欺く","形容詞"),("defiant","反抗的な","形容詞"),("detrimental","有害な","形容詞"),
  ("discerning","目の肥えた","形容詞"),("disconcerting","当惑させる","形容詞"),("disruptive","破壊的な","形容詞"),
  ("divergent","分岐した","形容詞"),("dogmatic","独断的な","形容詞"),("dubious","疑わしい","形容詞"),
  ("duplicitous","不誠実な","形容詞"),("dynamic","ダイナミックな","形容詞"),("egregious","甚大な","形容詞"),
  ("elusive","とらえどころのない","形容詞"),("empirical","実証的な","形容詞"),("enigmatic","謎めいた","形容詞"),
  ("ephemeral","短命な","形容詞"),("equitable","公平な","形容詞"),("erratic","不規則な","形容詞"),
  ("evasive","逃げ腰の","形容詞"),("excessive","過度な","形容詞"),("exclusive","独占的な","形容詞"),
  ("exhaustive","徹底的な","形容詞"),("explicit","明白な","形容詞"),("feasible","実現可能な","形容詞"),
  ("fervent","熱烈な","形容詞"),("flagrant","目に余る","形容詞"),("fleeting","つかの間の","形容詞"),
  ("formidable","手ごわい","形容詞"),("fragile","もろい","形容詞"),("frugal","倹約的な","形容詞"),
  ("futile","無駄な","形容詞"),("groundbreaking","画期的な","形容詞"),("hypocritical","偽善的な","形容詞"),
  ("hypothetical","仮定の","形容詞"),("idiosyncratic","特異な","形容詞"),("implicit","暗黙の","形容詞"),
  ("impetuous","衝動的な","形容詞"),("implacable","融通のきかない","形容詞"),("inadvertent","不注意な","形容詞"),
  ("indispensable","欠かせない","形容詞"),("inept","無能な","形容詞"),("inherent","固有の","形容詞"),
  ("insidious","陰険な","形容詞"),("intangible","無形の","形容詞"),("interdependent","相互依存の","形容詞"),
  ("intrinsic","本質的な","形容詞"),("irrevocable","取り消せない","形容詞"),("lethal","致命的な","形容詞"),
  ("marginal","わずかな","形容詞"),("meticulous","細心の","形容詞"),("myopic","近視眼的な","形容詞"),
  ("negligible","無視できる","形容詞"),("normative","規範的な","形容詞"),("omnipresent","遍在する","形容詞"),
  ("paradoxical","逆説的な","形容詞"),("paramount","最重要の","形容詞"),("plausible","もっともらしい","形容詞"),
  ("predominant","支配的な","形容詞"),("proactive","積極的な","形容詞"),("profound","深遠な","形容詞"),
  ("reciprocal","相互の","形容詞"),("resilient","回復力のある","形容詞"),("robust","頑丈な","形容詞"),
  ("sophisticated","洗練された","形容詞"),("systemic","組織的な","形容詞"),("tenuous","薄い","形容詞"),
  ("ubiquitous","至る所にある","形容詞"),("unprecedented","前例のない","形容詞"),("viable","実行可能な","形容詞"),
  ("volatile","不安定な","形容詞"),("vulnerable","傷つきやすい","形容詞"),
]

with open("/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json", encoding="utf-8") as f:
    current = json.load(f)

jun1_count = sum(1 for w in current if w["level"] == "準1級")
print(f"現在の準1級語数: {jun1_count}")

new_words = []
for i, (eng, jpn, cat) in enumerate(additional_jun1, jun1_count + 1):
    uid = f"11500000-{i:04d}-{i:04d}-{i:04d}-{i:012d}"
    new_words.append({"id": uid, "english": eng, "japanese": jpn, "category": cat, "level": "準1級"})

combined = current + new_words

for lv in ["4級","3級","準2級","2級","準1級","1級"]:
    c = sum(1 for w in combined if w["level"] == lv)
    print(f"  {lv}: {c}語")
print(f"総語数: {len(combined)}")

watch_out = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWord Watch App/Resources/words.json"
ios_out   = "/Users/endoushougo/Python_pjs/EnglishWord/EnglishWordIOS/Resources/words.json"
for path in [watch_out, ios_out]:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
print("Watch・iOS両方に書き込み完了")
