import SwiftUI

struct HomeView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        NavigationStack {
            ZStack {
                AppBackground()

                VStack(spacing: 14) {
                    NavigationLink {
                        LevelSelectView()
                    } label: {
                        Text("スタート")
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
        }
    }
}

#Preview {
    HomeView()
        .environment(ThemeManager())
}
