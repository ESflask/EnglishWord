# Management.md
このMarkdownファイルは、Apple Watch でオフラインでもいつでも英単語の学習を促進できるように開発する本アプリを、AIエージェントが正しく・一貫した・丁寧なコーディングができるようにルールや仕様を示したものです。全てのAIエージェントはこれにいかなる時も従ってください。

---

## 1. プロジェクトの概要
- **コンセプト**: Apple Watch でオフラインでもいつでも英単語の学習を促進するApple Watch専用アプリ
- **学習方式**: フラッシュカード形式（単語表示 → 答えを見る → 正誤判定）
- **レベル**: 英検6段階（4級 / 3級 / 準2級 / 2級 / 準1級 / 1級）
- **対応プラットフォーム**: watchOS（メイン）、iOS（コンパニオン）

---

## 2. プロジェクト構成

### Apple Watch App
```
EnglishWord Watch App/
├── EnglishWordApp.swift            # @main エントリポイント・ThemeManager注入
├── ContentView.swift               # ルートView（HomeViewに委譲）
├── Models/
│   ├── Word.swift                  # 単語データモデル（Codable, Identifiable）
│   └── ColorTheme.swift            # カラーテーマ定義（4種）
├── ViewModels/
│   ├── ThemeManager.swift          # テーマ・背景画像管理（@Observable）
│   └── WordViewModel.swift         # 学習セッション管理（@Observable）
├── Views/
│   ├── AppBackground.swift         # 共通背景View（カラーテーマ or 写真）
│   ├── HomeView.swift              # ホーム画面（クイズ・単語帳・設定）
│   ├── LevelSelectView.swift       # レベル選択画面（6段階）
│   ├── FlashcardView.swift         # フラッシュカード（問題→答え→正誤判定）
│   ├── ResultView.swift            # 学習結果画面
│   ├── VocabularyLevelSelectView.swift  # 単語帳用レベル選択画面
│   ├── VocabularyListView.swift    # 横スクロール単語カード（単語帳）
│   ├── PartOfSpeechBadge.swift     # 品詞バッジUI（動詞/名詞/形容詞）
│   ├── GlassButtonStyle.swift      # 共通ボタンスタイル（ガラス質）
│   ├── SettingsView.swift          # 設定メニュー（背景・カラーテーマ）
│   ├── ColorThemeView.swift        # カラーテーマ選択
│   └── BackgroundPhotoView.swift   # 背景写真選択（PhotosPicker）
├── Services/
│   └── WordDataService.swift       # JSON読み込み・UserDefaultsで進捗保存
└── Resources/
    └── words.json                  # 単語データ（3,976語）
```

### iOS App（EnglishWordIOS）
```
EnglishWordIOS/
├── EnglishWordIOSApp.swift
├── ContentView.swift
├── Models/         # ColorTheme.swift, Word.swift（Watch版と同一）
├── ViewModels/     # ThemeManager.swift, WordViewModel.swift
├── Views/
│   ├── HomeView.swift              # タイトル + クイズ・単語帳・設定ボタン
│   ├── LevelSelectView.swift
│   ├── FlashcardView.swift
│   ├── ResultView.swift
│   ├── VocabularyLevelSelectView.swift  # 単語帳用レベル選択画面
│   ├── VocabularyListView.swift    # 横スクロール単語カード（単語帳）
│   ├── PartOfSpeechBadge.swift
│   ├── GlassButtonStyle.swift
│   └── SettingsView.swift          # テーマ選択（Pickerスタイル）
└── Resources/
    └── words.json                  # Watch版と同一データ（3,976語）
```

---

## 3. 技術スタック

| 項目 | 内容 |
|---|---|
| 言語 | Swift 5.9+ |
| UI フレームワーク | SwiftUI（watchOS / iOS） |
| アーキテクチャ | MVVM（`@Observable` マクロ） |
| 学習進捗保存 | `UserDefaults`（isLearned / reviewCount） |
| 背景画像保存 | `Documents/background.dat`（ImageIO で CGImage 変換） |
| 写真選択 | `PhotosUI.PhotosPicker`（watchOS 9+、許可不要） |
| 単語データ | Bundle内 `words.json`（JSONDecoder） |
| Xcode | 26.x（`PBXFileSystemSynchronizedRootGroup` で自動ファイル検出） |
| デプロイターゲット | watchOS 26.2 / iOS（companionなし） |

---

## 4. 単語データ仕様

### ファイル: `Resources/words.json`
- **形式**: JSON配列
- **フィールド**: `id`（UUID）, `english`, `japanese`, `category`（品詞）, `level`（英検級）
- **生成スクリプト**: `gen_words.py`（ルートディレクトリ）

### 語数（Watch・iOS 共通）
| 級 | 語数 |
|---|---|
| 4級 | 516語 |
| 3級 | 563語 |
| 準2級 | 648語 |
| 2級 | 676語 |
| 準1級 | 714語 |
| 1級 | 859語 |
| **合計** | **3,976語** |

### 品詞カテゴリ
`動詞` / `名詞` / `形容詞` / `副詞`

---

## 5. 主要機能一覧

| 機能 | 状態 | 備考 |
|---|---|---|
| フラッシュカード学習 | ✅ 実装済 | 正誤判定 → 結果表示 |
| レベル選択（6段階） | ✅ 実装済 | LevelSelectView |
| 品詞バッジ表示 | ✅ 実装済 | PartOfSpeechBadge（色分け） |
| 学習進捗保存 | ✅ 実装済 | UserDefaults |
| カラーテーマ（4種） | ✅ 実装済 | ダーク・ライト・Tokyo Night・紫 |
| 背景写真設定（Watch） | ✅ 実装済 | PhotosPicker → Documents永続化 |
| 単語帳（横スクロール） | ✅ 実装済 | VocabularyListView |

---

## 6. カラーテーマ定義

| テーマ名 | rawValue | アイコン |
|---|---|---|
| ダーク | `ダーク` | `moon.fill` |
| ライト | `ライト` | `sun.max.fill` |
| Tokyo Night | `青 (Tokyo Night)` | `moon.stars.fill` |
| 紫 | `紫` | `wand.and.stars` |

各テーマは `background`, `foreground`, `glassFill`, `glassStroke` の4プロパティを持つ。

---

## 7. コーディングルール

1. **アーキテクチャ**: MVVMを厳守。ビジネスロジックはViewModelに記述し、Viewは表示のみに徹する
2. **状態管理**: `@Observable` マクロを使用する（`ObservableObject` / `@Published` は使用しない）
3. **背景描画**: 全Viewの背景は `AppBackground()` を ZStack 最背面に配置する（Watch App）
4. **環境オブジェクト**: `ThemeManager` は `.environment(themeManager)` で注入し、各Viewで `@Environment(ThemeManager.self)` で取得する
5. **単語データ追加**: `gen_words.py` を更新後に再実行し、Watch・iOS両方の `words.json` を同期する
6. **コメント**: WHYが非自明な場合のみ記述。WHATを説明するコメントは不要
7. **エラー処理**: システム境界（外部API・ユーザー入力）のみでバリデーションを行う
