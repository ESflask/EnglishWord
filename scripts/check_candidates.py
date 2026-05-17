
import json

existing_words = set(json.load(open('existing_words.json')))

# Large pool of candidates for each level
# (english, japanese, category)
pools = {
    "4級": [
        ("banana","バナナ","名詞"), ("grape","ぶどう","名詞"), ("melon","メロン","名詞"),
        ("peach","桃","名詞"), ("cherry","さくらんぼ","名詞"), ("strawberry","いちご","名詞"),
        ("potato","じゃがいも","名詞"), ("onion","玉ねぎ","名詞"), ("carrot","にんじん","名詞"),
        ("corn","とうもろこし","名詞"), ("pumpkin","かぼちゃ","名詞"), ("cabbage","キャベツ","名詞"),
        ("cucumber","きゅうり","名詞"), ("eye","目","名詞"), ("ear","耳","名詞"),
        ("mouth","口","名詞"), ("tooth","歯","名詞"), ("finger","指","名詞"),
        ("toe","足の指","名詞"), ("knee","膝","名詞"), ("elbow","肘","名詞"),
        ("stomach","胃","名詞"), ("pants","ズボン","名詞"), ("socks","靴下","名詞"),
        ("skirt","スカート","名詞"), ("jacket","ジャケット","名詞"), ("gloves","手袋","名詞"),
        ("scarf","スカーフ","名詞"), ("boots","ブーツ","名詞"), ("yellow","黄色い","形容詞"),
        ("brown","茶色の","形容詞"), ("pink","桃色の","形容詞"), ("purple","紫色の","形容詞"),
        ("gray","灰色の","形容詞"), ("silver","銀色の","形容詞"), ("gold","金色の","形容詞"),
        ("square","四角い","形容詞"), ("triangle","三角の","名詞"), ("oval","楕円形の","形容詞"),
        ("zero","ゼロ","名詞"), ("eleven","11","名詞"), ("twelve","12","名詞"),
        ("thirteen","13","名詞"), ("fourteen","14","名詞"), ("fifteen","15","名詞"),
        ("sixteen","16","名詞"), ("seventeen","17","名詞"), ("eighteen","18","名詞"),
        ("nineteen","19","名詞"), ("twenty","20","名詞"), ("thirty","30","名詞"),
        ("forty","40","名詞"), ("fifty","50","名詞"), ("sixty","60","名詞"),
        ("seventy","70","名詞"), ("eighty","80","名詞"), ("ninety","90","名詞"),
        ("hundred","100","名詞"), ("thousand","1000","名詞"), ("million","100万","名詞"),
        ("monday","月曜日","名詞"), ("tuesday","火曜日","名詞"), ("wednesday","水曜日","名詞"),
        ("thursday","木曜日","名詞"), ("friday","金曜日","名詞"), ("saturday","土曜日","名詞"),
        ("sunday","日曜日","名詞"), ("spring","春","名詞"), ("autumn","秋","名詞"),
        ("snowy","雪の降る","形容詞"), ("singer","歌手","名詞"), ("violin","バイオリン","名詞"),
        ("guitar","ギター","名詞"), ("flute","フルート","名詞"), ("trumpet","トランペット","名詞"),
        ("drum","ドラム","名詞"), ("baseball","野球","名詞"), ("tennis","テニス","名詞"),
        ("basketball","バスケットボール","名詞"), ("volleyball","バレーボール","名詞"),
        ("badminton","バドミントン","名詞"), ("restroom","トイレ","名詞"), ("balcony","バルコニー","名詞"),
        ("elevator","エレベーター","名詞"), ("fence","フェンス","名詞"), ("basement","地下室","名詞"),
        ("bookstore","本屋","名詞"), ("bakery","パン屋","名詞"), ("tunnel","トンネル","名詞"),
        ("pond","池","名詞"), ("fog","霧","名詞"), ("storm","嵐","名詞"),
        ("airplane","飛行機","名詞"), ("motorcycle","オートバイ","名詞"), ("van","バン","名詞"),
        ("canoe","カヌー","名詞"), ("taxi","タクシー","名詞"), ("helicopter","ヘリコプター","名詞"),
        ("rocket","ロケット","名詞"), ("tablet","タブレット","名詞"), ("television","テレビ","名詞"),
        ("mirror","鏡","名詞"), ("brush","ブラシ","名詞"), ("shampoo","シャンプー","名詞"),
        ("blanket","毛布","名詞"), ("pillow","枕","名詞"), ("curtain","カーテン","名詞"),
        ("shelf","棚","名詞"), ("glue","のり","名詞"), ("pencil","鉛筆","名詞"),
        ("eraser","消しゴム","名詞"), ("ruler","定規","名詞"), ("backpack","バックパック","名詞"),
        ("sketchbook","スケッチブック","名詞"), ("socks","靴下","名詞")
    ],
    "3級": [
        ("adventure","冒険","名詞"), ("average","平均","名詞"), ("baggage","手荷物","名詞"),
        ("baseball","野球","名詞"), ("between","〜の間に","副詞"), ("blanket","毛布","名詞"),
        ("bottom","底","名詞"), ("business","ビジネス","名詞"), ("charity","慈善","名詞"),
        ("coach","コーチ","名詞"), ("coast","海岸","名詞"), ("common","共通の","形容詞"),
        ("complain","不平を言う","動詞"), ("congratulations","おめでとう","名詞"), ("couple","カップル","名詞"),
        ("courage","勇気","名詞"), ("curtain","カーテン","名詞"), ("daughter","娘","名詞"),
        ("daytime","昼間","名詞"), ("delicious","おいしい","形容詞"), ("destroy","破壊する","動詞"),
        ("directly","直接に","副詞"), ("distance","距離","名詞"), ("double","二倍の","形容詞"),
        ("drawer","引き出し","名詞"), ("during","〜の間に","副詞"), ("easily","簡単に","副詞"),
        ("eighty","80","名詞"), ("either","どちらかの","形容詞"), ("electric","電気の","形容詞"),
        ("electronic","電子の","形容詞"), ("elephant","象","名詞"), ("elevator","エレベーター","名詞"),
        ("escape","逃げる","動詞"), ("especially","特に","副詞"), ("ever","今まで","副詞"),
        ("exactly","正確に","副詞"), ("except","〜を除いて","副詞"), ("exciting","刺激的な","形容詞"),
        ("exhibition","展覧会","名詞"), ("extra","余分な","形容詞"), ("fantastic","空想的な","形容詞"),
        ("fashion","ファッション","名詞"), ("feather","羽","名詞"), ("female","女性の","形容詞"),
        ("fifty","50","名詞"), ("figure","数字","名詞"), ("finally","ついに","副詞"),
        ("fireworks","花火","名詞"), ("forward","前方へ","副詞"), ("frightened","怯えた","形容詞"),
        ("front","前面","名詞"), ("fun","楽しみ","名詞"), ("furniture","家具","名詞"),
        ("future","未来","名詞"), ("gallery","画廊","名詞"), ("gas","ガス","名詞"),
        ("glass","グラス","名詞"), ("gradually","徐々に","副詞"), ("grammar","文法","名詞"),
        ("guitar","ギター","名詞"), ("happiness","幸福","名詞"), ("hardly","ほとんど〜ない","副詞"),
        ("height","高さ","名詞"), ("hero","英雄","名詞"), ("hostel","ホステル","名詞"),
        ("however","しかしながら","副詞"), ("huge","巨大な","形容詞"), ("if","もし〜なら","副詞"),
        ("immediately","すぐに","副詞"), ("impossible","不可能な","形容詞"), ("indeed","本当に","副詞"),
        ("indoor","屋内の","形容詞"), ("insect","昆虫","名詞"), ("inside","内側に","副詞"),
        ("instead","代わりに","副詞"), ("into","〜の中へ","副詞"), ("invitation","招待","名詞"),
        ("itself","それ自身","副詞"), ("jacket","ジャケット","名詞"), ("jewelry","宝石","名詞"),
        ("joke","冗談","名詞"), ("joy","喜び","名詞"), ("junior","年下の","形容詞"),
        ("kid","子供","名詞"), ("kill","殺す","動詞"), ("kindness","親切","名詞"),
        ("kiss","キス","名詞"), ("knee","膝","名詞"), ("label","ラベル","名詞"),
        ("leaf","葉","名詞"), ("least","最小の","形容詞"), ("lecture","講義","名詞"),
        ("left","左","名詞"), ("lemon","レモン","名詞"), ("length","長さ","名詞"),
        ("less","より少ない","形容詞"), ("let","〜させる","動詞"), ("lie","嘘をつく","動詞"),
        ("life","生活","名詞"), ("lift","持ち上げる","動詞"), ("lion","ライオン","名詞"),
        ("lip","唇","名詞"), ("list","リスト","名詞"), ("lovely","素敵な","形容詞"),
        ("luck","運","名詞"), ("mall","モール","名詞"), ("manager","マネージャー","名詞"),
        ("manner","マナー","名詞"), ("mask","マスク","名詞"), ("meaning","意味","名詞"),
        ("medal","メダル","名詞"), ("mile","マイル","名詞"), ("mistake","間違い","名詞")
    ],
    "準2級": [
        ("addition","追加","名詞"), ("agent","代理人","名詞"), ("ahead","前方へ","副詞"),
        ("alive","生きて","形容詞"), ("almost","ほとんど","副詞"), ("along","〜に沿って","副詞"),
        ("although","〜だけれども","副詞"), ("altogether","完全に","副詞"), ("amazing","素晴らしい","形容詞"),
        ("anger","怒り","名詞"), ("angle","角度","名詞"), ("another","別の","形容詞"),
        ("anybody","誰でも","副詞"), ("anyhow","とにかく","副詞"), ("anymore","これ以上","副詞"),
        ("anyone","誰でも","副詞"), ("anything","何か","副詞"), ("anyway","とにかく","副詞"),
        ("anywhere","どこでも","副詞"), ("apart","離れて","副詞"), ("apparent","明らかな","形容詞"),
        ("appoint","指名する","動詞"), ("appreciate","感謝する","動詞"), ("approval","承認","名詞"),
        ("around","周囲に","副詞"), ("arrange","手配する","動詞"), ("artist","芸術家","名詞"),
        ("asleep","眠って","形容詞"), ("assign","割り当てる","動詞"), ("assistant","助手","名詞"),
        ("athlete","運動選手","名詞"), ("attack","攻撃する","動詞"), ("attempt","試みる","動詞"),
        ("attract","引きつける","動詞"), ("author","著者","名詞"), ("average","平均","形容詞"),
        ("avoid","避ける","動詞"), ("awake","目覚めて","形容詞"), ("award","賞","名詞"),
        ("balance","バランス","名詞"), ("balloon","風船","名詞"), ("base","土台","名詞"),
        ("battle","戦い","名詞"), ("beauty","美しさ","名詞"), ("beg","乞う","動詞"),
        ("behave","振る舞う","動詞"), ("behind","後ろに","副詞"), ("below","下に","副詞"),
        ("bench","ベンチ","名詞"), ("beside","そばに","副詞"), ("beyond","越えて","副詞"),
        ("birth","誕生","名詞"), ("bit","少し","名詞"), ("blind","盲目の","形容詞"),
        ("block","ブロック","名詞"), ("blood","血","名詞"), ("blow","吹く","動詞"),
        ("board","板","名詞"), ("boil","沸騰する","動詞"), ("bone","骨","名詞"),
        ("born","生まれた","形容詞"), ("borrow","借りる","動詞"), ("both","両方の","形容詞"),
        ("bottle","ボトル","名詞"), ("bottom","底","名詞"), ("bowl","鉢","名詞"),
        ("brain","脳","名詞"), ("branch","枝","名詞"), ("brave","勇敢な","形容詞"),
        ("breath","呼吸","名詞"), ("breathe","呼吸する","動詞"), ("bright","明るい","形容詞"),
        ("bring","持ってくる","動詞"), ("broad","広い","形容詞"), ("brush","ブラシ","名詞"),
        ("build","建てる","動詞"), ("bunch","束","名詞"), ("burn","燃える","動詞"),
        ("bury","埋める","動詞"), ("bush","低木","名詞"), ("business","ビジネス","名詞"),
        ("busy","忙しい","形容詞"), ("button","ボタン","名詞"), ("cabin","小屋","名詞"),
        ("cage","檻","名詞"), ("calm","穏やかな","形容詞"), ("camp","キャンプ","名詞"),
        ("can","缶","名詞"), ("canal","運河","名詞"), ("cancel","取り消す","動詞"),
        ("candle","ろうそく","名詞"), ("candy","キャンディー","名詞"), ("cap","キャップ","名詞"),
        ("capital","資本","名詞"), ("captain","船長","名詞"), ("card","カード","名詞"),
        ("care","世話","名詞"), ("careful","注意深い","形容詞"), ("carpenter","大工","名詞")
    ],
    "2級": [
        ("absolute","絶対的な","形容詞"), ("academic","学問的な","形容詞"), ("accent","アクセント","名詞"),
        ("acceptance","受諾","名詞"), ("accomplish","成し遂げる","動詞"), ("according","〜によれば","副詞"),
        ("accountant","会計士","名詞"), ("accusation","告発","名詞"), ("accustomed","慣れた","形容詞"),
        ("achievable","達成可能な","形容詞"), ("acid","酸","名詞"), ("across","〜を横切って","副詞"),
        ("action","行動","名詞"), ("activate","活性化する","動詞"), ("active","活発な","形容詞"),
        ("activist","活動家","名詞"), ("actress","女優","名詞"), ("acute","鋭い","形容詞"),
        ("adjustment","調整","名詞"), ("administrative","管理の","形容詞"), ("admirable","立派な","形容詞"),
        ("admiral","提督","名詞"), ("admiration","感嘆","名詞"), ("admission","入場","名詞"),
        ("admittance","入場許可","名詞"), ("adolescence","思春期","名詞"), ("adolescent","青年期の","形容詞"),
        ("adorable","可愛らしい","形容詞"), ("adore","敬愛する","動詞"), ("advancement","進歩","名詞"),
        ("advantageous","有利な","形容詞"), ("adventure","冒険","名詞"), ("adventurous","冒険好きな","形容詞"),
        ("adverb","副詞","名詞"), ("adverse","逆境の","形容詞"), ("advertise","広告する","動詞"),
        ("advertisement","広告","名詞"), ("advisable","勧めるべき","形容詞"), ("adviser","助言者","名詞"),
        ("aesthetic","美的な","形容詞"), ("affair","事件","名詞"), ("affection","愛情","名詞"),
        ("affectionate","愛情深い","形容詞"), ("affiliate","提携する","動詞"), ("affirm","断言する","動詞"),
        ("affirmative","肯定的な","形容詞"), ("affix","添付する","動詞"), ("afflict","苦しめる","動詞"),
        ("afford","〜する余裕がある","動詞"), ("affordable","手頃な","形容詞"), ("agenda","協議事項","名詞"),
        ("aggression","攻撃性","名詞"), ("agriculture","農業","名詞"), ("airplane","飛行機","名詞"),
        ("aisle","通路","名詞"), ("alarm","警報","名詞"), ("alcohol","アルコール","名詞"),
        ("alert","警戒して","形容詞"), ("alliance","同盟","名詞"), ("allowance","手当","名詞"),
        ("ally","同盟国","名詞"), ("alphabet","アルファベット","名詞"), ("alteration","変更","名詞"),
        ("altitude","高度","名詞"), ("aluminum","アルミニウム","名詞"), ("amateur","アマチュア","名詞"),
        ("ambassador","大使","名詞"), ("ambition","野心","名詞"), ("ambulance","救急車","名詞"),
        ("amendment","修正","名詞"), ("ample","十分な","形容詞"), ("amusement","楽しみ","名詞"),
        ("analogy","類推","名詞"), ("analysis","分析","名詞"), ("ancestor","先祖","名詞"),
        ("anchor","錨","名詞"), ("ancient","古代の","形容詞"), ("angel","天使","名詞"),
        ("anniversary","周年","名詞"), ("annual","例年の","形容詞"), ("antenna","アンテナ","名詞"),
        ("antique","骨董品","名詞"), ("anxiety","不安","名詞"), ("anyhow","とにかく","副詞"),
        ("apartment","アパート","名詞"), ("apology","謝罪","名詞"), ("apparatus","器具","名詞"),
        ("apparent","明白な","形容詞"), ("appetite","食欲","名詞"), ("applaud","拍手する","動詞"),
        ("appliance","器具","名詞"), ("applicant","志願者","名詞"), ("appoint","任命する","動詞"),
        ("appraisal","評価","名詞"), ("appreciate","感謝する","動詞"), ("apprentice","見習い","名詞"),
        ("approval","承認","名詞"), ("apron","エプロン","名詞"), ("aquarium","水族館","名詞"),
        ("arch","アーチ","名詞"), ("architecture","建築","名詞"), ("archive","公文書","名詞")
    ],
    "準1級": [
        ("abbreviate","省略する","動詞"), ("abound","たくさんある","動詞"), ("abrupt","突然の","形容詞"),
        ("absentee","欠席者","名詞"), ("absolute","絶対の","形容詞"), ("abundant","豊富な","形容詞"),
        ("abuse","虐待","名詞"), ("academic","学業の","形容詞"), ("accent","アクセント","名詞"),
        ("accidentally","偶然に","副詞"), ("acclaim","称賛","名詞"), ("accomplish","果たす","動詞"),
        ("accord","一致","名詞"), ("accordance","一致","名詞"), ("accordingly","それに応じて","副詞"),
        ("accountant","会計士","名詞"), ("accumulation","蓄積","名詞"), ("accurately","正確に","副詞"),
        ("accusation","告発","名詞"), ("accustomed","慣れている","形容詞"), ("achievable","達成できる","形容詞"),
        ("acid","酸性の","形容詞"), ("acknowledgment","承認","名詞"), ("acquaint","知らせる","動詞"),
        ("acre","エーカー","名詞"), ("activate","作動させる","動詞"), ("activism","活動主義","名詞"),
        ("activist","活動家","名詞"), ("actuality","現実","名詞"), ("acute","深刻な","形容詞"),
        ("adaptability","適応性","名詞"), ("addict","中毒者","名詞"), ("addiction","中毒","名詞"),
        ("additionally","さらに","副詞"), ("adequacy","妥当性","名詞"), ("adequately","適切に","副詞"),
        ("adherence","固執","名詞"), ("adjective","形容詞","名詞"), ("adjustable","調節可能な","形容詞"),
        ("adjustment","調節","名詞"), ("administrative","管理上の","形容詞"), ("administrator","管理者","名詞"),
        ("admirable","賞賛に値する","形容詞"), ("admirably","見事に","副詞"), ("admiral","提督","名詞"),
        ("admiration","感嘆","名詞"), ("advocacy","弁護","名詞"), ("aesthetic","美的な","形容詞"),
        ("affectionate","愛情深い","形容詞"), ("affirmative","肯定的な","形容詞"), ("affluence","富","名詞"),
        ("aftermath","余波","名詞"), ("agenda","協議事項","名詞"), ("aggravate","悪化させる","動詞"),
        ("aggregate","総計の","形容詞"), ("agitation","動揺","名詞"), ("alienation","疎外","名詞"),
        ("alignment","提携","名詞"), ("allegation","申し立て","名詞"), ("alleviate","軽減する","動詞"),
        ("allocation","割り当て","名詞"), ("allowance","手当","名詞"), ("allude","ほのめかす","動詞"),
        ("allure","魅惑","名詞"), ("alphabetical","アルファベット順の","形容詞"), ("alteration","変更","名詞"),
        ("alternate","交互の","形容詞"), ("alternative","代替の","形容詞"), ("altitude","高度","名詞"),
        ("ambassador","大使","名詞"), ("ambiguity","曖昧さ","名詞"), ("ambivalence","ためらい","名詞"),
        ("amend","修正する","動詞"), ("amenity","快適さ","名詞"), ("amiable","愛想の良い","形容詞"),
        ("amicable","友好的な","形容詞"), ("ample","十分な","形容詞"), ("analogy","類推","名詞"),
        ("analytical","分析的な","形容詞"), ("ancestor","先祖","名詞"), ("ancillary","補助の","形容詞"),
        ("anecdote","逸話","名詞"), ("annex","併合する","動詞"), ("annihilation","全滅","名詞"),
        ("annotation","注釈","名詞"), ("annuity","年金","名詞"), ("anonymous","匿名の","形容詞"),
        ("antagonism","敵対","名詞"), ("anticipation","期待","名詞"), ("appendix","付録","名詞"),
        ("appliance","器具","名詞"), ("applicable","適用できる","形容詞"), ("appraisal","評価","名詞"),
        ("appreciation","感謝","名詞"), ("apprehension","不安","名詞"), ("apprentice","見習い","名詞"),
        ("appropriate","適切な","形容詞"), ("approval","承認","名詞"), ("approximate","おおよその","形容詞"),
        ("aptitude","才能","名詞"), ("aquatic","水生の","形容詞"), ("arbitrary","任意の","形容詞"),
        ("archetype","原型","名詞")
    ],
    "1級": [
        ("abate","和らぐ","動詞"), ("abnegation","拒絶","名詞"), ("aboriginal","先住の","形容詞"),
        ("abortive","失敗に終わった","形容詞"), ("abound","満ちている","動詞"), ("abridge","要約する","動詞"),
        ("abrupt","ぶっきらぼうな","形容詞"), ("abscond","逃亡する","動詞"), ("absolution","免罪","名詞"),
        ("absolve","免除する","動詞"), ("abstracted","心ここにあらずの","形容詞"), ("abstruse","難解な","形容詞"),
        ("abysmal","底知れぬ","形容詞"), ("acclaim","喝采を送る","動詞"), ("acclimatize","順応させる","動詞"),
        ("acclivity","上り坂","名詞"), ("accommodating","親切な","形容詞"), ("accomplice","共犯者","名詞"),
        ("accord","一致する","動詞"), ("accost","話しかける","動詞"), ("accoutre","装束を着せる","動詞"),
        ("accretion","増大","名詞"), ("acetous","酢のような","形容詞"), ("achromatic","無色の","形容詞"),
        ("acidulous","少し酸っぱい","形容詞"), ("acme","絶頂","名詞"), ("acoustic","音響の","形容詞"),
        ("acquiescence","黙認","名詞"), ("acquisitive","欲張りな","形容詞"), ("acquit","無罪にする","動詞"),
        ("acrid","刺激臭のある","形容詞"), ("acrophobia","高所恐怖症","名詞"), ("actionable","告訴できる","形容詞"),
        ("activate","活動的にする","動詞"), ("actuate","作動させる","動詞"), ("acuity","鋭さ","名詞"),
        ("acute","激しい","形容詞"), ("addendum","付録","名詞"), ("addiction","執着","名詞"),
        ("addle","混乱させる","動詞"), ("adduce","提示する","動詞"), ("adherence","忠実","名詞"),
        ("adherent","支持者","名詞"), ("adhesion","接着","名詞"), ("adhesive","接着剤","名詞"),
        ("adieu","さらば","名詞"), ("adipose","脂肪の","形容詞"), ("adjourn","休会する","動詞"),
        ("adjudge","判決を下す","動詞"), ("adjunct","付属品","名詞"), ("adjuration","厳命","名詞"),
        ("adjure","厳命する","動詞"), ("adjutant","副官","名詞"), ("adjuvant","補助の","形容詞"),
        ("admirable","感心な","形容詞"), ("admiralty","海軍本部","名詞"), ("bamboozle","騙す","動詞"),
        ("bandwagon","流行","名詞"), ("banish","追放する","動詞"), ("banter","冗談","名詞"),
        ("barb","刺","名詞"), ("baroque","バロック様式の","形容詞"), ("barrage","集中砲火","名詞"),
        ("bask","日向ぼっこをする","動詞"), ("bastion","砦","名詞"), ("batten","固定する","動詞"),
        ("bauble","安物","名詞"), ("bawdy","卑猥な","形容詞"), ("beatific","至福の","形容詞"),
        ("bedazzle","幻惑する","動詞"), ("bedraggle","汚す","動詞"), ("befuddle","当惑させる","動詞"),
        ("beget","生じさせる","動詞"), ("begrudge","惜しむ","動詞"), ("behemoth","巨大なもの","名詞"),
        ("beholden","恩義がある","形容詞"), ("behoove","〜すべきである","動詞"), ("belabor","詳しく説明する","動詞"),
        ("beleaguer","包囲する","動詞"), ("belittle","けなす","動詞"), ("bemused","困惑した","形容詞"),
        ("benediction","祝福","名詞"), ("benefactor","恩人","名詞"), ("beneficent","慈悲深い","形容詞"),
        ("benighted","無知な","形容詞"), ("bereave","奪う","動詞"), ("berserk","狂暴な","形容詞"),
        ("beseech","懇願する","動詞"), ("beset","悩ます","動詞"), ("besmirch","汚す","動詞"),
        ("bestial","獣のような","形容詞"), ("bestow","授ける","動詞"), ("betoken","示す","動詞"),
        ("betroth","婚約させる","動詞"), ("beverage","飲み物","名詞"), ("bewail","嘆く","動詞"),
        ("bibliography","参考文献目録","名詞"), ("bicameral","二院制の","形容詞"), ("bicker","口論する","動詞"),
        ("biennial","二年ごとの","形容詞"), ("bifurcated","二叉に分かれた","形容詞"), ("bilious","怒りっぽい","形容詞")
    ]
}

