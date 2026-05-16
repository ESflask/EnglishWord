import SwiftUI

struct HomeView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        NavigationStack {
            ZStack {
                themeManager.current.background.ignoresSafeArea()

                VStack(spacing: 20) {
                    Spacer()

                    Text("英単語")
                        .font(.largeTitle.weight(.bold))
                        .foregroundStyle(themeManager.current.foreground)

                    Spacer()

                    VStack(spacing: 14) {
                        NavigationLink {
                            Text("レベル選択")  // LevelSelectView に後で置き換え
                        } label: {
                            Text("スタート")
                        }
                        .buttonStyle(GlassButtonStyle())

                        NavigationLink {
                            Text("設定")  // SettingsView に後で置き換え
                        } label: {
                            Text("設定")
                        }
                        .buttonStyle(GlassButtonStyle())
                    }
                    .padding(.horizontal, 32)

                    Spacer()
                }
            }
        }
    }
}

#Preview {
    HomeView()
        .environment(ThemeManager())
}
