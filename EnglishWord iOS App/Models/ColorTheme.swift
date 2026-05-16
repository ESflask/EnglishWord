import SwiftUI

enum ColorTheme: String, CaseIterable, Codable {
    case dark = "ダーク"
    case light = "ライト"

    var background: Color {
        switch self {
        case .dark: return .black
        case .light: return .white
        }
    }

    var foreground: Color {
        switch self {
        case .dark: return .white
        case .light: return .black
        }
    }

    var glassFill: Color {
        switch self {
        case .dark: return .white.opacity(0.10)
        case .light: return .black.opacity(0.07)
        }
    }

    var glassStroke: Color {
        switch self {
        case .dark: return .white.opacity(0.25)
        case .light: return .black.opacity(0.18)
        }
    }

    var icon: String {
        switch self {
        case .dark: return "moon.fill"
        case .light: return "sun.max.fill"
        }
    }
}
