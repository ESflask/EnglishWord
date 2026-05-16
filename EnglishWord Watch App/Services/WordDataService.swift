import Foundation

final class WordDataService {
    private let progressKey = "wordProgress"

    func loadWords(for level: String) -> [Word] {
        guard let url = Bundle.main.url(forResource: "words", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let baseWords = try? JSONDecoder().decode([Word].self, from: data)
        else { return [] }

        let filtered = baseWords.filter { $0.level == level }
        let progress = loadProgress()
        let all = filtered.map { word -> Word in
            var w = word
            if let p = progress[word.id.uuidString] {
                w.isLearned = p.isLearned
                w.reviewCount = p.reviewCount
            }
            return w
        }
        return Array(all.shuffled().prefix(30))
    }

    func saveProgress(for words: [Word]) {
        var progress: [String: ProgressEntry] = [:]
        for word in words {
            progress[word.id.uuidString] = ProgressEntry(isLearned: word.isLearned, reviewCount: word.reviewCount)
        }
        if let data = try? JSONEncoder().encode(progress) {
            UserDefaults.standard.set(data, forKey: progressKey)
        }
    }

    private func loadProgress() -> [String: ProgressEntry] {
        guard let data = UserDefaults.standard.data(forKey: progressKey),
              let progress = try? JSONDecoder().decode([String: ProgressEntry].self, from: data)
        else { return [:] }
        return progress
    }
}

private struct ProgressEntry: Codable {
    var isLearned: Bool
    var reviewCount: Int
}
