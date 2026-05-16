import SwiftUI

struct AppBackground: View {
    @Environment(ThemeManager.self) private var themeManager

    var body: some View {
        Group {
            if let image = themeManager.backgroundImage {
                image
                    .resizable()
                    .scaledToFill()
            } else {
                themeManager.current.background
            }
        }
        .ignoresSafeArea()
    }
}
