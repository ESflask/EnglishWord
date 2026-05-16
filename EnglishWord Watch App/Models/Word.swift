import Foundation

struct Word: Identifiable, Codable {
    let id: UUID
    let english: String
    let japanese: String
    let category: String
    var isLearned: Bool = false
    var reviewCount: Int = 0

    enum CodingKeys: String, CodingKey {
        case id, english, japanese, category
    }
}
