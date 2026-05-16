import SwiftUI

struct ResultView: View {
    var viewModel: WordViewModel
    @Binding var isStudying: Bool
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        VStack(spacing: 24) {
            Spacer()

            Image(systemName: "checkmark.seal.fill")
                .font(.system(size: 72))
                .foregroundStyle(.green)

            Text("完了!")
                .font(.largeTitle.weight(.bold))
                .foregroundStyle(themeManager.current.foreground)

            Text("\(viewModel.correctCount) / \(viewModel.words.count) 正解")
                .font(.title2)
                .foregroundStyle(themeManager.current.foreground.opacity(0.7))

            Spacer()

            VStack(spacing: 14) {
                Button("もう一度") {
                    viewModel.resetSession()
                }
                .buttonStyle(GlassButtonStyle())

                Button("ホームへ戻る") {
                    isStudying = false
                }
                .buttonStyle(GlassButtonStyle())
            }
            .padding(.horizontal, 32)
            .padding(.bottom, 40)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(themeManager.current.background.ignoresSafeArea())
        .navigationBarBackButtonHidden(true)
    }
}
