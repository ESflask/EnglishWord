import SwiftUI

struct SettingsView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        ZStack {
            AppBackground()

            VStack(spacing: 14) {
                NavigationLink {
                    BackgroundPhotoView()
                } label: {
                    Text("背景")
                }
                .buttonStyle(GlassButtonStyle())

                NavigationLink {
                    ColorThemeView()
                } label: {
                    Text("カラーテーマ")
                }
                .buttonStyle(GlassButtonStyle())

            }
            .padding(.horizontal)
        }
        .navigationTitle("設定")
    }
}

#Preview {
    NavigationStack {
        SettingsView()
            .environment(ThemeManager())
    }
}
