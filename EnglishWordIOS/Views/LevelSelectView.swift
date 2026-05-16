import SwiftUI

struct LevelSelectView: View {
    @Environment(ThemeManager.self) private var themeManager
    @State private var viewModel = WordViewModel()
    @State private var isStudying = false

    private let levels = ["4級", "3級", "準2級", "2級", "準1級", "1級"]

    var body: some View {
        ZStack {
            themeManager.current.background.ignoresSafeArea()

            ScrollView {
                VStack(spacing: 14) {
                    ForEach(levels, id: \.self) { level in
                        Button(level) {
                            viewModel.loadWords(level: level)
                            isStudying = true
                        }
                        .buttonStyle(GlassButtonStyle())
                    }
                }
                .padding(.horizontal, 32)
                .padding(.vertical, 20)
            }
        }
        .navigationTitle("レベル選択")
        .navigationDestination(isPresented: $isStudying) {
            FlashcardView(viewModel: viewModel, isStudying: $isStudying)
        }
    }
}

#Preview {
    NavigationStack {
        LevelSelectView()
            .environment(ThemeManager())
    }
}
