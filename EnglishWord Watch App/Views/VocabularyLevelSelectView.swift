import SwiftUI

struct VocabularyLevelSelectView: View {
    @Environment(ThemeManager.self) private var themeManager
    @Binding var path: NavigationPath

    private let levels = ["4級", "3級", "準2級", "2級", "準1級", "1級"]

    var body: some View {
        ZStack {
            AppBackground()

            ScrollView {
                VStack(spacing: 10) {
                    ForEach(levels, id: \.self) { level in
                        Button(level) {
                            path.append(AppRoute.vocabularyList(level))
                        }
                        .buttonStyle(GlassButtonStyle())
                    }
                }
                .padding(.horizontal)
            }
        }
        .navigationTitle("単語帳")
    }
}

#Preview {
    NavigationStack {
        VocabularyLevelSelectView(path: .constant(NavigationPath()))
            .environment(ThemeManager())
    }
}
