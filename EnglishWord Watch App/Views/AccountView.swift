import SwiftUI

struct AccountView: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        ZStack {
            AppBackground()

            Text("近日公開予定")
                .font(.caption)
                .foregroundStyle(themeManager.current.foreground.opacity(0.6))
        }
        .navigationTitle("アカウント")
    }
}

#Preview {
    NavigationStack {
        AccountView()
            .environment(ThemeManager())
    }
}
