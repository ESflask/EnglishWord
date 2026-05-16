import SwiftUI

struct ColorThemeView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        ZStack {
            AppBackground()

            ScrollView {
                VStack(spacing: 10) {
                    ForEach(ColorTheme.allCases, id: \.self) { theme in
                        Button {
                            themeManager.current = theme
                        } label: {
                            HStack {
                                Image(systemName: theme.icon)
                                Text(theme.rawValue)
                                Spacer()
                                if themeManager.current == theme {
                                    Image(systemName: "checkmark")
                                        .font(.caption.weight(.bold))
                                }
                            }
                        }
                        .buttonStyle(GlassButtonStyle())
                    }
                }
                .padding(.horizontal)
            }
        }
        .navigationTitle("カラーテーマ")
    }
}

#Preview {
    NavigationStack {
        ColorThemeView()
            .environment(ThemeManager())
    }
}
