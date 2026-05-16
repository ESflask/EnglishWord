import SwiftUI

struct GlassButtonStyle: ButtonStyle {
    @Environment(ThemeManager.self) private var themeManager

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.title3.weight(.semibold))
            .foregroundStyle(themeManager.current.foreground)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background {
                RoundedRectangle(cornerRadius: 16)
                    .fill(themeManager.current.glassFill)
                    .overlay {
                        RoundedRectangle(cornerRadius: 16)
                            .strokeBorder(themeManager.current.glassStroke, lineWidth: 0.8)
                    }
            }
            .scaleEffect(configuration.isPressed ? 0.97 : 1.0)
            .opacity(configuration.isPressed ? 0.75 : 1.0)
            .animation(.easeOut(duration: 0.12), value: configuration.isPressed)
    }
}
