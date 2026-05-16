//
//  EnglishWordApp.swift
//  EnglishWord Watch App
//
//  Created by 遠藤省吾 on R 8/05/16.
//

import SwiftUI

@main
struct EnglishWord_Watch_AppApp: App {
    @State private var themeManager = ThemeManager()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(themeManager)
        }
    }
}
