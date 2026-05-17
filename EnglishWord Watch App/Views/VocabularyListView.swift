import SwiftUI

struct VocabularyListView: View {
    let level: String
    @Binding var path: NavigationPath
    @Environment(ThemeManager.self) private var themeManager
    @State private var words: [Word] = []

    var body: some View {
        ZStack {
            AppBackground()

            VStack(spacing: 8) {
                if words.isEmpty {
                    ProgressView()
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                } else {
                    ScrollView(.horizontal, showsIndicators: false) {
                        LazyHStack(spacing: 10) {
                            ForEach(words) { word in
                                cardView(word: word)
                                    .containerRelativeFrame(.horizontal) { size, _ in
                                        size - 36
                                    }
                            }
                        }
                        .scrollTargetLayout()
                    }
                    .scrollTargetBehavior(.viewAligned)
                    .scrollClipDisabled()
                }

                Button("ホームに戻る") {
                    path = NavigationPath()
                }
                .font(.caption2)
                .buttonStyle(GlassButtonStyle())
                .padding(.horizontal, 8)
                .padding(.bottom, 4)
            }
        }
        .navigationTitle(level)
        .onAppear {
            if words.isEmpty {
                words = WordDataService().loadAllWords(for: level)
            }
        }
    }

    @ViewBuilder
    private func cardView(word: Word) -> some View {
        ZStack {
            RoundedRectangle(cornerRadius: 14)
                .fill(themeManager.current.glassFill)
                .overlay {
                    RoundedRectangle(cornerRadius: 14)
                        .strokeBorder(themeManager.current.glassStroke, lineWidth: 0.8)
                }
            VStack(spacing: 6) {
                Text(word.english)
                    .font(.title3.weight(.bold))
                    .foregroundStyle(themeManager.current.foreground)
                    .multilineTextAlignment(.center)
                    .minimumScaleFactor(0.7)
                    .lineLimit(2)

                PartOfSpeechBadge(category: word.category)

                Divider()

                Text(word.japanese)
                    .font(.body)
                    .foregroundStyle(themeManager.current.foreground.opacity(0.85))
                    .multilineTextAlignment(.center)
                    .minimumScaleFactor(0.7)
                    .lineLimit(3)
            }
            .padding(10)
        }
    }
}

#Preview {
    NavigationStack {
        VocabularyListView(level: "4級", path: .constant(NavigationPath()))
            .environment(ThemeManager())
    }
}
