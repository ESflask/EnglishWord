import SwiftUI

@Observable
final class ThemeManager {
    var current: ColorTheme {
        didSet {
            UserDefaults.standard.set(current.rawValue, forKey: "colorTheme")
        }
    }

    init() {
        let saved = UserDefaults.standard.string(forKey: "colorTheme") ?? ""
        self.current = ColorTheme(rawValue: saved) ?? .dark
    }
}
