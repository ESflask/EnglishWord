# EiTan（英単）

Apple Watch で、オフラインでもいつでも英単語学習ができるアプリです。  
watchOS をメインとし、iOS コンパニオンアプリも同梱しています。

---

## 概要

| 項目 | 内容 |
|---|---|
| 学習方式 | フラッシュカード（単語 → 答え確認 → 正誤判定） |
| 対応レベル | 英検6段階（4級 / 3級 / 準2級 / 2級 / 準1級 / 1級） |
| 収録語数 | **3,976語** |
| プラットフォーム | watchOS（メイン）/ iOS（コンパニオン） |
| オフライン対応 | ✅ すべての単語データはアプリ内に同梱 |

---

## 機能

| 機能 | 説明 |
|---|---|
| フラッシュカード学習 | 単語を見て答えを確認し、正誤を自己判定 |
| レベル選択 | 英検6段階からレベルを選んで学習 |
| 単語帳 | レベルごとに全単語を横スクロールで一覧表示 |
| 品詞バッジ表示 | 動詞・名詞・形容詞・副詞を色分けで表示 |
| 学習進捗保存 | 学習済み単語と復習回数を記録（UserDefaults） |
| カラーテーマ | ダーク / ライト / Tokyo Night / 紫 の4種 |
| 背景写真設定 | フォトライブラリから選んだ画像を背景に設定（Watch） |

---

## 収録語数

| 級 | 語数 |
|---|---|
| 4級 | 516語 |
| 3級 | 563語 |
| 準2級 | 648語 |
| 2級 | 676語 |
| 準1級 | 714語 |
| 1級 | 859語 |
| **合計** | **3,976語** |

---

## 技術スタック

| 項目 | 内容 |
|---|---|
| 言語 | Swift 5.9+ |
| UI フレームワーク | SwiftUI |
| アーキテクチャ | MVVM（`@Observable` マクロ） |
| 単語データ | Bundle 内 `words.json`（JSONDecoder） |
| 進捗保存 | UserDefaults |
| 背景画像保存 | Documents/background.dat（ImageIO） |
| 写真選択 | PhotosUI.PhotosPicker |
| Xcode | 26.x |
| デプロイターゲット | watchOS 26.2 / iOS 18+ |

---

## プロジェクト構成

```
EnglishWord/
├── EnglishWord Watch App/      # watchOS アプリ（メイン）
│   ├── Models/                 # Word, ColorTheme
│   ├── ViewModels/             # ThemeManager, WordViewModel
│   ├── Views/                  # 各画面（HomeView, FlashcardView, VocabularyListView など）
│   ├── Services/               # WordDataService（JSON読み込み・進捗保存）
│   └── Resources/words.json   # 単語データ（3,976語）
├── EnglishWordIOS/             # iOS コンパニオンアプリ
│   ├── Models/
│   ├── ViewModels/
│   ├── Views/
│   └── Resources/words.json   # Watch版と同一データ
├── gen_words.py                # 単語データ生成スクリプト
└── Management.md               # 開発ルール・仕様書
```

---

## 開発ルール

- アーキテクチャは MVVM を厳守。`@Observable` を使い、`ObservableObject` / `@Published` は使用しない
- 全 View の背景は `AppBackground()` を ZStack 最背面に配置する
- 単語データを変更する場合は `gen_words.py` を再実行し、Watch・iOS 両方の `words.json` を同期する
- 詳細は [Management.md](Management.md) を参照
