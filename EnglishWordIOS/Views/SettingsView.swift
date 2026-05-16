import SwiftUI

struct SettingsView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        ZStack {
            themeManager.current.background.ignoresSafeArea()

            VStack(spacing: 20) {
                HStack {
                    Text("テーマ")
                        .font(.headline)
                        .foregroundStyle(themeManager.current.foreground)
                    Spacer()
                    Picker("テーマ", selection: Bindable(themeManager).current) {
                        ForEach(ColorTheme.allCases, id: \.self) { theme in
                            Label(theme.rawValue, systemImage: theme.icon)
                                .tag(theme)
                        }
                    }
                    .pickerStyle(.segmented)
                    .frame(width: 160)
                }
                .padding()
                .background {
                    RoundedRectangle(cornerRadius: 16)
                        .fill(themeManager.current.glassFill)
                        .overlay {
                            RoundedRectangle(cornerRadius: 16)
                                .strokeBorder(themeManager.current.glassStroke, lineWidth: 0.8)
                        }
                }

                Spacer()
            }
            .padding(.horizontal, 24)
            .padding(.top, 20)
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
