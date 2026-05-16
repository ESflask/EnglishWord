import SwiftUI

struct PartOfSpeechBadge: View {
    let category: String

    private var color: Color {
        switch category {
        case "動詞":
            return .orange
        case "名詞":
            return .blue
        case "形容詞":
            return .green
        case "副詞":
            return .purple
        default:
            return .gray
        }
    }

    var body: some View {
        Text(category)
            .font(.caption2.weight(.semibold))
            .foregroundStyle(color)
            .padding(.horizontal, 8)
            .padding(.vertical, 3)
            .background {
                Capsule()
                    .fill(color.opacity(0.16))
            }
            .overlay {
                Capsule()
                    .strokeBorder(color.opacity(0.45), lineWidth: 0.8)
            }
    }
}
