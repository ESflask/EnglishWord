import SwiftUI

enum ColorTheme: String, CaseIterable, Codable {
    case dark = "ダーク"
    case light = "ライト"
    case tokyoNight = "青 (Tokyo Night)"
    case purple = "紫"

    var background: Color {
        switch self {
        case .dark:       return .black
        case .light:      return .white
        case .tokyoNight: return Color(red: 0.102, green: 0.106, blue: 0.149) // #1a1b26
        case .purple:     return Color(red: 0.102, green: 0.000, blue: 0.180) // #1a002e
        }
    }

    var foreground: Color {
        switch self {
        case .dark:       return .white
        case .light:      return .black
        case .tokyoNight: return Color(red: 0.753, green: 0.792, blue: 0.961) // #c0caf5
        case .purple:     return Color(red: 0.910, green: 0.835, blue: 0.980) // #e8d5fa
        }
    }

    var glassFill: Color {
        switch self {
        case .dark:       return .white.opacity(0.10)
        case .light:      return .black.opacity(0.07)
        case .tokyoNight: return Color(red: 0.478, green: 0.635, blue: 0.969).opacity(0.15) // #7aa2f7
        case .purple:     return Color(red: 0.580, green: 0.259, blue: 0.910).opacity(0.15) // #9442e8
        }
    }

    var glassStroke: Color {
        switch self {
        case .dark:       return .white.opacity(0.25)
        case .light:      return .black.opacity(0.18)
        case .tokyoNight: return Color(red: 0.478, green: 0.635, blue: 0.969).opacity(0.40) // #7aa2f7
        case .purple:     return Color(red: 0.580, green: 0.259, blue: 0.910).opacity(0.45) // #9442e8
        }
    }

    var icon: String {
        switch self {
        case .dark:       return "moon.fill"
        case .light:      return "sun.max.fill"
        case .tokyoNight: return "moon.stars.fill"
        case .purple:     return "wand.and.stars"
        }
    }
}
