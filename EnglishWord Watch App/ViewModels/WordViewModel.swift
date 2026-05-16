import SwiftUI

@Observable
final class WordViewModel {
    var words: [Word] = []
    var currentIndex: Int = 0
    var isShowingAnswer: Bool = false
    var sessionCompleted: Bool = false
    var correctCount: Int = 0

    private let dataService = WordDataService()
    private var currentLevel: String = ""

    var currentWord: Word? {
        words.indices.contains(currentIndex) ? words[currentIndex] : nil
    }

    var progress: Double {
        words.isEmpty ? 0 : Double(currentIndex) / Double(words.count)
    }

    func loadWords(level: String) {
        currentLevel = level
        words = dataService.loadWords(for: level)
        resetCounters()
    }

    func showAnswer() {
        isShowingAnswer = true
    }

    func markCorrect() {
        guard words.indices.contains(currentIndex) else { return }
        words[currentIndex].isLearned = true
        words[currentIndex].reviewCount += 1
        correctCount += 1
        advance()
    }

    func markIncorrect() {
        guard words.indices.contains(currentIndex) else { return }
        words[currentIndex].reviewCount += 1
        advance()
    }

    // 「もう一度」: 新しい30語を引き直してセッションをリセット
    func resetSession() {
        guard !currentLevel.isEmpty else { return }
        words = dataService.loadWords(for: currentLevel)
        resetCounters()
    }

    private func resetCounters() {
        currentIndex = 0
        isShowingAnswer = false
        sessionCompleted = false
        correctCount = 0
    }

    private func advance() {
        isShowingAnswer = false
        if currentIndex + 1 >= words.count {
            dataService.saveProgress(for: words)
            sessionCompleted = true
        } else {
            currentIndex += 1
        }
    }
}
