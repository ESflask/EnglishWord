import SwiftUI

struct FlashcardView: View {
    var viewModel: WordViewModel
    @Binding var isStudying: Bool

    var body: some View {
        Group {
            if viewModel.sessionCompleted {
                ResultView(viewModel: viewModel, isStudying: $isStudying)
            } else if let word = viewModel.currentWord {
                cardContent(word: word)
            }
        }
        .navigationBarBackButtonHidden(true)
    }

    @ViewBuilder
    private func cardContent(word: Word) -> some View {
        VStack(spacing: 6) {
            Text(word.english)
                .font(.title3)
                .fontWeight(.bold)
                .multilineTextAlignment(.center)

            if viewModel.isShowingAnswer {
                Divider()
                Text(word.japanese)
                    .font(.body)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)

                HStack(spacing: 16) {
                    Button {
                        viewModel.markIncorrect()
                    } label: {
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.red)
                            .font(.title2)
                    }
                    .buttonStyle(.plain)

                    Button {
                        viewModel.markCorrect()
                    } label: {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundStyle(.green)
                            .font(.title2)
                    }
                    .buttonStyle(.plain)
                }
            } else {
                Button("答えを見る") {
                    viewModel.showAnswer()
                }
                .font(.caption)
            }

            ProgressView(value: viewModel.progress)
                .tint(.blue)
        }
        .padding()
    }
}
