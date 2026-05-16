import SwiftUI

struct SettingsView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        ZStack {
            themeManager.current.background.ignoresSafeArea()

            VStack(spacing: 14) {
                NavigationLink {
                    ColorThemeView()
                } label: {
                    Text("カラーテーマ")
                }
                .buttonStyle(GlassButtonStyle())

                NavigationLink {
                    AccountView()
                } label: {
                    Text("アカウント")
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
