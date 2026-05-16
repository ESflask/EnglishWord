# Management.md
このmarkdownファイルは、Apple Watch でオフラインでもいつでも英単語の学習を促進できるように開発する本アプリをAIエージェントが正しく一貫した丁寧なコーディングができるようにルールなどを示したのもで、全てのAIエージェントはこれにいかなる時も従ってください。AIエージェントは、
##1. プロジェクトの概要
- このプロジェクトは、Apple Watch でオフラインでもいつでも英単語の学習を促進させるというコンセプトのApple Watch用アプリです。
- 
##2. プロジェクト構成

```
EnglishWord Watch App/
├── EnglishWordApp.swift        # @main エントリポイント
├── ContentView.swift           # ルートView（HomeViewに委譲）
├── Models/
│   └── Word.swift              # 単語データモデル
├── ViewModels/
│   └── WordViewModel.swift     # 学習セッション管理（@Observable）
├── Views/
│   ├── HomeView.swift          # ホーム画面（進捗表示・学習開始）
│   ├── FlashcardView.swift     # フラッシュカード（問題/正誤判定）
│   └── ResultView.swift        # 学習結果画面
├── Services/
│   └── WordDataService.swift   # 単語データ読み込み・進捗保存
├── Resources/
│   └── words.json              # 単語データ（英語・日本語訳・カテゴリ）
└── Assets.xcassets/
```

##3. 技術スタック

- **言語**: Swift 5.9+
- **UI フレームワーク**: SwiftUI（watchOS向け）
- **アーキテクチャ**: MVVM（@Observable マクロ使用）
- **データ永続化**: UserDefaults（学習進捗）、Bundle JSON（単語データ）
- **対応プラットフォーム**: watchOS（Apple Watch専用、スタンドアロン）
- **Xcode**: 26.x（PBXFileSystemSynchronizedRootGroup によるファイル自動検出）