# common pool (emergency backup)
common_pool = [
    ("forecast","予報","名詞"), ("quietly","静かに","副詞"), ("railway","鉄道","名詞"),
    ("umbrella","傘","名詞"), ("village","村","名詞"), ("welcome","歓迎する","動詞"),
    ("yesterday","昨日","名詞"), ("pajamas","パジャマ","名詞"), ("tie","ネクタイ","名詞"),
    ("belt","ベルト","名詞"), ("beige","ベージュ","形容詞"), ("navy","紺色","形容詞"),
    ("diamond","菱形","名詞"), ("rectangle","長方形","名詞"), ("million","百万","名詞"),
    ("stormy","嵐の","形容詞"), ("foggy","霧の","形容詞"), ("dancer","ダンサー","名詞"),
    ("baker","パン職人","名詞"), ("volleyball","バレーボール","名詞"), ("badminton","バドミントン","名詞"),
    ("bookstore","書店","名詞"), ("bakery","パン屋","名詞"), ("pond","池","名詞"),
    ("shampoo","シャンプー","名詞"), ("pillow","枕","名詞"), ("rug","敷物","名詞"),
    ("drawer","引き出し","名詞"), ("glue","糊","名詞"), ("eraser","消しゴム","名詞"),
    ("ruler","定規","名詞"), ("backpack","リュックサック","名詞"), ("sketchbook","スケッチブック","名詞")
]

# Sort and filter
final_words = {}
used_global = set()
for level in ["4級", "3級", "準2級", "2級", "準1級", "1級"]:
    candidates = pools[level]
    # Add common words if needed
    candidates.extend(common_pool)
    
    unique_level_words = []
    seen_in_level = set()
    for eng, jpn, cat in candidates:
        low_eng = eng.lower()
        if low_eng not in existing_words and low_eng not in used_global and low_eng not in seen_in_level:
            unique_level_words.append((eng, jpn, cat))
            seen_in_level.add(low_eng)
            used_global.add(low_eng)
        if len(unique_level_words) >= 100:
            break
    
    final_words[level] = unique_level_words

# Print summary
for level, words in final_words.items():
    print(f"{level}: {len(words)} words")

# Output for copy-pasting
print("DATA = {")
for level, words in final_words.items():
    print(f'    "{level}": {words},')
print("}")

