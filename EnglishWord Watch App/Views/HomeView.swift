import SwiftUI

enum AppRoute: Hashable {
    case quizLevelSelect
    case vocabularyLevelSelect
    case vocabularyList(String)
}

struct HomeView: View {
    @Environment(ThemeManager.self) private var themeManager
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            ZStack {
                AppBackground()

                VStack(spacing: 14) {
                    Button("クイズ") {
                        path.append(AppRoute.quizLevelSelect)
                    }
                    .buttonStyle(GlassButtonStyle())

                    Button("単語帳") {
                        path.append(AppRoute.vocabularyLevelSelect)
                    }
                    .buttonStyle(GlassButtonStyle())

                    NavigationLink {
                        SettingsView()
                    } label: {
                        Text("設定")
                    }
                    .buttonStyle(GlassButtonStyle())
                }
                .padding(.horizontal)
            }
            .navigationTitle("英単語")
            .navigationDestination(for: AppRoute.self) { route in
                switch route {
                case .quizLevelSelect:
                    LevelSelectView()
                case .vocabularyLevelSelect:
                    VocabularyLevelSelectView(path: $path)
                case .vocabularyList(let level):
                    VocabularyListView(level: level, path: $path)
                }
            }
        }
    }
}

#Preview {
    HomeView()
        .environment(ThemeManager())
}
