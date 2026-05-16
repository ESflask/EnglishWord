import SwiftUI

struct FlashcardView: View {
    var viewModel: WordViewModel
    @Binding var isStudying: Bool
    @Environment(\.dismiss) private var dismiss
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        ZStack {
            themeManager.current.background.ignoresSafeArea()

            Group {
                if viewModel.sessionCompleted {
                    ResultView(viewModel: viewModel, isStudying: $isStudying)
                } else if let word = viewModel.currentWord {
                    cardContent(word: word)
                }
            }
        }
        .navigationBarBackButtonHidden(true)
        .toolbar {
            ToolbarItem(placement: .navigationBarLeading) {
                Button {
                    isStudying = false
                    dismiss()
                } label: {
                    HStack(spacing: 4) {
                        Image(systemName: "chevron.left")
                        Text("ホーム")
                    }
                    .foregroundStyle(themeManager.current.foreground)
                }
            }
        }
    }

    @ViewBuilder
    private func cardContent(word: Word) -> some View {
        VStack(spacing: 24) {
            Spacer()

            VStack(spacing: 16) {
                Text(word.english)
                    .font(.largeTitle.weight(.bold))
                    .foregroundStyle(themeManager.current.foreground)
                    .multilineTextAlignment(.center)

                PartOfSpeechBadge(category: word.category)

                if viewModel.isShowingAnswer {
                    Divider()
                        .overlay(themeManager.current.glassStroke)

                    Text(word.japanese)
                        .font(.title2)
                        .foregroundStyle(themeManager.current.foreground.opacity(0.8))
                        .multilineTextAlignment(.center)
                }
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
            .padding(.horizontal, 24)

            Spacer()

            if viewModel.isShowingAnswer {
                HStack(spacing: 16) {
                    Button {
                        viewModel.markIncorrect()
                    } label: {
                        Label("不正解", systemImage: "xmark.circle.fill")
                    }
                    .buttonStyle(GlassButtonStyle())

                    Button {
                        viewModel.markCorrect()
                    } label: {
                        Label("正解", systemImage: "checkmark.circle.fill")
                    }
                    .buttonStyle(GlassButtonStyle())
                }
                .padding(.horizontal, 24)
            } else {
                Button("答えを見る") {
                    viewModel.showAnswer()
                }
                .buttonStyle(GlassButtonStyle())
                .padding(.horizontal, 24)
            }

            ProgressView(value: viewModel.progress)
                .tint(.blue)
                .padding(.horizontal, 24)
                .padding(.bottom, 32)
        }
    }
}
