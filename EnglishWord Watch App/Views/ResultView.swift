import SwiftUI

struct ResultView: View {
    var viewModel: WordViewModel
    @Binding var isStudying: Bool

    var body: some View {
        VStack(spacing: 8) {
            Image(systemName: "checkmark.seal.fill")
                .font(.largeTitle)
                .foregroundStyle(.green)

            Text("完了!")
                .font(.headline)

            Text("\(viewModel.correctCount)/\(viewModel.words.count) 正解")
                .font(.body)
                .foregroundStyle(.secondary)

            Button("もう一度") {
                viewModel.resetSession()
            }
            .font(.caption)

            Button("ホームへ") {
                isStudying = false
            }
            .font(.caption)
            .foregroundStyle(.secondary)
        }
        .padding()
        .navigationBarBackButtonHidden(true)
    }
}
