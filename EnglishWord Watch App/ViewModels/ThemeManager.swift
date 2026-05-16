import SwiftUI
import ImageIO

@Observable
final class ThemeManager {
    var current: ColorTheme {
        didSet {
            UserDefaults.standard.set(current.rawValue, forKey: "colorTheme")
        }
    }

    private(set) var backgroundImage: Image? = nil

    private static let imageFileURL: URL = {
        let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        return docs.appendingPathComponent("background.dat")
    }()

    init() {
        let saved = UserDefaults.standard.string(forKey: "colorTheme") ?? ""
        self.current = ColorTheme(rawValue: saved) ?? .dark
        if let data = try? Data(contentsOf: Self.imageFileURL) {
            self.backgroundImage = Self.makeImage(from: data)
        }
    }

    func setBackgroundImage(_ data: Data) {
        try? data.write(to: Self.imageFileURL)
        backgroundImage = Self.makeImage(from: data)
    }

    func clearBackgroundImage() {
        try? FileManager.default.removeItem(at: Self.imageFileURL)
        backgroundImage = nil
    }

    private static func makeImage(from data: Data) -> Image? {
        guard let source = CGImageSourceCreateWithData(data as CFData, nil),
              let cgImage = CGImageSourceCreateImageAtIndex(source, 0, nil)
        else { return nil }
        return Image(cgImage, scale: 1.0, orientation: .up, label: Text("背景"))
    }
}
