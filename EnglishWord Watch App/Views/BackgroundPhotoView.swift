import SwiftUI
import PhotosUI

struct BackgroundPhotoView: View {
    @Environment(ThemeManager.self) private var themeManager
    @State private var selectedItem: PhotosPickerItem?
    @State private var isLoading = false

    var body: some View {
        ZStack {
            AppBackground()

            VStack(spacing: 12) {
                previewThumbnail

                PhotosPicker(selection: $selectedItem, matching: .images) {
                    Label(isLoading ? "読み込み中..." : "写真を選ぶ", systemImage: "photo.badge.plus")
                }
                .buttonStyle(GlassButtonStyle())
                .disabled(isLoading)

                if themeManager.backgroundImage != nil {
                    Button(role: .destructive) {
                        themeManager.clearBackgroundImage()
                    } label: {
                        Label("背景をリセット", systemImage: "trash")
                            .font(.caption)
                    }
                }
            }
            .padding(.horizontal)
        }
        .navigationTitle("背景")
        .onChange(of: selectedItem) { _, item in
            guard let item else { return }
            isLoading = true
            Task {
                if let data = try? await item.loadTransferable(type: Data.self) {
                    themeManager.setBackgroundImage(data)
                }
                isLoading = false
                selectedItem = nil
            }
        }
    }

    @ViewBuilder
    private var previewThumbnail: some View {
        if let image = themeManager.backgroundImage {
            image
                .resizable()
                .scaledToFill()
                .frame(width: 88, height: 60)
                .clipShape(RoundedRectangle(cornerRadius: 8))
                .overlay(RoundedRectangle(cornerRadius: 8).strokeBorder(themeManager.current.glassStroke))
        } else {
            RoundedRectangle(cornerRadius: 8)
                .fill(themeManager.current.glassFill)
                .frame(width: 88, height: 60)
                .overlay {
                    Image(systemName: "photo")
                        .foregroundStyle(themeManager.current.foreground.opacity(0.4))
                }
        }
    }
}

#Preview {
    NavigationStack {
        BackgroundPhotoView()
            .environment(ThemeManager())
    }
}
