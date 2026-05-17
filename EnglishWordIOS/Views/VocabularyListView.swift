import SwiftUI

struct VocabularyListView: View {
    let level: String
    @Binding var path: NavigationPath
    @Environment(ThemeManager.self) private var themeManager
    @State private var words: [Word] = []

    var body: some View {
        ZStack {
            themeManager.current.background.ignoresSafeArea()

            if words.isEmpty {
                ProgressView()
            } else {
                ScrollView(.horizontal, showsIndicators: false) {
                    LazyHStack(spacing: 16) {
                        ForEach(words) { word in
                            cardView(word: word)
                                .containerRelativeFrame(.horizontal) { size, _ in
                                    size - 60
                                }
                        }
                    }
                    .scrollTargetLayout()
                }
                .scrollTargetBehavior(.viewAligned)
                .scrollClipDisabled()
                .padding(.vertical)
            }
        }
        .navigationTitle(level)
        .navigationBarBackButtonHidden(false)
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Button {
                    path = NavigationPath()
                } label: {
                    Label("ホーム", systemImage: "house.fill")
                        .foregroundStyle(themeManager.current.foreground)
                }
            }
        }
        .onAppear {
            if words.isEmpty {
                words = WordDataService().loadAllWords(for: level)
            }
        }
    }

    @ViewBuilder
    private func cardView(word: Word) -> some View {
        VStack(spacing: 20) {
            Spacer()

            VStack(spacing: 16) {
                Text(word.english)
                    .font(.largeTitle.weight(.bold))
                    .foregroundStyle(themeManager.current.foreground)
                    .multilineTextAlignment(.center)
                    .minimumScaleFactor(0.6)
                    .lineLimit(3)

                PartOfSpeechBadge(category: word.category)

                Divider()
                    .overlay(themeManager.current.glassStroke)

                Text(word.japanese)
                    .font(.title2)
                    .foregroundStyle(themeManager.current.foreground.opacity(0.8))
                    .multilineTextAlignment(.center)
                    .minimumScaleFactor(0.7)
                    .lineLimit(4)
            }
            .padding(28)
            .background {
                RoundedRectangle(cornerRadius: 20)
                    .fill(themeManager.current.glassFill)
                    .overlay {
                        RoundedRectangle(cornerRadius: 20)
                            .strokeBorder(themeManager.current.glassStroke, lineWidth: 0.8)
                    }
            }

            Spacer()
        }
        .padding(.horizontal, 4)
    }
}

#Preview {
    NavigationStack {
        VocabularyListView(level: "4級", path: .constant(NavigationPath()))
            .environment(ThemeManager())
    }
}
