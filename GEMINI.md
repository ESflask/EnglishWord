# GEMINI.md

プロジェクトの仕様・ルールは `Management.md` を参照すること。
全てのコーディングルール・アーキテクチャ・ファイル構成はそこに定義されている。

## 要点
- アーキテクチャ: MVVM（`@Observable`マクロ、`ObservableObject`は使わない）
- 対象プラットフォーム: watchOS（メイン）、iOS（コンパニオン）
- 単語データ変更時は `gen_words.py` を再実行し Watch/iOS 両方の `words.json` を同期する
- 背景: 全Viewで `AppBackground()` を ZStack 最背面に置く
- コメント: WHYが非自明な場合のみ記述する
